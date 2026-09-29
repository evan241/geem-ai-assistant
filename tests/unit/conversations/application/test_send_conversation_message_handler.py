from datetime import UTC, datetime
from typing import Self
from uuid import uuid4

import pytest

from geem_ai.conversations.application.commands import SendConversationMessageCommand
from geem_ai.conversations.application.exceptions import ConversationNotFoundError
from geem_ai.conversations.application.handlers import SendConversationMessageHandler
from geem_ai.conversations.application.idempotency import IdempotencyRecord
from geem_ai.conversations.application.ports.repositories import (
    AssistantExecutionRepository,
    ConversationRepository,
    IdempotencyRepository,
    MessageRepository,
)
from geem_ai.conversations.application.ports.unit_of_work import ConversationUnitOfWork
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ConversationStatus
from geem_ai.conversations.domain.exceptions import (
    ConversationNotActiveError,
    InvalidMessageContentError,
)
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.actor import Actor, ActorType
from geem_ai.shared.domain.ids import (
    ConversationId,
    ExecutionId,
    MessageId,
    TenantId,
    UserId,
)


class FakeConversationRepository:
    def __init__(self, conversations: list[Conversation]) -> None:
        self.conversations = conversations
        self.lookups: list[tuple[TenantId, ConversationId]] = []
        self.saved: list[Conversation] = []

    def add(self, conversation: Conversation) -> None:
        self.conversations.append(conversation)

    def save(self, conversation: Conversation) -> None:
        self.saved.append(conversation)

    def get_by_id(
        self, tenant_id: TenantId, conversation_id: ConversationId
    ) -> Conversation | None:
        self.lookups.append((tenant_id, conversation_id))
        return next(
            (
                conversation
                for conversation in self.conversations
                if conversation.tenant_id == tenant_id and conversation.id == conversation_id
            ),
            None,
        )

    def exists(self, tenant_id: TenantId, conversation_id: ConversationId) -> bool:
        return self.get_by_id(tenant_id, conversation_id) is not None


class FakeMessageRepository:
    def __init__(self) -> None:
        self.added: list[Message] = []

    def add(self, message: Message) -> None:
        self.added.append(message)


class FakeAssistantExecutionRepository:
    def __init__(self) -> None:
        self.added: list[AssistantExecution] = []

    def add(self, execution: AssistantExecution) -> None:
        self.added.append(execution)


class FakeIdempotencyRepository:
    def __init__(self) -> None:
        self.records: list[IdempotencyRecord] = []
        self.reserve_results: list[bool] = []

    def get(self, tenant_id: TenantId, scope: str, key: str) -> IdempotencyRecord | None:
        return next(
            (
                record
                for record in self.records
                if record.tenant_id == tenant_id.value
                and record.scope == scope
                and record.idempotency_key == key
            ),
            None,
        )

    def reserve(self, record: IdempotencyRecord) -> bool:
        reserved = (
            self.get(TenantId(record.tenant_id), record.scope, record.idempotency_key) is None
        )
        self.reserve_results.append(reserved)
        if not reserved:
            return False
        self.records.append(record)
        return True

    def complete(self, record: IdempotencyRecord, **values: object) -> None:
        record.status = "completed"
        record.response_status = int(values["response_status"])
        record.response_body = values["response_body"]  # type: ignore[assignment]
        record.completed_at = values["completed_at"]  # type: ignore[assignment]


class FakeConversationUnitOfWork:
    def __init__(self, conversations: list[Conversation]) -> None:
        self.conversation_repository = FakeConversationRepository(conversations)
        self.message_repository = FakeMessageRepository()
        self.execution_repository = FakeAssistantExecutionRepository()
        self.conversations: ConversationRepository = self.conversation_repository
        self.messages: MessageRepository = self.message_repository
        self.executions: AssistantExecutionRepository = self.execution_repository
        self.idempotency_repository = FakeIdempotencyRepository()
        self.idempotency: IdempotencyRepository = self.idempotency_repository
        self.commit_count = 0
        self.rollback_count = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        if exc_type is not None:
            self.rollback()

    def commit(self) -> None:
        self.commit_count += 1

    def rollback(self) -> None:
        self.rollback_count += 1


class FakeConversationUnitOfWorkFactory:
    def __init__(self, unit_of_work: FakeConversationUnitOfWork) -> None:
        self.unit_of_work = unit_of_work
        self.actors: list[Actor] = []

    def create(self, actor: Actor) -> ConversationUnitOfWork:
        self.actors.append(actor)
        return self.unit_of_work


NOW = datetime(2026, 9, 29, 10, 30, tzinfo=UTC)


def build_actor(*, tenant_id: TenantId | None = None) -> Actor:
    return Actor.user(tenant_id=tenant_id or TenantId(uuid4()), user_id=UserId(uuid4()))


def build_conversation(actor: Actor) -> Conversation:
    assert actor.user_id is not None
    return Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=actor.tenant_id,
        owner_user_id=actor.user_id,
        title="Support",
        language="en",
        now=datetime(2026, 9, 28, tzinfo=UTC),
    )


def build_handler(
    unit_of_work: FakeConversationUnitOfWork,
    *,
    message_id: MessageId | None = None,
    execution_id: ExecutionId | None = None,
) -> tuple[
    SendConversationMessageHandler,
    MessageId,
    ExecutionId,
    FakeConversationUnitOfWorkFactory,
]:
    expected_message_id = message_id or MessageId(uuid4())
    expected_execution_id = execution_id or ExecutionId(uuid4())
    factory = FakeConversationUnitOfWorkFactory(unit_of_work)
    handler = SendConversationMessageHandler(
        unit_of_work_factory=factory,
        message_id_factory=lambda: expected_message_id,
        execution_id_factory=lambda: expected_execution_id,
        clock=lambda: NOW,
        idempotency_id_factory=uuid4,
    )
    return handler, expected_message_id, expected_execution_id, factory


def test_accepts_message_and_creates_pending_execution_atomically() -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, message_id, execution_id, factory = build_handler(unit_of_work)

    result = handler.handle(
        SendConversationMessageCommand(
            actor=actor,
            conversation_id=conversation.id,
            content="How do I install it?",
            idempotency_key="request-key",
        )
    )

    assert factory.actors == [actor]
    assert unit_of_work.conversation_repository.lookups == [(actor.tenant_id, conversation.id)]
    assert unit_of_work.conversation_repository.saved == [conversation]
    assert conversation.updated_at == NOW
    assert conversation.last_message_at == NOW

    assert len(unit_of_work.message_repository.added) == 1
    user_message = unit_of_work.message_repository.added[0]
    assert user_message.id == message_id
    assert user_message.tenant_id == actor.tenant_id
    assert user_message.conversation_id == conversation.id
    assert user_message.author_id == actor.user_id
    assert user_message.content == "How do I install it?"
    assert user_message.created_at == NOW

    assert len(unit_of_work.execution_repository.added) == 1
    execution = unit_of_work.execution_repository.added[0]
    assert execution.id == execution_id
    assert execution.tenant_id == actor.tenant_id
    assert execution.conversation_id == conversation.id
    assert execution.user_message_id == user_message.id
    assert execution.status.value == "created"
    assert execution.capability.value == "direct_response"
    assert execution.assistant_message_id is None
    assert execution.created_at == NOW
    assert execution.updated_at == NOW

    assert unit_of_work.idempotency_repository.reserve_results == [True]
    assert unit_of_work.commit_count == 1
    assert result.user_message_id == message_id
    assert result.assistant_execution_id == execution_id
    assert result.execution_status == "created"
    assert result.capability == "direct_response"


def test_requires_user_actor_before_opening_unit_of_work() -> None:
    actor = Actor(
        actor_type=ActorType.SERVICE,
        tenant_id=TenantId(uuid4()),
        user_id=None,
    )
    unit_of_work = FakeConversationUnitOfWork([])
    handler, _, _, factory = build_handler(unit_of_work)

    with pytest.raises(ValueError, match="User actor is required"):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=ConversationId(uuid4()),
                content="hello",
                idempotency_key="request-key",
            )
        )

    assert factory.actors == []
    assert_no_writes_or_commit(unit_of_work)


@pytest.mark.parametrize("cross_tenant", [False, True])
def test_invisible_conversation_raises_same_not_found_error(cross_tenant: bool) -> None:
    actor = build_actor()
    conversation_actor = build_actor() if cross_tenant else actor
    conversation = build_conversation(conversation_actor)
    unit_of_work = FakeConversationUnitOfWork([conversation] if cross_tenant else [])
    handler, _, _, _ = build_handler(unit_of_work)

    with pytest.raises(ConversationNotFoundError):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=conversation.id,
                content="hello",
                idempotency_key="request-key",
            )
        )

    assert unit_of_work.conversation_repository.lookups == [(actor.tenant_id, conversation.id)]
    assert_no_writes_or_commit(unit_of_work)


@pytest.mark.parametrize("status", [ConversationStatus.ARCHIVED, ConversationStatus.LOCKED])
def test_inactive_conversation_uses_domain_rejection(status: ConversationStatus) -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    conversation.status = status
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, _, _, _ = build_handler(unit_of_work)

    with pytest.raises(ConversationNotActiveError):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=conversation.id,
                content="hello",
                idempotency_key="request-key",
            )
        )

    assert_no_writes_or_commit(unit_of_work)


def test_rejects_unsupported_capability_before_opening_unit_of_work() -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, _, _, factory = build_handler(unit_of_work)

    with pytest.raises(ValueError, match="Unsupported execution capability"):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=conversation.id,
                content="hello",
                idempotency_key="request-key",
                capability_hint="knowledge_query",
            )
        )

    assert factory.actors == []
    assert_no_writes_or_commit(unit_of_work)


def test_invalid_user_message_is_not_persisted_or_committed() -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, _, _, _ = build_handler(unit_of_work)

    with pytest.raises(InvalidMessageContentError):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=conversation.id,
                content="   ",
                idempotency_key="request-key",
            )
        )

    assert_no_writes_or_commit(unit_of_work)


def test_accepts_explicit_direct_response_and_uses_supplied_factories() -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    message_id = MessageId(uuid4())
    execution_id = ExecutionId(uuid4())
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, _, _, _ = build_handler(unit_of_work, message_id=message_id, execution_id=execution_id)

    result = handler.handle(
        SendConversationMessageCommand(
            actor=actor,
            conversation_id=conversation.id,
            content="hello",
            idempotency_key="request-key",
            capability_hint="direct_response",
        )
    )

    assert result.user_message_id is message_id
    assert result.assistant_execution_id is execution_id


def assert_no_writes_or_commit(unit_of_work: FakeConversationUnitOfWork) -> None:
    assert unit_of_work.conversation_repository.saved == []
    assert unit_of_work.message_repository.added == []
    assert unit_of_work.execution_repository.added == []
    assert unit_of_work.commit_count == 0


def test_replay_returns_stored_result_without_new_business_effects() -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, _, _, _ = build_handler(unit_of_work)
    command = SendConversationMessageCommand(
        actor=actor,
        conversation_id=conversation.id,
        content="  preserve me  ",
        idempotency_key="replay-key",
    )

    first = handler.handle(command)
    replayed = handler.handle(command)

    assert replayed == first
    assert len(unit_of_work.message_repository.added) == 1
    assert len(unit_of_work.execution_repository.added) == 1
    assert len(unit_of_work.conversation_repository.saved) == 1
    assert unit_of_work.idempotency_repository.reserve_results == [True, False]
    assert unit_of_work.commit_count == 1
    record = unit_of_work.idempotency_repository.records[0]
    assert record.status == "completed"
    assert record.response_body == {
        "assistant_execution_id": str(first.assistant_execution_id.value),
        "capability": "direct_response",
        "execution_status": "created",
        "user_message_id": str(first.user_message_id.value),
    }
    assert "preserve me" not in str(record.response_body)


@pytest.mark.parametrize(
    ("changed_conversation", "changed_content", "changed_capability"),
    [(False, True, False), (True, False, False), (False, False, True)],
)
def test_reused_key_with_different_logical_payload_conflicts(
    changed_conversation: bool, changed_content: bool, changed_capability: bool
) -> None:
    actor = build_actor()
    conversation = build_conversation(actor)
    other_conversation = build_conversation(actor)
    unit_of_work = FakeConversationUnitOfWork([conversation, other_conversation])
    handler, _, _, _ = build_handler(unit_of_work)
    original = SendConversationMessageCommand(
        actor=actor,
        conversation_id=conversation.id,
        content="hello",
        idempotency_key="one-key",
    )
    handler.handle(original)

    from geem_ai.conversations.application.exceptions import IdempotencyKeyConflictError
    from geem_ai.conversations.domain.enums import ExecutionCapability

    if changed_capability:
        handler._resolve_capability = lambda _: ExecutionCapability.KNOWLEDGE_QUERY  # type: ignore[method-assign]

    with pytest.raises(IdempotencyKeyConflictError):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=other_conversation.id if changed_conversation else conversation.id,
                content="changed" if changed_content else "hello",
                idempotency_key="one-key",
                capability_hint="knowledge_query" if changed_capability else None,
            )
        )
    assert unit_of_work.idempotency_repository.reserve_results == [True, False]
    assert len(unit_of_work.message_repository.added) == 1
    assert len(unit_of_work.execution_repository.added) == 1
    assert len(unit_of_work.conversation_repository.saved) == 1
    assert unit_of_work.commit_count == 1


def test_processing_identical_request_raises_in_progress() -> None:
    from geem_ai.conversations.application.exceptions import IdempotencyRequestInProgressError

    actor = build_actor()
    conversation = build_conversation(actor)
    unit_of_work = FakeConversationUnitOfWork([conversation])
    handler, _, _, _ = build_handler(unit_of_work)
    command = SendConversationMessageCommand(
        actor=actor, conversation_id=conversation.id, content="hello", idempotency_key="busy"
    )
    handler.handle(command)
    unit_of_work.idempotency_repository.records[0].status = "processing"

    with pytest.raises(IdempotencyRequestInProgressError):
        handler.handle(command)
    assert unit_of_work.idempotency_repository.reserve_results == [True, False]
    assert len(unit_of_work.message_repository.added) == 1
    assert len(unit_of_work.execution_repository.added) == 1
    assert len(unit_of_work.conversation_repository.saved) == 1
    assert unit_of_work.commit_count == 1


@pytest.mark.parametrize("key", ["", "   ", "x" * 256])
def test_invalid_idempotency_key_is_rejected_before_opening_uow(key: str) -> None:
    from geem_ai.conversations.application.exceptions import InvalidIdempotencyKeyError

    actor = build_actor()
    unit_of_work = FakeConversationUnitOfWork([])
    handler, _, _, factory = build_handler(unit_of_work)
    with pytest.raises(InvalidIdempotencyKeyError):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=ConversationId(uuid4()),
                content="hello",
                idempotency_key=key,
            )
        )
    assert factory.actors == []
    assert_no_writes_or_commit(unit_of_work)


def test_different_tenants_can_use_the_same_key_independently() -> None:
    first_actor = build_actor()
    second_actor = build_actor()
    first_conversation = build_conversation(first_actor)
    second_conversation = build_conversation(second_actor)
    unit_of_work = FakeConversationUnitOfWork([first_conversation, second_conversation])
    handler, _, _, _ = build_handler(unit_of_work)

    for actor, conversation in (
        (first_actor, first_conversation),
        (second_actor, second_conversation),
    ):
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=conversation.id,
                content="hello",
                idempotency_key="shared-key",
            )
        )

    assert len(unit_of_work.idempotency_repository.records) == 2
    assert {record.tenant_id for record in unit_of_work.idempotency_repository.records} == {
        first_actor.tenant_id.value,
        second_actor.tenant_id.value,
    }
    assert unit_of_work.commit_count == 2
