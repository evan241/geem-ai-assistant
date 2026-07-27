from datetime import UTC, datetime
from uuid import uuid4

import pytest

from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import (
    ExecutionCapability,
    ExecutionStatus,
)
from geem_ai.conversations.domain.exceptions import (
    InvalidExecutionTransitionError,
    MissingExecutionFailureError,
    MissingExecutionResultError,
    NegativeExecutionMetricError,
)
from geem_ai.shared.domain.ids import (
    ConversationId,
    ExecutionId,
    MessageId,
    TenantId,
)


def build_execution() -> AssistantExecution:
    return AssistantExecution.create(
        execution_id=ExecutionId(uuid4()),
        tenant_id=TenantId(uuid4()),
        conversation_id=ConversationId(uuid4()),
        user_message_id=MessageId(uuid4()),
        capability=ExecutionCapability.DIRECT_RESPONSE,
    )


def test_execution_can_transition_from_created_to_running_to_completed() -> None:
    execution = build_execution()
    started_at = datetime.now(UTC)
    completed_at = datetime.now(UTC)

    execution.start(now=started_at)

    assert execution.status is ExecutionStatus.RUNNING
    assert execution.started_at == started_at

    assistant_message_id = MessageId(uuid4())

    execution.complete(
        assistant_message_id=assistant_message_id,
        provider="openai",
        model="test-model",
        input_tokens=10,
        output_tokens=5,
        total_tokens=15,
        cost_amount=0.001,
        latency_ms=250,
        now=completed_at,
    )

    assert execution.status is ExecutionStatus.COMPLETED
    assert execution.assistant_message_id == assistant_message_id
    assert execution.provider == "openai"
    assert execution.model == "test-model"
    assert execution.total_tokens == 15
    assert execution.cost_amount == 0.001
    assert execution.latency_ms == 250
    assert execution.completed_at == completed_at


def test_execution_cannot_complete_without_result() -> None:
    execution = build_execution()
    execution.start(now=datetime.now(UTC))

    with pytest.raises(MissingExecutionResultError):
        execution.complete(
            assistant_message_id=None,
            provider="openai",
            model="test-model",
            input_tokens=10,
            output_tokens=5,
            total_tokens=15,
            cost_amount=0.001,
            latency_ms=250,
            now=datetime.now(UTC),
        )


def test_failed_execution_requires_failure_information() -> None:
    execution = build_execution()
    execution.start(now=datetime.now(UTC))

    with pytest.raises(MissingExecutionFailureError):
        execution.fail(
            failure_code="",
            failure_detail=None,
            now=datetime.now(UTC),
        )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("input_tokens", -1),
        ("output_tokens", -1),
        ("total_tokens", -1),
        ("cost_amount", -0.01),
        ("latency_ms", -1),
    ],
)
def test_execution_rejects_negative_metrics(field: str, value: int | float) -> None:
    execution = build_execution()
    execution.start(now=datetime.now(UTC))

    kwargs = {
        "assistant_message_id": MessageId(uuid4()),
        "provider": "openai",
        "model": "test-model",
        "input_tokens": 10,
        "output_tokens": 5,
        "total_tokens": 15,
        "cost_amount": 0.001,
        "latency_ms": 250,
        "now": datetime.now(UTC),
    }
    kwargs[field] = value

    with pytest.raises(NegativeExecutionMetricError):
        execution.complete(**kwargs)


def test_completed_execution_cannot_start_again() -> None:
    execution = build_execution()
    execution.start(now=datetime.now(UTC))
    execution.complete(
        assistant_message_id=MessageId(uuid4()),
        provider="openai",
        model="test-model",
        input_tokens=10,
        output_tokens=5,
        total_tokens=15,
        cost_amount=0.001,
        latency_ms=250,
        now=datetime.now(UTC),
    )

    with pytest.raises(InvalidExecutionTransitionError):
        execution.start(now=datetime.now(UTC))


def test_running_execution_can_be_cancelled() -> None:
    execution = build_execution()
    now = datetime.now(UTC)

    execution.start(now=now)
    execution.cancel(now=now)

    assert execution.status is ExecutionStatus.CANCELLED
    assert execution.completed_at == now


def test_completed_execution_cannot_be_cancelled() -> None:
    execution = build_execution()
    now = datetime.now(UTC)

    execution.start(now=now)
    execution.complete(
        assistant_message_id=MessageId(uuid4()),
        provider="openai",
        model="test-model",
        input_tokens=10,
        output_tokens=5,
        total_tokens=15,
        cost_amount=0.001,
        latency_ms=250,
        now=now,
    )

    with pytest.raises(InvalidExecutionTransitionError):
        execution.cancel(now=now)
