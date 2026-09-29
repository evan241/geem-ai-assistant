from datetime import UTC, datetime
from typing import Self
from uuid import uuid4

import pytest

from geem_ai.conversations.application.commands import ClaimAssistantExecutionCommand
from geem_ai.conversations.application.exceptions import AssistantExecutionNotFoundError
from geem_ai.conversations.application.handlers import ClaimAssistantExecutionHandler
from geem_ai.conversations.application.ports.repositories import AssistantExecutionRepository
from geem_ai.conversations.application.ports.unit_of_work import ConversationUnitOfWork
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.conversations.domain.exceptions import InvalidExecutionTransitionError
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId

CREATED_AT = datetime(2026, 9, 29, 10, tzinfo=UTC)
CLAIMED_AT = datetime(2026, 9, 29, 10, 5, tzinfo=UTC)


class FakeExecutionRepository:
    def __init__(self, execution: AssistantExecution | None) -> None:
        self.execution = execution
        self.lookups: list[tuple[TenantId, ExecutionId]] = []
        self.saved: list[AssistantExecution] = []

    def add(self, execution: AssistantExecution) -> None:
        raise AssertionError("add should not be called")

    def get_for_update(
        self, tenant_id: TenantId, execution_id: ExecutionId
    ) -> AssistantExecution | None:
        self.lookups.append((tenant_id, execution_id))
        if self.execution is None or self.execution.tenant_id != tenant_id:
            return None
        return self.execution if self.execution.id == execution_id else None

    def save(self, execution: AssistantExecution) -> None:
        self.saved.append(execution)


class FakeUnitOfWork:
    def __init__(self, execution: AssistantExecution | None) -> None:
        self.execution_repository = FakeExecutionRepository(execution)
        self.executions: AssistantExecutionRepository = self.execution_repository
        self.commit_count = 0

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        return None

    def commit(self) -> None:
        self.commit_count += 1

    def rollback(self) -> None:
        return None


class FakeFactory:
    def __init__(self, unit_of_work: FakeUnitOfWork) -> None:
        self.unit_of_work = unit_of_work
        self.actors: list[Actor] = []

    def create(self, actor: Actor) -> ConversationUnitOfWork:
        self.actors.append(actor)
        return self.unit_of_work  # type: ignore[return-value]


def make_actor(*, tenant_id: TenantId | None = None) -> Actor:
    return Actor.user(tenant_id=tenant_id or TenantId(uuid4()), user_id=UserId(uuid4()))


def make_execution(actor: Actor) -> AssistantExecution:
    return AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=actor.tenant_id,
        conversation_id=ConversationId(uuid4()),
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=CREATED_AT,
    )


def test_created_execution_is_claimed_with_single_clock_save_and_commit() -> None:
    actor = make_actor()
    execution = make_execution(actor)
    unit_of_work = FakeUnitOfWork(execution)
    factory = FakeFactory(unit_of_work)
    clock_calls = 0

    def clock() -> datetime:
        nonlocal clock_calls
        clock_calls += 1
        return CLAIMED_AT

    result = ClaimAssistantExecutionHandler(unit_of_work_factory=factory, clock=clock).handle(
        ClaimAssistantExecutionCommand(actor=actor, execution_id=execution.id)
    )

    assert result.execution is execution
    assert execution.status.value == "running"
    assert execution.started_at == CLAIMED_AT
    assert execution.updated_at == CLAIMED_AT
    assert clock_calls == 1
    assert unit_of_work.execution_repository.saved == [execution]
    assert unit_of_work.commit_count == 1
    assert factory.actors == [actor]
    assert unit_of_work.execution_repository.lookups == [(actor.tenant_id, execution.id)]


def test_missing_execution_raises_and_does_not_save_or_commit() -> None:
    actor = make_actor()
    execution_id = ExecutionId(uuid4())
    unit_of_work = FakeUnitOfWork(None)

    with pytest.raises(AssistantExecutionNotFoundError):
        ClaimAssistantExecutionHandler(
            unit_of_work_factory=FakeFactory(unit_of_work), clock=lambda: CLAIMED_AT
        ).handle(ClaimAssistantExecutionCommand(actor=actor, execution_id=execution_id))

    assert unit_of_work.execution_repository.saved == []
    assert unit_of_work.commit_count == 0


def test_other_tenant_execution_behaves_as_not_found() -> None:
    owner = make_actor()
    actor = make_actor()
    unit_of_work = FakeUnitOfWork(make_execution(owner))

    with pytest.raises(AssistantExecutionNotFoundError):
        ClaimAssistantExecutionHandler(
            unit_of_work_factory=FakeFactory(unit_of_work), clock=lambda: CLAIMED_AT
        ).handle(
            ClaimAssistantExecutionCommand(
                actor=actor,
                execution_id=unit_of_work.execution_repository.execution.id,  # type: ignore[union-attr]
            )
        )

    assert unit_of_work.commit_count == 0


def test_already_running_execution_uses_domain_transition_and_does_not_commit() -> None:
    actor = make_actor()
    execution = make_execution(actor)
    execution.start(now=CLAIMED_AT)
    unit_of_work = FakeUnitOfWork(execution)

    with pytest.raises(InvalidExecutionTransitionError):
        ClaimAssistantExecutionHandler(
            unit_of_work_factory=FakeFactory(unit_of_work), clock=lambda: CLAIMED_AT
        ).handle(ClaimAssistantExecutionCommand(actor=actor, execution_id=execution.id))

    assert unit_of_work.execution_repository.saved == []
    assert unit_of_work.commit_count == 0
