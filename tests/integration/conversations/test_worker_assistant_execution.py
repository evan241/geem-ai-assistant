import asyncio
from datetime import UTC, datetime
from uuid import uuid4

import pytest
from apps.worker.assistant_execution import (
    AssistantExecutionRequestedEventHandler,
    build_assistant_execution_job_handler,
)
from sqlalchemy import Engine, delete, func, select
from sqlalchemy.orm import Session

from geem_ai.ai_runtime.infrastructure.fake_model_gateway import FakeModelGateway
from geem_ai.ai_runtime.public import ModelExecutionResult, ModelUsage
from geem_ai.conversations.application.events import assistant_execution_requested
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ExecutionCapability
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
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import create_database_engine

CREATED = datetime(2026, 9, 30, 12, tzinfo=UTC)


@pytest.fixture
def engine() -> Engine:
    value = create_database_engine(get_settings().database_url)
    yield value
    value.dispose()


def test_delivered_event_executes_once_across_worker_seam(engine: Engine) -> None:
    actor = Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))
    conversation = Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=actor.tenant_id,
        owner_user_id=actor.user_id,
        title="Worker slice",
        language="en",
        now=CREATED,  # type: ignore[arg-type]
    )
    user_message = Message.create_user(
        message_id=MessageId(uuid4()),
        conversation_id=conversation.id,
        tenant_id=actor.tenant_id,
        author_id=actor.user_id,
        content="Answer through the worker seam",
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
    event = assistant_execution_requested(event_id=uuid4(), execution=execution, now=CREATED)
    gateway = FakeModelGateway(
        ModelExecutionResult(
            content="Worker answer",
            provider="fake",
            model="fake-model",
            usage=ModelUsage(4, 2, 6),
            finish_reason="stop",
            latency_ms=8,
            estimated_cost=0.001,
        )
    )

    with Session(engine) as session:
        SQLAlchemyConversationRepository(session).add(conversation)
        session.commit()
    with Session(engine) as session:
        SQLAlchemyMessageRepository(session).add(user_message)
        SQLAlchemyAssistantExecutionRepository(session).add(execution)
        session.commit()

    try:
        adapter = AssistantExecutionRequestedEventHandler(
            job_handler=build_assistant_execution_job_handler(
                engine=engine,
                model_gateway=gateway,
            )
        )
        asyncio.run(adapter.handle(event))
        asyncio.run(adapter.handle(event))

        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
            assistant_messages = session.scalar(
                select(func.count())
                .select_from(MessageModel)
                .where(MessageModel.execution_id == execution.id.value)
            )
        assert stored is not None
        assert stored.status == "completed"
        assert stored.assistant_message_id is not None
        assert assistant_messages == 1
        assert len(gateway.requests) == 1
    finally:
        with Session(engine) as session:
            session.execute(
                delete(MessageModel).where(
                    MessageModel.conversation_id == execution.conversation_id.value
                )
            )
            session.execute(
                delete(AssistantExecutionModel).where(
                    AssistantExecutionModel.id == execution.id.value
                )
            )
            session.execute(
                delete(ConversationModel).where(
                    ConversationModel.id == execution.conversation_id.value
                )
            )
            session.commit()
