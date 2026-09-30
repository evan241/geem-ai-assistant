import asyncio
from datetime import UTC, datetime, timedelta
from uuid import uuid4

import pytest
from sqlalchemy import Engine, delete, func, select
from sqlalchemy.orm import Session

from geem_ai.conversations.application.commands import FailAssistantExecutionCommand
from geem_ai.conversations.application.exceptions import AssistantExecutionNotFoundError
from geem_ai.conversations.application.execution_context import ModelExecutionRequestBuilder
from geem_ai.conversations.application.handlers import (
    ClaimAssistantExecutionHandler,
    CompleteAssistantExecutionHandler,
    FailAssistantExecutionHandler,
)
from geem_ai.conversations.application.orchestration import (
    AssistantExecutionJobHandler,
    AssistantExecutionOrchestrator,
)
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

CREATED = datetime(2026, 9, 30, 15, tzinfo=UTC)
FAILED = CREATED + timedelta(seconds=1)


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
        title="Failure",
        language="en",
        now=CREATED,
    )
    execution = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=actor.tenant_id,
        conversation_id=conversation.id,
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=CREATED,
    )
    execution.start(now=CREATED)
    with Session(engine) as session:
        SQLAlchemyConversationRepository(session).add(conversation)
        session.commit()
    with Session(engine) as session:
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


def test_failure_fields_are_persisted(engine: Engine) -> None:
    actor, execution = seed_running(engine)
    try:
        FailAssistantExecutionHandler(
            unit_of_work_factory=SQLAlchemyConversationUnitOfWorkFactory(engine),
            clock=lambda: FAILED,
        ).handle(
            FailAssistantExecutionCommand(
                actor, execution.id, "model_gateway_error", "Model execution failed."
            )
        )

        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
        assert stored is not None
        assert (stored.status, stored.failure_code, stored.failure_detail) == (
            "failed",
            "model_gateway_error",
            "Model execution failed.",
        )
        assert stored.completed_at == stored.updated_at == FAILED
    finally:
        cleanup(engine, execution)


def test_foreign_tenant_cannot_fail_execution(engine: Engine) -> None:
    _, execution = seed_running(engine)
    foreign = Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))
    try:
        with pytest.raises(AssistantExecutionNotFoundError):
            FailAssistantExecutionHandler(
                unit_of_work_factory=SQLAlchemyConversationUnitOfWorkFactory(engine),
                clock=lambda: FAILED,
            ).handle(
                FailAssistantExecutionCommand(foreign, execution.id, "model_gateway_error", None)
            )
        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
        assert stored is not None and stored.status == "running"
    finally:
        cleanup(engine, execution)


def test_failure_transaction_is_rolled_back_when_commit_fails(engine: Engine) -> None:
    actor, execution = seed_running(engine)

    class FailingFactory(SQLAlchemyConversationUnitOfWorkFactory):
        def create(self, actor: Actor):  # type: ignore[no-untyped-def]
            uow = super().create(actor)

            def fail_commit() -> None:
                uow.session.flush()
                raise RuntimeError("commit failed")

            uow.commit = fail_commit  # type: ignore[method-assign]
            return uow

    try:
        with pytest.raises(RuntimeError, match="commit failed"):
            FailAssistantExecutionHandler(
                unit_of_work_factory=FailingFactory(engine), clock=lambda: FAILED
            ).handle(
                FailAssistantExecutionCommand(actor, execution.id, "model_gateway_error", None)
            )
        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
        assert stored is not None
        assert stored.status == "running"
        assert stored.failure_code is None
        assert stored.completed_at is None
    finally:
        cleanup(engine, execution)


@pytest.mark.parametrize("terminal", ["cancelled", "completed"])
def test_terminal_execution_is_not_overwritten(engine: Engine, terminal: str) -> None:
    actor, execution = seed_running(engine)
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)
    try:
        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
            assert stored is not None
            stored.status = terminal
            stored.completed_at = FAILED
            stored.updated_at = FAILED
            session.commit()

        with pytest.raises(InvalidExecutionTransitionError):
            FailAssistantExecutionHandler(
                unit_of_work_factory=factory, clock=lambda: FAILED
            ).handle(
                FailAssistantExecutionCommand(actor, execution.id, "model_gateway_error", None)
            )
        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
        assert stored is not None and stored.status == terminal
    finally:
        cleanup(engine, execution)


def test_redelivering_completed_execution_does_not_call_gateway_or_change_result(
    engine: Engine,
) -> None:
    actor, execution = seed_running(engine)
    factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

    class Gateway:
        calls = 0

        async def execute(self, request: object) -> object:
            self.calls += 1
            raise AssertionError("duplicate delivery must not invoke the gateway")

    gateway = Gateway()
    try:
        assistant_message_id = MessageId(uuid4())
        assistant_message = Message.create_assistant(
            message_id=assistant_message_id,
            conversation_id=execution.conversation_id,
            tenant_id=actor.tenant_id,
            content="Stable answer",
            execution_id=execution.id,
            now=FAILED,
        )
        assistant_message.complete(now=FAILED)
        with Session(engine) as session:
            SQLAlchemyMessageRepository(session).add(assistant_message)
            session.commit()
        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
            assert stored is not None
            stored.status = "completed"
            stored.assistant_message_id = assistant_message_id.value
            stored.provider = "fake"
            stored.model = "stable-model"
            stored.input_tokens = 3
            stored.output_tokens = 4
            stored.total_tokens = 7
            stored.cost_amount = 0.25
            stored.latency_ms = 9
            stored.completed_at = FAILED
            stored.updated_at = FAILED
            session.commit()

        orchestrator = AssistantExecutionOrchestrator(
            unit_of_work_factory=factory,
            claim_handler=ClaimAssistantExecutionHandler(
                unit_of_work_factory=factory, clock=lambda: FAILED
            ),
            request_builder=ModelExecutionRequestBuilder(),
            model_gateway=gateway,  # type: ignore[arg-type]
            complete_handler=CompleteAssistantExecutionHandler(
                unit_of_work_factory=factory, clock=lambda: FAILED
            ),
            fail_handler=FailAssistantExecutionHandler(
                unit_of_work_factory=factory, clock=lambda: FAILED
            ),
            message_id_factory=lambda: MessageId(uuid4()),
        )
        asyncio.run(
            AssistantExecutionJobHandler(orchestrator).handle(
                actor=actor, execution_id=execution.id
            )
        )

        with Session(engine) as session:
            stored = session.get(AssistantExecutionModel, execution.id.value)
            message_count = session.scalar(
                select(func.count())
                .select_from(MessageModel)
                .where(MessageModel.execution_id == execution.id.value)
            )
        assert gateway.calls == 0
        assert stored is not None
        assert stored.assistant_message_id == assistant_message_id.value
        assert (stored.input_tokens, stored.output_tokens, stored.total_tokens) == (3, 4, 7)
        assert stored.model == "stable-model"
        assert message_count == 1
    finally:
        cleanup(engine, execution)
