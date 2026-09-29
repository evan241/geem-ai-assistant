from datetime import UTC, datetime, timedelta
from uuid import UUID

from sqlalchemy import Engine, delete, select
from sqlalchemy.orm import Session

from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.conversations.infrastructure.persistence.models import (
    AssistantExecutionModel,
    ConversationModel,
    MessageModel,
)
from geem_ai.conversations.infrastructure.persistence.repositories import (
    SQLAlchemyAssistantExecutionRepository,
    SQLAlchemyConversationRepository,
    SQLAlchemyMessageRepository,
)
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import create_database_engine

TENANT_ID = TenantId(UUID("10000000-0000-0000-0000-000000000001"))
OTHER_TENANT_ID = TenantId(UUID("10000000-0000-0000-0000-000000000002"))
USER_ID = UserId(UUID("20000000-0000-0000-0000-000000000001"))
CONVERSATION_ID = ConversationId(UUID("30000000-0000-0000-0000-000000000001"))
MESSAGE_ID = MessageId(UUID("40000000-0000-0000-0000-000000000001"))
EXECUTION_ID = ExecutionId(UUID("50000000-0000-0000-0000-000000000001"))
CREATED_AT = datetime(2026, 9, 29, 10, 0, tzinfo=UTC)
MESSAGE_AT = CREATED_AT + timedelta(minutes=5)


def build_conversation(*, tenant_id: TenantId = TENANT_ID) -> Conversation:
    return Conversation.create(
        conversation_id=CONVERSATION_ID,
        tenant_id=tenant_id,
        owner_user_id=USER_ID,
        title="Persistence foundation",
        language="en",
        now=CREATED_AT,
    )


def clean_persisted_rows(engine: Engine) -> None:
    with Session(engine) as session:
        session.execute(
            delete(MessageModel).where(MessageModel.conversation_id == CONVERSATION_ID.value)
        )
        session.execute(
            delete(AssistantExecutionModel).where(
                AssistantExecutionModel.conversation_id == CONVERSATION_ID.value
            )
        )
        session.execute(
            delete(ConversationModel).where(ConversationModel.id == CONVERSATION_ID.value)
        )
        session.commit()


def test_message_repository_persists_user_message() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean_persisted_rows(engine)
    conversation = build_conversation()
    message = conversation.add_user_message(
        message_id=MESSAGE_ID,
        content="Deterministic user message",
        author_id=USER_ID,
        now=MESSAGE_AT,
    )

    try:
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).add(conversation)
            SQLAlchemyMessageRepository(session).add(message)
            session.commit()

        with Session(engine) as session:
            model = session.get(MessageModel, MESSAGE_ID.value)

            assert model is not None
            assert model.tenant_id == TENANT_ID.value
            assert model.conversation_id == CONVERSATION_ID.value
            assert model.author_type == "user"
            assert model.author_id == USER_ID.value
            assert model.role == "user"
            assert model.content == "Deterministic user message"
            assert model.status == "completed"
            assert model.execution_id is None
            assert model.metadata_json == {}
            assert model.created_at == MESSAGE_AT
            assert model.completed_at == MESSAGE_AT
    finally:
        clean_persisted_rows(engine)
        engine.dispose()


def test_execution_repository_persists_created_execution() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean_persisted_rows(engine)
    conversation = build_conversation()
    execution = AssistantExecution.create(
        execution_id=EXECUTION_ID,
        tenant_id=TENANT_ID,
        conversation_id=CONVERSATION_ID,
        user_message_id=MESSAGE_ID,
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=MESSAGE_AT,
    )

    try:
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).add(conversation)
            SQLAlchemyAssistantExecutionRepository(session).add(execution)
            session.commit()

        with Session(engine) as session:
            model = session.get(AssistantExecutionModel, EXECUTION_ID.value)

            assert model is not None
            assert model.tenant_id == TENANT_ID.value
            assert model.conversation_id == CONVERSATION_ID.value
            assert model.user_message_id == MESSAGE_ID.value
            assert model.assistant_message_id is None
            assert model.status == "created"
            assert model.capability == "direct_response"
            assert model.provider is None
            assert model.model is None
            assert model.input_tokens is None
            assert model.output_tokens is None
            assert model.total_tokens is None
            assert model.cost_amount is None
            assert model.latency_ms is None
            assert model.failure_code is None
            assert model.failure_detail is None
            assert model.started_at is None
            assert model.completed_at is None
            assert model.created_at == MESSAGE_AT
            assert model.updated_at == MESSAGE_AT
    finally:
        clean_persisted_rows(engine)
        engine.dispose()


def test_conversation_repository_save_persists_message_timestamps() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean_persisted_rows(engine)
    conversation = build_conversation()

    try:
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).add(conversation)
            session.commit()

        conversation.add_user_message(
            message_id=MESSAGE_ID,
            content="Update timestamps",
            author_id=USER_ID,
            now=MESSAGE_AT,
        )
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).save(conversation)
            session.commit()

        with Session(engine) as session:
            model = session.get(ConversationModel, CONVERSATION_ID.value)
            assert model is not None
            assert model.updated_at == MESSAGE_AT
            assert model.last_message_at == MESSAGE_AT
    finally:
        clean_persisted_rows(engine)
        engine.dispose()


def test_conversation_repository_save_cannot_update_another_tenant() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean_persisted_rows(engine)
    stored = build_conversation(tenant_id=TENANT_ID)

    try:
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).add(stored)
            session.commit()

        foreign = build_conversation(tenant_id=OTHER_TENANT_ID)
        foreign.updated_at = MESSAGE_AT
        foreign.last_message_at = MESSAGE_AT
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).save(foreign)
            session.commit()

        with Session(engine) as session:
            model = session.get(ConversationModel, CONVERSATION_ID.value)
            assert model is not None
            assert model.tenant_id == TENANT_ID.value
            assert model.updated_at == CREATED_AT
            assert model.last_message_at is None
    finally:
        clean_persisted_rows(engine)
        engine.dispose()


def test_unit_of_work_commits_all_acceptance_writes_atomically() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean_persisted_rows(engine)
    actor = Actor.user(tenant_id=TENANT_ID, user_id=USER_ID)
    conversation = build_conversation()
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

    try:
        with factory.create(actor) as uow:
            uow.conversations.add(conversation)
            uow.commit()

        with factory.create(actor) as uow:
            loaded = uow.conversations.get_by_id(TENANT_ID, CONVERSATION_ID)
            assert loaded is not None
            message = loaded.add_user_message(
                message_id=MESSAGE_ID,
                content="Atomic commit",
                author_id=USER_ID,
                now=MESSAGE_AT,
            )
            execution = AssistantExecution.create(
                execution_id=EXECUTION_ID,
                tenant_id=TENANT_ID,
                conversation_id=CONVERSATION_ID,
                user_message_id=MESSAGE_ID,
                capability=ExecutionCapability.DIRECT_RESPONSE,
                now=MESSAGE_AT,
            )
            uow.conversations.save(loaded)
            uow.messages.add(message)
            uow.executions.add(execution)
            uow.commit()

        with Session(engine) as session:
            persisted_conversation = session.get(ConversationModel, CONVERSATION_ID.value)
            assert persisted_conversation is not None
            assert persisted_conversation.last_message_at == MESSAGE_AT
            assert session.get(MessageModel, MESSAGE_ID.value) is not None
            assert session.get(AssistantExecutionModel, EXECUTION_ID.value) is not None
    finally:
        clean_persisted_rows(engine)
        engine.dispose()


def test_unit_of_work_rolls_back_all_acceptance_writes() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean_persisted_rows(engine)
    actor = Actor.user(tenant_id=TENANT_ID, user_id=USER_ID)
    conversation = build_conversation()
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

    try:
        with factory.create(actor) as uow:
            uow.conversations.add(conversation)
            uow.commit()

        with factory.create(actor) as uow:
            loaded = uow.conversations.get_by_id(TENANT_ID, CONVERSATION_ID)
            assert loaded is not None
            message = loaded.add_user_message(
                message_id=MESSAGE_ID,
                content="Atomic rollback",
                author_id=USER_ID,
                now=MESSAGE_AT,
            )
            execution = AssistantExecution.create(
                execution_id=EXECUTION_ID,
                tenant_id=TENANT_ID,
                conversation_id=CONVERSATION_ID,
                user_message_id=MESSAGE_ID,
                capability=ExecutionCapability.DIRECT_RESPONSE,
                now=MESSAGE_AT,
            )
            uow.conversations.save(loaded)
            uow.messages.add(message)
            uow.executions.add(execution)

        with Session(engine) as session:
            persisted_conversation = session.get(ConversationModel, CONVERSATION_ID.value)
            assert persisted_conversation is not None
            assert persisted_conversation.last_message_at is None
            assert (
                session.scalar(select(MessageModel).where(MessageModel.id == MESSAGE_ID.value))
                is None
            )
            assert (
                session.scalar(
                    select(AssistantExecutionModel).where(
                        AssistantExecutionModel.id == EXECUTION_ID.value
                    )
                )
                is None
            )
    finally:
        clean_persisted_rows(engine)
        engine.dispose()
