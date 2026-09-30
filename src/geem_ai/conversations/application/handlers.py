from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timedelta
from uuid import UUID

from geem_ai.conversations.application.commands import (
    ClaimAssistantExecutionCommand,
    CompleteAssistantExecutionCommand,
    CreateConversationCommand,
    FailAssistantExecutionCommand,
    SendConversationMessageCommand,
)
from geem_ai.conversations.application.events import assistant_execution_requested
from geem_ai.conversations.application.exceptions import (
    AssistantExecutionNotFoundError,
    ConversationNotFoundError,
    IdempotencyKeyConflictError,
    IdempotencyRequestInProgressError,
    InvalidIdempotencyKeyError,
)
from geem_ai.conversations.application.idempotency import (
    IDEMPOTENCY_TTL_HOURS,
    SEND_MESSAGE_IDEMPOTENCY_SCOPE,
    IdempotencyRecord,
    deserialize_send_message_result,
    send_message_request_hash,
    serialize_send_message_result,
)
from geem_ai.conversations.application.ports.repositories import (
    ConversationReadRepository,
)
from geem_ai.conversations.application.ports.unit_of_work import (
    ConversationUnitOfWorkFactory,
)
from geem_ai.conversations.application.queries import GetConversationQuery
from geem_ai.conversations.application.results import (
    ClaimAssistantExecutionResult,
    CreateConversationResult,
    SendConversationMessageResult,
)
from geem_ai.conversations.application.views import ConversationView
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId


class ClaimAssistantExecutionHandler:
    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        clock: Callable[[], datetime],
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._clock = clock

    def handle(self, command: ClaimAssistantExecutionCommand) -> ClaimAssistantExecutionResult:
        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
            execution = unit_of_work.executions.get_for_update(
                command.actor.tenant_id, command.execution_id
            )
            if execution is None:
                raise AssistantExecutionNotFoundError()

            execution.start(now=self._clock())
            unit_of_work.executions.save(execution)
            unit_of_work.commit()

        return ClaimAssistantExecutionResult(execution=execution)


class CompleteAssistantExecutionHandler:
    """Atomically persist the final message and its execution completion."""

    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        clock: Callable[[], datetime],
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._clock = clock

    def handle(self, command: CompleteAssistantExecutionCommand) -> None:
        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
            execution = unit_of_work.executions.get_for_update(
                command.actor.tenant_id, command.execution_id
            )
            if execution is None:
                raise AssistantExecutionNotFoundError()

            completed_at = self._clock()
            assistant_message = Message.create_assistant(
                message_id=command.assistant_message_id,
                conversation_id=execution.conversation_id,
                tenant_id=execution.tenant_id,
                content=command.result.content,
                execution_id=execution.id,
                now=completed_at,
            )
            assistant_message.complete(now=completed_at)
            execution.complete(
                assistant_message_id=assistant_message.id,
                provider=command.result.provider,
                model=command.result.model,
                input_tokens=command.result.usage.input_tokens,
                output_tokens=command.result.usage.output_tokens,
                total_tokens=command.result.usage.total_tokens,
                cost_amount=command.result.estimated_cost,
                latency_ms=command.result.latency_ms,
                now=completed_at,
            )

            unit_of_work.messages.add(assistant_message)
            unit_of_work.executions.save(execution)
            unit_of_work.commit()


class FailAssistantExecutionHandler:
    """Persist a safe terminal failure for a running execution."""

    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        clock: Callable[[], datetime],
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._clock = clock

    def handle(self, command: FailAssistantExecutionCommand) -> None:
        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
            execution = unit_of_work.executions.get_for_update(
                command.actor.tenant_id, command.execution_id
            )
            if execution is None:
                raise AssistantExecutionNotFoundError()

            execution.fail(
                failure_code=command.failure_code,
                failure_detail=command.safe_detail,
                now=self._clock(),
            )
            unit_of_work.executions.save(execution)
            unit_of_work.commit()


class CreateConversationHandler:
    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        conversation_id_factory: Callable[[], ConversationId],
        clock: Callable[[], datetime],
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._conversation_id_factory = conversation_id_factory
        self._clock = clock

    def handle(
        self,
        command: CreateConversationCommand,
    ) -> CreateConversationResult:
        if command.actor.user_id is None:
            raise ValueError("User actor is required to create a conversation.")

        now = self._clock()

        conversation = Conversation.create(
            conversation_id=self._conversation_id_factory(),
            tenant_id=command.actor.tenant_id,
            owner_user_id=command.actor.user_id,
            title=command.title or "",
            language=command.language,
            now=now,
        )

        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
            unit_of_work.conversations.add(conversation)
            unit_of_work.commit()

        return CreateConversationResult(
            conversation_id=conversation.id,
            title=conversation.title,
            status=conversation.status.value,
            language=conversation.language.value,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            version=conversation.version,
        )


class SendConversationMessageHandler:
    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        message_id_factory: Callable[[], MessageId],
        execution_id_factory: Callable[[], ExecutionId],
        clock: Callable[[], datetime],
        idempotency_id_factory: Callable[[], UUID],
        outbox_event_id_factory: Callable[[], UUID],
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._message_id_factory = message_id_factory
        self._execution_id_factory = execution_id_factory
        self._clock = clock
        self._idempotency_id_factory = idempotency_id_factory
        self._outbox_event_id_factory = outbox_event_id_factory

    def handle(
        self,
        command: SendConversationMessageCommand,
    ) -> SendConversationMessageResult:
        if command.actor.user_id is None:
            raise ValueError("User actor is required to send a conversation message.")

        self._validate_idempotency_key(command.idempotency_key)
        capability = self._resolve_capability(command.capability_hint)
        now = self._clock()
        request_hash = send_message_request_hash(
            conversation_id=command.conversation_id,
            content=command.content,
            capability=capability.value,
        )

        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
            idempotency_record = IdempotencyRecord(
                id=self._idempotency_id_factory(),
                tenant_id=command.actor.tenant_id.value,
                scope=SEND_MESSAGE_IDEMPOTENCY_SCOPE,
                idempotency_key=command.idempotency_key,
                request_hash=request_hash,
                status="processing",
                response_status=None,
                response_body=None,
                resource_type=None,
                resource_id=None,
                created_at=now,
                completed_at=None,
                expires_at=now + timedelta(hours=IDEMPOTENCY_TTL_HOURS),
            )
            if not unit_of_work.idempotency.reserve(idempotency_record):
                existing = unit_of_work.idempotency.get(
                    command.actor.tenant_id,
                    SEND_MESSAGE_IDEMPOTENCY_SCOPE,
                    command.idempotency_key,
                )
                if existing is None:
                    raise RuntimeError("Reserved idempotency record could not be loaded.")
                if existing.request_hash != request_hash:
                    raise IdempotencyKeyConflictError()
                if existing.status == "processing":
                    raise IdempotencyRequestInProgressError()
                if existing.status == "completed" and existing.response_body is not None:
                    return deserialize_send_message_result(existing.response_body)
                raise IdempotencyRequestInProgressError()
            conversation = unit_of_work.conversations.get_by_id(
                command.actor.tenant_id,
                command.conversation_id,
            )
            if conversation is None:
                raise ConversationNotFoundError()

            user_message = conversation.add_user_message(
                message_id=self._message_id_factory(),
                content=command.content,
                author_id=command.actor.user_id,
                now=now,
            )
            execution = AssistantExecution.create(
                execution_id=self._execution_id_factory(),
                tenant_id=command.actor.tenant_id,
                conversation_id=conversation.id,
                user_message_id=user_message.id,
                capability=capability,
                now=now,
            )

            unit_of_work.conversations.save(conversation)
            unit_of_work.messages.add(user_message)
            unit_of_work.executions.add(execution)
            unit_of_work.outbox.add(
                assistant_execution_requested(
                    event_id=self._outbox_event_id_factory(), execution=execution, now=now
                )
            )
            result = SendConversationMessageResult(
                user_message_id=user_message.id,
                assistant_execution_id=execution.id,
                execution_status=execution.status.value,
                capability=execution.capability.value,
            )
            unit_of_work.idempotency.complete(
                idempotency_record,
                response_status=200,
                response_body=serialize_send_message_result(result),
                resource_type="assistant_execution",
                resource_id=execution.id.value,
                completed_at=now,
            )
            unit_of_work.commit()

        return result

    @staticmethod
    def _validate_idempotency_key(key: str) -> None:
        if not key or not key.strip():
            raise InvalidIdempotencyKeyError("Idempotency key must not be blank.")
        if len(key) > 255:
            raise InvalidIdempotencyKeyError("Idempotency key must not exceed 255 characters.")

    @staticmethod
    def _resolve_capability(capability_hint: str | None) -> ExecutionCapability:
        if capability_hint in {None, ExecutionCapability.DIRECT_RESPONSE.value}:
            return ExecutionCapability.DIRECT_RESPONSE
        raise ValueError(f"Unsupported execution capability: {capability_hint}")


class GetConversationHandler:
    def __init__(
        self,
        *,
        repository: ConversationReadRepository,
    ) -> None:
        self._repository = repository

    def handle(
        self,
        query: GetConversationQuery,
    ) -> ConversationView:
        conversation = self._repository.get_view(
            query.actor.tenant_id,
            query.conversation_id,
        )

        if conversation is None:
            raise ConversationNotFoundError()

        return conversation
