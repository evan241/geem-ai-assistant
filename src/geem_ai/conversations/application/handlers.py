from __future__ import annotations

from collections.abc import Callable
from datetime import datetime

from geem_ai.conversations.application.commands import (
    CreateConversationCommand,
    SendConversationMessageCommand,
)
from geem_ai.conversations.application.exceptions import ConversationNotFoundError
from geem_ai.conversations.application.ports.repositories import (
    ConversationReadRepository,
)
from geem_ai.conversations.application.ports.unit_of_work import (
    ConversationUnitOfWorkFactory,
)
from geem_ai.conversations.application.queries import GetConversationQuery
from geem_ai.conversations.application.results import (
    CreateConversationResult,
    SendConversationMessageResult,
)
from geem_ai.conversations.application.views import ConversationView
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId


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
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._message_id_factory = message_id_factory
        self._execution_id_factory = execution_id_factory
        self._clock = clock

    def handle(
        self,
        command: SendConversationMessageCommand,
    ) -> SendConversationMessageResult:
        if command.actor.user_id is None:
            raise ValueError("User actor is required to send a conversation message.")

        capability = self._resolve_capability(command.capability_hint)
        now = self._clock()

        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
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
            unit_of_work.commit()

        return SendConversationMessageResult(
            user_message_id=user_message.id,
            assistant_execution_id=execution.id,
            execution_status=execution.status.value,
            capability=execution.capability.value,
        )

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
