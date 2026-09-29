from concurrent.futures import ThreadPoolExecutor, TimeoutError
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from decimal import Decimal
from threading import Event
from uuid import uuid4

import pytest
from sqlalchemy import Engine, delete
from sqlalchemy.orm import Session

from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import ExecutionCapability, ExecutionStatus
from geem_ai.conversations.domain.exceptions import InvalidExecutionTransitionError
from geem_ai.conversations.infrastructure.persistence.models import (
    AssistantExecutionModel,
    ConversationModel,
)
from geem_ai.conversations.infrastructure.persistence.repositories import (
    SQLAlchemyAssistantExecutionRepository,
    SQLAlchemyConversationRepository,
)
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import create_database_engine

CREATED_AT = datetime(2026, 9, 29, 10, tzinfo=UTC)
STARTED_AT = CREATED_AT + timedelta(minutes=1)


@pytest.fixture
def engine() -> Engine:
    database_engine = create_database_engine(get_settings().database_url)
    yield database_engine
    database_engine.dispose()


def seed_execution(engine: Engine) -> AssistantExecution:
    tenant_id = TenantId(uuid4())
    conversation_id = ConversationId(uuid4())
    execution = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=tenant_id,
        conversation_id=conversation_id,
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.KNOWLEDGE_QUERY,
        now=CREATED_AT,
    )
    conversation = Conversation.create(
        conversation_id=conversation_id,
        tenant_id=tenant_id,
        owner_user_id=UserId(uuid4()),
        title="Claim persistence",
        language="en",
        now=CREATED_AT,
    )
    with Session(engine) as session:
        SQLAlchemyConversationRepository(session).add(conversation)
        SQLAlchemyAssistantExecutionRepository(session).add(execution)
        session.commit()
    return execution


def remove_execution(engine: Engine, execution: AssistantExecution) -> None:
    with Session(engine) as session:
        session.execute(
            delete(AssistantExecutionModel).where(AssistantExecutionModel.id == execution.id.value)
        )
        session.execute(
            delete(ConversationModel).where(ConversationModel.id == execution.conversation_id.value)
        )
        session.commit()


def test_get_for_update_is_tenant_scoped_and_reconstructs_all_fields(engine: Engine) -> None:
    execution = seed_execution(engine)
    assistant_message_id = MessageId(uuid4())
    try:
        with Session(engine) as session:
            model = session.get(AssistantExecutionModel, execution.id.value)
            assert model is not None
            model.assistant_message_id = assistant_message_id.value
            model.status = "failed"
            model.provider = "provider"
            model.model = "model"
            model.input_tokens = 10
            model.output_tokens = 20
            model.total_tokens = 30
            model.cost_amount = Decimal("1.25000000")
            model.latency_ms = 400
            model.failure_code = "provider_error"
            model.failure_detail = "detail"
            model.started_at = STARTED_AT
            model.completed_at = STARTED_AT + timedelta(seconds=1)
            model.updated_at = STARTED_AT + timedelta(seconds=1)
            session.commit()

        with Session(engine) as session:
            repository = SQLAlchemyAssistantExecutionRepository(session)
            loaded = repository.get_for_update(execution.tenant_id, execution.id)
            hidden = repository.get_for_update(TenantId(uuid4()), execution.id)

        assert loaded is not None
        assert loaded.id == execution.id
        assert loaded.tenant_id == execution.tenant_id
        assert loaded.conversation_id == execution.conversation_id
        assert loaded.user_message_id == execution.user_message_id
        assert loaded.assistant_message_id == assistant_message_id
        assert loaded.status is ExecutionStatus.FAILED
        assert loaded.capability is ExecutionCapability.KNOWLEDGE_QUERY
        assert loaded.provider == "provider"
        assert loaded.model == "model"
        assert (loaded.input_tokens, loaded.output_tokens, loaded.total_tokens) == (10, 20, 30)
        assert loaded.cost_amount == 1.25
        assert loaded.latency_ms == 400
        assert loaded.failure_code == "provider_error"
        assert loaded.failure_detail == "detail"
        assert loaded.started_at == STARTED_AT
        assert loaded.completed_at == STARTED_AT + timedelta(seconds=1)
        assert loaded.created_at == CREATED_AT
        assert loaded.updated_at == STARTED_AT + timedelta(seconds=1)
        assert hidden is None
    finally:
        remove_execution(engine, execution)


def test_save_persists_claim_is_tenant_scoped_and_rollback_is_atomic(engine: Engine) -> None:
    execution = seed_execution(engine)
    try:
        with Session(engine) as session:
            repository = SQLAlchemyAssistantExecutionRepository(session)
            loaded = repository.get_for_update(execution.tenant_id, execution.id)
            assert loaded is not None
            loaded.start(now=STARTED_AT)
            repository.save(loaded)
            session.commit()

        with Session(engine) as session:
            model = session.get(AssistantExecutionModel, execution.id.value)
            assert model is not None
            assert model.status == "running"
            assert model.started_at == STARTED_AT
            assert model.updated_at == STARTED_AT

        foreign = replace(execution, tenant_id=TenantId(uuid4()))
        foreign.status = ExecutionStatus.COMPLETED
        with Session(engine) as session:
            SQLAlchemyAssistantExecutionRepository(session).save(foreign)
            session.commit()
        with Session(engine) as session:
            model = session.get(AssistantExecutionModel, execution.id.value)
            assert model is not None and model.status == "running"

        with Session(engine) as session:
            repository = SQLAlchemyAssistantExecutionRepository(session)
            loaded = repository.get_for_update(execution.tenant_id, execution.id)
            assert loaded is not None
            loaded.updated_at = STARTED_AT + timedelta(minutes=1)
            repository.save(loaded)
            session.rollback()
        with Session(engine) as session:
            model = session.get(AssistantExecutionModel, execution.id.value)
            assert model is not None and model.updated_at == STARTED_AT
    finally:
        remove_execution(engine, execution)


def test_row_lock_prevents_two_workers_from_claiming_created_execution(engine: Engine) -> None:
    execution = seed_execution(engine)
    first_locked = Event()
    release_first = Event()
    second_started = Event()

    def first_worker() -> None:
        with Session(engine) as session:
            repository = SQLAlchemyAssistantExecutionRepository(session)
            loaded = repository.get_for_update(execution.tenant_id, execution.id)
            assert loaded is not None
            loaded.start(now=STARTED_AT)
            repository.save(loaded)
            first_locked.set()
            assert release_first.wait(timeout=5)
            session.commit()

    def second_worker() -> None:
        assert first_locked.wait(timeout=5)
        with Session(engine) as session:
            second_started.set()
            repository = SQLAlchemyAssistantExecutionRepository(session)
            loaded = repository.get_for_update(execution.tenant_id, execution.id)
            assert loaded is not None
            loaded.start(now=STARTED_AT + timedelta(seconds=1))

    try:
        with ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(first_worker)
            assert first_locked.wait(timeout=5)
            second = pool.submit(second_worker)
            assert second_started.wait(timeout=5)
            with pytest.raises(TimeoutError):
                second.result(timeout=0.2)
            release_first.set()
            first.result(timeout=5)
            with pytest.raises(InvalidExecutionTransitionError):
                second.result(timeout=5)
    finally:
        release_first.set()
        remove_execution(engine, execution)
