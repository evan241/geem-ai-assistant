from datetime import UTC, datetime, timedelta
from uuid import uuid4

import pytest
from sqlalchemy import Engine, delete, select
from sqlalchemy.orm import Session

from geem_ai.ai_runtime.public import ModelExecutionResult, ModelUsage
from geem_ai.conversations.application.commands import CompleteAssistantExecutionCommand
from geem_ai.conversations.application.exceptions import AssistantExecutionNotFoundError
from geem_ai.conversations.application.handlers import CompleteAssistantExecutionHandler
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.conversations.domain.exceptions import InvalidExecutionTransitionError
from geem_ai.conversations.domain.message import Message
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

CREATED = datetime(2026, 9, 30, 12, tzinfo=UTC)
COMPLETED = CREATED + timedelta(seconds=2)


@pytest.fixture
def engine() -> Engine:
    value = create_database_engine(get_settings().database_url)
    yield value
    value.dispose()


def seed_running(engine: Engine) -> tuple[Actor, AssistantExecution]:
    actor = Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))
    conversation = Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=actor.tenant_id,
        owner_user_id=actor.user_id,
        title="Completion",
        language="en",
        now=CREATED,  # type: ignore[arg-type]
    )
    user_message = Message.create_user(
        message_id=MessageId(uuid4()),
        conversation_id=conversation.id,
        tenant_id=actor.tenant_id,
        author_id=actor.user_id,
        content="Hello",
        now=CREATED,  # type: ignore[arg-type]
    )
    execution = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=actor.tenant_id,
        conversation_id=conversation.id,
        user_message_id=user_message.id,
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=CREATED,
    )
    execution.start(now=CREATED)
    with Session(engine) as session:
        SQLAlchemyConversationRepository(session).add(conversation)
        session.commit()
    with Session(engine) as session:
        SQLAlchemyMessageRepository(session).add(user_message)
        SQLAlchemyAssistantExecutionRepository(session).add(execution)
        session.commit()
    return actor, execution


def cleanup(engine: Engine, execution: AssistantExecution) -> None:
    with Session(engine) as session:
        session.execute(
            delete(MessageModel).where(
                MessageModel.conversation_id == execution.conversation_id.value
            )
        )
        session.execute(
            delete(AssistantExecutionModel).where(AssistantExecutionModel.id == execution.id.value)
        )
        session.execute(
            delete(ConversationModel).where(ConversationModel.id == execution.conversation_id.value)
        )
        session.commit()


def model_result() -> ModelExecutionResult:
    return ModelExecutionResult(
        content="Persisted answer",
        provider="fake",
        model="fake-model",
        usage=ModelUsage(13, 8, 21),
        finish_reason="stop",
        latency_ms=55,
        estimated_cost=0.0025,
    )


def test_success_persists_message_and_execution_atomically(engine: Engine) -> None:
    actor, execution = seed_running(engine)
    message_id = MessageId(uuid4())
    try:
        CompleteAssistantExecutionHandler(
            unit_of_work_factory=SQLAlchemyConversationUnitOfWorkFactory(engine),
            clock=lambda: COMPLETED,
        ).handle(CompleteAssistantExecutionCommand(actor, execution.id, model_result(), message_id))

        with Session(engine) as session:
            message = session.scalar(
                select(MessageModel).where(MessageModel.id == message_id.value)
            )
            stored = session.get(AssistantExecutionModel, execution.id.value)
        assert message is not None and stored is not None
        assert (message.tenant_id, message.conversation_id, message.execution_id) == (
            actor.tenant_id.value,
            execution.conversation_id.value,
            execution.id.value,
        )
        assert (message.role, message.status, message.content) == (
            "assistant",
            "completed",
            "Persisted answer",
        )
        assert message.created_at == message.completed_at == COMPLETED
        assert (stored.status, stored.assistant_message_id) == ("completed", message_id.value)
        assert (stored.provider, stored.model) == ("fake", "fake-model")
        assert (stored.input_tokens, stored.output_tokens, stored.total_tokens) == (13, 8, 21)
        assert float(stored.cost_amount) == 0.0025  # type: ignore[arg-type]
        assert stored.latency_ms == 55
        assert stored.completed_at == stored.updated_at == COMPLETED
    finally:
        cleanup(engine, execution)


def test_foreign_tenant_and_cancelled_execution_cannot_complete(engine: Engine) -> None:
    actor, execution = seed_running(engine)
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)
    try:
        foreign_actor = Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))
        with pytest.raises(AssistantExecutionNotFoundError):
            CompleteAssistantExecutionHandler(
                unit_of_work_factory=factory, clock=lambda: COMPLETED
            ).handle(
                CompleteAssistantExecutionCommand(
                    foreign_actor, execution.id, model_result(), MessageId(uuid4())
                )
            )

        with factory.create(actor) as uow:
            current = uow.executions.get_for_update(actor.tenant_id, execution.id)
            assert current is not None
            current.cancel(now=COMPLETED)
            uow.executions.save(current)
            uow.commit()
        rejected_message_id = MessageId(uuid4())
        with pytest.raises(InvalidExecutionTransitionError):
            CompleteAssistantExecutionHandler(
                unit_of_work_factory=factory, clock=lambda: COMPLETED
            ).handle(
                CompleteAssistantExecutionCommand(
                    actor, execution.id, model_result(), rejected_message_id
                )
            )

        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
            message = session.get(MessageModel, rejected_message_id.value)
        assert stored is not None and stored.status == "cancelled"
        assert stored.assistant_message_id is None
        assert message is None
    finally:
        cleanup(engine, execution)
