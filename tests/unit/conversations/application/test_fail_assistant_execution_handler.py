from datetime import UTC, datetime
from typing import Self
from uuid import uuid4

import pytest

from geem_ai.conversations.application.commands import FailAssistantExecutionCommand
from geem_ai.conversations.application.exceptions import AssistantExecutionNotFoundError
from geem_ai.conversations.application.handlers import FailAssistantExecutionHandler
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import ExecutionCapability, ExecutionStatus
from geem_ai.conversations.domain.exceptions import InvalidExecutionTransitionError
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId

CREATED = datetime(2026, 9, 30, 10, tzinfo=UTC)
FAILED = datetime(2026, 9, 30, 10, 1, tzinfo=UTC)


class Repository:
    def __init__(self, execution: AssistantExecution | None) -> None:
        self.execution = execution
        self.lookups: list[tuple[TenantId, ExecutionId]] = []
        self.saved: list[AssistantExecution] = []

    def get_for_update(
        self, tenant_id: TenantId, execution_id: ExecutionId
    ) -> AssistantExecution | None:
        self.lookups.append((tenant_id, execution_id))
        if self.execution is None:
            return None
        if (tenant_id, execution_id) != (self.execution.tenant_id, self.execution.id):
            return None
        return self.execution

    def save(self, execution: AssistantExecution) -> None:
        self.saved.append(execution)


class Uow:
    def __init__(self, execution: AssistantExecution | None) -> None:
        self.executions = Repository(execution)
        self.commits = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def commit(self) -> None:
        self.commits += 1


class Factory:
    def __init__(self, uow: Uow) -> None:
        self.uow = uow

    def create(self, actor: Actor) -> Uow:
        return self.uow


def actor() -> Actor:
    return Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))


def execution(owner: Actor) -> AssistantExecution:
    value = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=owner.tenant_id,
        conversation_id=ConversationId(uuid4()),
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=CREATED,
    )
    value.start(now=CREATED)
    return value


def test_running_execution_is_failed_with_one_clock_save_and_commit() -> None:
    owner = actor()
    value = execution(owner)
    uow = Uow(value)
    calls = 0

    def clock() -> datetime:
        nonlocal calls
        calls += 1
        return FAILED

    FailAssistantExecutionHandler(unit_of_work_factory=Factory(uow), clock=clock).handle(
        FailAssistantExecutionCommand(
            owner, value.id, "model_gateway_error", "Model execution failed."
        )
    )

    assert value.status.value == "failed"
    assert value.failure_code == "model_gateway_error"
    assert value.failure_detail == "Model execution failed."
    assert value.completed_at == value.updated_at == FAILED
    assert calls == 1
    assert uow.executions.saved == [value]
    assert uow.commits == 1
    assert uow.executions.lookups == [(owner.tenant_id, value.id)]


@pytest.mark.parametrize("foreign", [False, True])
def test_missing_or_foreign_execution_does_not_commit(foreign: bool) -> None:
    owner = actor()
    value = execution(owner)
    uow = Uow(value if foreign else None)
    requester = actor() if foreign else owner

    with pytest.raises(AssistantExecutionNotFoundError):
        FailAssistantExecutionHandler(
            unit_of_work_factory=Factory(uow), clock=lambda: FAILED
        ).handle(
            FailAssistantExecutionCommand(requester, value.id, "execution_context_error", None)
        )
    assert uow.executions.saved == []
    assert uow.commits == 0


@pytest.mark.parametrize(
    "state", ["completed", "cancelled", "failed", "timed_out", "waiting_for_approval"]
)
def test_terminal_execution_cannot_be_failed_or_persisted(state: str) -> None:
    owner = actor()
    value = execution(owner)
    if state == "completed":
        value.complete(
            assistant_message_id=MessageId(uuid4()),
            provider="p",
            model="m",
            input_tokens=1,
            output_tokens=1,
            total_tokens=2,
            cost_amount=0.0,
            latency_ms=1,
            now=FAILED,
        )
    elif state == "cancelled":
        value.cancel(now=FAILED)
    else:
        if state == "failed":
            value.fail(failure_code="old", failure_detail=None, now=FAILED)
        else:
            value.status = ExecutionStatus(state)
    uow = Uow(value)

    with pytest.raises(InvalidExecutionTransitionError):
        FailAssistantExecutionHandler(
            unit_of_work_factory=Factory(uow), clock=lambda: FAILED
        ).handle(FailAssistantExecutionCommand(owner, value.id, "model_gateway_error", None))
    assert uow.executions.saved == []
    assert uow.commits == 0
