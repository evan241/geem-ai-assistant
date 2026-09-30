from datetime import UTC, datetime
from typing import Self
from uuid import uuid4

import pytest

from geem_ai.ai_runtime.public import ModelExecutionResult, ModelUsage
from geem_ai.conversations.application.commands import CompleteAssistantExecutionCommand
from geem_ai.conversations.application.exceptions import AssistantExecutionNotFoundError
from geem_ai.conversations.application.handlers import CompleteAssistantExecutionHandler
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import ExecutionCapability, MessageRole, MessageStatus
from geem_ai.conversations.domain.exceptions import InvalidExecutionTransitionError
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId

CREATED = datetime(2026, 9, 30, 10, tzinfo=UTC)
COMPLETED = datetime(2026, 9, 30, 10, 1, tzinfo=UTC)


class ExecutionRepository:
    def __init__(self, execution: AssistantExecution | None) -> None:
        self.execution = execution
        self.lookups: list[tuple[TenantId, ExecutionId]] = []
        self.saved: list[AssistantExecution] = []

    def get_for_update(self, tenant_id: TenantId, execution_id: ExecutionId):  # type: ignore[no-untyped-def]
        self.lookups.append((tenant_id, execution_id))
        if self.execution is None or self.execution.tenant_id != tenant_id:
            return None
        return self.execution if self.execution.id == execution_id else None

    def save(self, execution: AssistantExecution) -> None:
        self.saved.append(execution)


class MessageRepository:
    def __init__(self) -> None:
        self.added = []  # type: ignore[var-annotated]

    def add(self, message):  # type: ignore[no-untyped-def]
        self.added.append(message)


class UnitOfWork:
    def __init__(self, execution: AssistantExecution | None) -> None:
        self.executions = ExecutionRepository(execution)
        self.messages = MessageRepository()
        self.commits = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def commit(self) -> None:
        self.commits += 1


class Factory:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    def create(self, actor: Actor):  # type: ignore[no-untyped-def]
        return self.uow


def make_actor() -> Actor:
    return Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))


def make_running(actor: Actor) -> AssistantExecution:
    execution = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=actor.tenant_id,
        conversation_id=ConversationId(uuid4()),
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=CREATED,
    )
    execution.start(now=CREATED)
    return execution


def result() -> ModelExecutionResult:
    return ModelExecutionResult(
        content="Exact final answer",
        provider="fake",
        model="fake-model",
        usage=ModelUsage(input_tokens=11, output_tokens=7, total_tokens=18),
        finish_reason="stop",
        latency_ms=123,
        estimated_cost=0.0042,
    )


def test_completion_atomically_maps_result_and_uses_one_timestamp() -> None:
    actor = make_actor()
    execution = make_running(actor)
    uow = UnitOfWork(execution)
    message_id = MessageId(uuid4())
    clock_calls = 0

    def clock() -> datetime:
        nonlocal clock_calls
        clock_calls += 1
        return COMPLETED

    CompleteAssistantExecutionHandler(
        unit_of_work_factory=Factory(uow),  # type: ignore[arg-type]
        clock=clock,
    ).handle(CompleteAssistantExecutionCommand(actor, execution.id, result(), message_id))

    assert uow.executions.lookups == [(actor.tenant_id, execution.id)]
    assert len(uow.messages.added) == 1
    message = uow.messages.added[0]
    assert (message.id, message.content, message.role, message.status) == (
        message_id,
        "Exact final answer",
        MessageRole.ASSISTANT,
        MessageStatus.COMPLETED,
    )
    assert message.execution_id == execution.id
    assert message.created_at == message.completed_at == COMPLETED
    assert execution.assistant_message_id == message_id
    assert (execution.provider, execution.model) == ("fake", "fake-model")
    assert (execution.input_tokens, execution.output_tokens, execution.total_tokens) == (11, 7, 18)
    assert (execution.cost_amount, execution.latency_ms) == (0.0042, 123)
    assert execution.completed_at == execution.updated_at == COMPLETED
    assert uow.executions.saved == [execution]
    assert uow.commits == 1
    assert clock_calls == 1


def test_missing_execution_does_not_write_or_commit() -> None:
    actor = make_actor()
    uow = UnitOfWork(None)
    execution_id = ExecutionId(uuid4())

    with pytest.raises(AssistantExecutionNotFoundError):
        CompleteAssistantExecutionHandler(
            unit_of_work_factory=Factory(uow),
            clock=lambda: COMPLETED,  # type: ignore[arg-type]
        ).handle(
            CompleteAssistantExecutionCommand(actor, execution_id, result(), MessageId(uuid4()))
        )

    assert uow.executions.lookups == [(actor.tenant_id, execution_id)]
    assert uow.messages.added == []
    assert uow.executions.saved == []
    assert uow.commits == 0


def test_non_running_execution_rejects_before_message_is_persisted() -> None:
    actor = make_actor()
    execution = make_running(actor)
    execution.cancel(now=COMPLETED)
    uow = UnitOfWork(execution)

    with pytest.raises(InvalidExecutionTransitionError):
        CompleteAssistantExecutionHandler(
            unit_of_work_factory=Factory(uow),
            clock=lambda: COMPLETED,  # type: ignore[arg-type]
        ).handle(
            CompleteAssistantExecutionCommand(actor, execution.id, result(), MessageId(uuid4()))
        )

    assert uow.messages.added == []
    assert uow.executions.saved == []
    assert uow.commits == 0
