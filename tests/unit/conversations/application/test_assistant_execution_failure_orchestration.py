import asyncio
from datetime import UTC, datetime
from types import SimpleNamespace
from typing import Self
from uuid import uuid4

import pytest

from geem_ai.ai_runtime.public import ModelExecutionRequest, ModelExecutionResult, ModelUsage
from geem_ai.conversations.application.exceptions import (
    AssistantExecutionNotClaimableError,
    ExecutionUserMessageNotFoundError,
    UnsupportedExecutionCapabilityError,
)
from geem_ai.conversations.application.orchestration import (
    AssistantExecutionJobHandler,
    AssistantExecutionOrchestrator,
)
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.conversations.domain.exceptions import InvalidExecutionTransitionError
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId, UserId

NOW = datetime(2026, 9, 30, tzinfo=UTC)


def fixtures() -> tuple[Actor, AssistantExecution, Message]:
    actor = Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4()))
    execution = AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=actor.tenant_id,
        conversation_id=ConversationId(uuid4()),
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
        now=NOW,
    )
    message = Message.create_user(
        message_id=execution.user_message_id,
        conversation_id=execution.conversation_id,
        tenant_id=actor.tenant_id,
        author_id=actor.user_id,
        content="Question",
        now=NOW,
    )
    return actor, execution, message


class Messages:
    def __init__(self, message: Message | None) -> None:
        self.message = message

    def list_recent_for_execution(self, *args: object, **kwargs: object) -> tuple[Message, ...]:
        return () if self.message is None else (self.message,)

    def get_for_execution(self, *args: object) -> Message | None:
        return self.message


class ContextUow:
    def __init__(self, message: Message | None, active: list[bool]) -> None:
        self.messages = Messages(message)
        self.active = active

    def __enter__(self) -> Self:
        self.active[0] = True
        return self

    def __exit__(self, *args: object) -> None:
        self.active[0] = False


class Factory:
    def __init__(self, message: Message | None, active: list[bool]) -> None:
        self.uow = ContextUow(message, active)

    def create(self, actor: Actor) -> ContextUow:
        return self.uow


class Claim:
    def __init__(self, execution: AssistantExecution, error: Exception | None = None) -> None:
        self.execution = execution
        self.error = error

    def handle(self, command: object) -> object:
        if self.error:
            raise self.error
        return SimpleNamespace(execution=self.execution)


class Builder:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error

    def build(self, execution: AssistantExecution, context: object) -> ModelExecutionRequest:
        if self.error:
            raise self.error
        return ModelExecutionRequest(execution.tenant_id, execution.id, "direct_response", (), None)


class Gateway:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error
        self.calls = 0

    async def execute(self, request: ModelExecutionRequest) -> ModelExecutionResult:
        self.calls += 1
        if self.error:
            raise self.error
        return ModelExecutionResult("ok", "fake", "model", ModelUsage(1, 1, 2), "stop", 1, 0.0)


class Complete:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error
        self.calls = 0

    def handle(self, command: object) -> None:
        self.calls += 1
        if self.error:
            raise self.error


class Fail:
    def __init__(self, active: list[bool]) -> None:
        self.active = active
        self.commands = []  # type: ignore[var-annotated]

    def handle(self, command: object) -> None:
        assert not self.active[0]
        self.commands.append(command)


def orchestrator(
    *, claim_error=None, message=True, builder_error=None, gateway_error=None, complete_error=None
):  # type: ignore[no-untyped-def]
    actor, execution, user_message = fixtures()
    active = [False]
    fail = Fail(active)
    gateway = Gateway(gateway_error)
    value = AssistantExecutionOrchestrator(
        unit_of_work_factory=Factory(user_message if message else None, active),  # type: ignore[arg-type]
        claim_handler=Claim(execution, claim_error),  # type: ignore[arg-type]
        request_builder=Builder(builder_error),  # type: ignore[arg-type]
        model_gateway=gateway,
        complete_handler=Complete(complete_error),  # type: ignore[arg-type]
        fail_handler=fail,  # type: ignore[arg-type]
        message_id_factory=lambda: MessageId(uuid4()),
    )
    return value, actor, execution, fail, gateway


@pytest.mark.parametrize(
    ("kwargs", "error_type", "code", "detail"),
    [
        (
            {"message": False},
            ExecutionUserMessageNotFoundError,
            "execution_context_error",
            "Execution context could not be prepared.",
        ),
        (
            {"builder_error": UnsupportedExecutionCapabilityError()},
            UnsupportedExecutionCapabilityError,
            "unsupported_execution_capability",
            "Execution capability is not supported.",
        ),
        (
            {"gateway_error": RuntimeError("secret provider body API_KEY")},
            RuntimeError,
            "model_gateway_error",
            "Model execution failed.",
        ),
    ],
)
def test_preparation_and_gateway_failures_are_safely_persisted_and_reraised(
    kwargs, error_type, code, detail
):  # type: ignore[no-untyped-def]
    value, actor, execution, fail, _ = orchestrator(**kwargs)
    with pytest.raises(error_type):
        asyncio.run(value.execute(actor=actor, execution_id=execution.id))
    assert len(fail.commands) == 1
    assert fail.commands[0].failure_code == code
    assert fail.commands[0].safe_detail == detail
    assert "secret" not in fail.commands[0].safe_detail


def test_only_claim_transition_is_converted_to_not_claimable() -> None:
    value, actor, execution, fail, _ = orchestrator(claim_error=InvalidExecutionTransitionError())
    with pytest.raises(AssistantExecutionNotClaimableError):
        asyncio.run(value.execute(actor=actor, execution_id=execution.id))
    assert fail.commands == []

    value, actor, execution, fail, _ = orchestrator(
        complete_error=InvalidExecutionTransitionError()
    )
    with pytest.raises(InvalidExecutionTransitionError):
        asyncio.run(value.execute(actor=actor, execution_id=execution.id))
    assert fail.commands == []


def test_job_handler_swallows_only_duplicate_claims() -> None:
    class Orchestrator:
        def __init__(self, error: Exception | None) -> None:
            self.error = error
            self.calls = 0

        async def execute(self, **kwargs: object) -> None:
            self.calls += 1
            if self.error:
                raise self.error

    actor, execution, _ = fixtures()
    duplicate = Orchestrator(AssistantExecutionNotClaimableError())
    asyncio.run(
        AssistantExecutionJobHandler(duplicate).handle(actor=actor, execution_id=execution.id)
    )  # type: ignore[arg-type]
    assert duplicate.calls == 1

    ordinary = Orchestrator(RuntimeError("boom"))
    with pytest.raises(RuntimeError, match="boom"):
        asyncio.run(
            AssistantExecutionJobHandler(ordinary).handle(actor=actor, execution_id=execution.id)
        )  # type: ignore[arg-type]

    success = Orchestrator(None)
    asyncio.run(
        AssistantExecutionJobHandler(success).handle(actor=actor, execution_id=execution.id)
    )  # type: ignore[arg-type]
    assert success.calls == 1
