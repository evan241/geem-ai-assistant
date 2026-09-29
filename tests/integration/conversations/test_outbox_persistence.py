from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy import Engine, delete, inspect
from sqlalchemy.orm import Session

from geem_ai.conversations.application.commands import SendConversationMessageCommand
from geem_ai.conversations.application.events import OutboxEvent
from geem_ai.conversations.application.handlers import SendConversationMessageHandler
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.infrastructure.persistence.models import (
    AssistantExecutionModel,
    ConversationModel,
    IdempotencyRecordModel,
    MessageModel,
    OutboxEventModel,
)
from geem_ai.conversations.infrastructure.persistence.repositories import SQLAlchemyOutboxRepository
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWork,
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import create_database_engine

TENANT_ID = TenantId(UUID("a0000000-0000-0000-0000-000000000001"))
USER_ID = UserId(UUID("a0000000-0000-0000-0000-000000000002"))
CONVERSATION_ID = ConversationId(UUID("a0000000-0000-0000-0000-000000000003"))
MESSAGE_ID = MessageId(UUID("a0000000-0000-0000-0000-000000000004"))
EXECUTION_ID = ExecutionId(UUID("a0000000-0000-0000-0000-000000000005"))
EVENT_ID = UUID("a0000000-0000-0000-0000-000000000006")
IDEMPOTENCY_ID = UUID("a0000000-0000-0000-0000-000000000007")
NOW = datetime(2026, 9, 29, 12, tzinfo=UTC)


def event() -> OutboxEvent:
    return OutboxEvent(
        id=EVENT_ID,
        tenant_id=TENANT_ID.value,
        event_type="assistant.execution.requested",
        event_version=1,
        aggregate_type="assistant_execution",
        aggregate_id=EXECUTION_ID.value,
        correlation_id=None,
        causation_id=None,
        payload={"safe": "payload"},
        status="pending",
        attempt=0,
        available_at=NOW,
        created_at=NOW,
        published_at=None,
        last_error=None,
    )


def clean(engine: Engine) -> None:
    with Session(engine) as session:
        session.execute(delete(OutboxEventModel).where(OutboxEventModel.id == EVENT_ID))
        session.execute(
            delete(AssistantExecutionModel).where(AssistantExecutionModel.id == EXECUTION_ID.value)
        )
        session.execute(delete(MessageModel).where(MessageModel.id == MESSAGE_ID.value))
        session.execute(
            delete(IdempotencyRecordModel).where(IdempotencyRecordModel.id == IDEMPOTENCY_ID)
        )
        session.execute(
            delete(ConversationModel).where(ConversationModel.id == CONVERSATION_ID.value)
        )
        session.commit()


def test_outbox_repository_maps_pending_event_and_partial_index() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean(engine)
    try:
        with Session(engine) as session:
            SQLAlchemyOutboxRepository(session).add(event())
            session.commit()

        with Session(engine) as session:
            model = session.get(OutboxEventModel, EVENT_ID)
            assert model is not None
            assert model.tenant_id == TENANT_ID.value
            assert model.event_type == "assistant.execution.requested"
            assert model.event_version == 1
            assert model.aggregate_type == "assistant_execution"
            assert model.aggregate_id == EXECUTION_ID.value
            assert model.payload == {"safe": "payload"}
            assert model.status == "pending"
            assert model.attempt == 0
            assert model.available_at == NOW
            assert model.created_at == NOW

        indexes = inspect(engine).get_indexes("outbox_events")
        index = next(
            item for item in indexes if item["name"] == "ix_outbox_events__pending_available"
        )
        assert index["column_names"] == ["available_at", "created_at"]
        assert "pending" in str(index["dialect_options"]["postgresql_where"])
        assert "failed" in str(index["dialect_options"]["postgresql_where"])
    finally:
        clean(engine)
        engine.dispose()


def test_outbox_repository_participates_in_session_rollback() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean(engine)
    try:
        with Session(engine) as session:
            SQLAlchemyOutboxRepository(session).add(event())
            session.rollback()
        with Session(engine) as session:
            assert session.get(OutboxEventModel, EVENT_ID) is None
    finally:
        clean(engine)
        engine.dispose()


def test_handler_commits_all_acceptance_effects_atomically() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean(engine)
    actor = Actor.user(tenant_id=TENANT_ID, user_id=USER_ID)
    conversation = Conversation.create(
        conversation_id=CONVERSATION_ID,
        tenant_id=TENANT_ID,
        owner_user_id=USER_ID,
        title="Atomic acceptance",
        language="en",
        now=NOW,
    )
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)
    try:
        with factory.create(actor) as uow:
            uow.conversations.add(conversation)
            uow.commit()

        handler = SendConversationMessageHandler(
            unit_of_work_factory=factory,
            message_id_factory=lambda: MESSAGE_ID,
            execution_id_factory=lambda: EXECUTION_ID,
            idempotency_id_factory=lambda: IDEMPOTENCY_ID,
            outbox_event_id_factory=lambda: EVENT_ID,
            clock=lambda: NOW,
        )
        handler.handle(
            SendConversationMessageCommand(
                actor=actor,
                conversation_id=CONVERSATION_ID,
                content="Commit everything",
                idempotency_key="atomic-event",
            )
        )

        with Session(engine) as session:
            persisted_conversation = session.get(ConversationModel, CONVERSATION_ID.value)
            assert persisted_conversation is not None
            assert persisted_conversation.last_message_at == NOW
            assert session.get(MessageModel, MESSAGE_ID.value) is not None
            assert session.get(AssistantExecutionModel, EXECUTION_ID.value) is not None
            idempotency = session.get(IdempotencyRecordModel, IDEMPOTENCY_ID)
            assert idempotency is not None
            assert idempotency.status == "completed"
            assert session.get(OutboxEventModel, EVENT_ID) is not None
    finally:
        clean(engine)
        engine.dispose()


def test_handler_failure_before_commit_rolls_back_every_acceptance_effect() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean(engine)
    actor = Actor.user(tenant_id=TENANT_ID, user_id=USER_ID)
    conversation = Conversation.create(
        conversation_id=CONVERSATION_ID,
        tenant_id=TENANT_ID,
        owner_user_id=USER_ID,
        title="Atomic rollback",
        language="en",
        now=NOW,
    )
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

    class FailingCommitFactory:
        def create(self, requested_actor: Actor) -> SQLAlchemyConversationUnitOfWork:
            uow = factory.create(requested_actor)

            def fail_before_commit() -> None:
                raise RuntimeError("injected pre-commit failure")

            uow.commit = fail_before_commit  # type: ignore[method-assign]
            return uow

    try:
        with factory.create(actor) as uow:
            uow.conversations.add(conversation)
            uow.commit()

        handler = SendConversationMessageHandler(
            unit_of_work_factory=FailingCommitFactory(),
            message_id_factory=lambda: MESSAGE_ID,
            execution_id_factory=lambda: EXECUTION_ID,
            idempotency_id_factory=lambda: IDEMPOTENCY_ID,
            outbox_event_id_factory=lambda: EVENT_ID,
            clock=lambda: NOW,
        )
        try:
            handler.handle(
                SendConversationMessageCommand(
                    actor=actor,
                    conversation_id=CONVERSATION_ID,
                    content="Roll back everything",
                    idempotency_key="atomic-failure",
                )
            )
        except RuntimeError as error:
            assert str(error) == "injected pre-commit failure"
        else:
            raise AssertionError("Expected injected commit failure")

        with Session(engine) as session:
            persisted_conversation = session.get(ConversationModel, CONVERSATION_ID.value)
            assert persisted_conversation is not None
            assert persisted_conversation.last_message_at is None
            assert session.get(MessageModel, MESSAGE_ID.value) is None
            assert session.get(AssistantExecutionModel, EXECUTION_ID.value) is None
            assert session.get(IdempotencyRecordModel, IDEMPOTENCY_ID) is None
            assert session.get(OutboxEventModel, EVENT_ID) is None
    finally:
        clean(engine)
        engine.dispose()
