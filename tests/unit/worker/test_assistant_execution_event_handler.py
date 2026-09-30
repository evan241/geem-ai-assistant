import asyncio
from dataclasses import replace
from datetime import UTC, datetime
from uuid import uuid4

import pytest
from apps.worker.assistant_execution import (
    AssistantExecutionRequestedEventHandler,
    InvalidWorkerEventPayloadError,
    UnsupportedWorkerEventError,
    build_assistant_execution_job_handler,
)

from geem_ai.ai_runtime.infrastructure.fake_model_gateway import FakeModelGateway
from geem_ai.ai_runtime.public import ModelExecutionResult, ModelUsage
from geem_ai.conversations.application.events import OutboxEvent
from geem_ai.conversations.application.orchestration import AssistantExecutionJobHandler
from geem_ai.shared.domain.actor import ActorType
from geem_ai.shared.domain.ids import ExecutionId, TenantId


class RecordingJobHandler:
    def __init__(self, error: Exception | None = None) -> None:
        self.calls: list[tuple[object, object]] = []
        self.error = error

    async def handle(self, *, actor, execution_id) -> None:  # type: ignore[no-untyped-def]
        self.calls.append((actor, execution_id))
        if self.error is not None:
            raise self.error


def event() -> OutboxEvent:
    execution_id = uuid4()
    now = datetime(2026, 9, 30, tzinfo=UTC)
    return OutboxEvent(
        id=uuid4(),
        tenant_id=uuid4(),
        event_type="assistant.execution.requested",
        event_version=1,
        aggregate_type="assistant_execution",
        aggregate_id=execution_id,
        correlation_id=None,
        causation_id=None,
        payload={"assistant_execution_id": str(execution_id)},
        status="pending",
        attempt=0,
        available_at=now,
        created_at=now,
        published_at=None,
        last_error=None,
    )


def test_valid_event_dispatches_once_with_tenant_scoped_worker_actor() -> None:
    delivered = event()
    job = RecordingJobHandler()

    asyncio.run(AssistantExecutionRequestedEventHandler(job_handler=job).handle(delivered))

    assert len(job.calls) == 1
    actor, execution_id = job.calls[0]
    assert actor.actor_type is ActorType.WORKER  # type: ignore[union-attr]
    assert actor.tenant_id == TenantId(delivered.tenant_id)  # type: ignore[union-attr,arg-type]
    assert actor.user_id is None  # type: ignore[union-attr]
    assert execution_id == ExecutionId(delivered.aggregate_id)


@pytest.mark.parametrize(
    ("change", "error"),
    [
        ({"event_type": "other"}, UnsupportedWorkerEventError),
        ({"event_version": 2}, UnsupportedWorkerEventError),
        ({"tenant_id": None}, InvalidWorkerEventPayloadError),
        ({"aggregate_type": "conversation"}, InvalidWorkerEventPayloadError),
        ({"payload": {}}, InvalidWorkerEventPayloadError),
        ({"payload": {"assistant_execution_id": "not-a-uuid"}}, InvalidWorkerEventPayloadError),
        (
            {"payload": {"assistant_execution_id": str(uuid4())}},
            InvalidWorkerEventPayloadError,
        ),
        ({"payload": {"assistant_execution_id": 42}}, InvalidWorkerEventPayloadError),
    ],
)
def test_invalid_event_is_rejected_without_dispatch(
    change: dict[str, object], error: type[Exception]
) -> None:
    job = RecordingJobHandler()
    invalid = replace(event(), **change)

    with pytest.raises(error):
        asyncio.run(AssistantExecutionRequestedEventHandler(job_handler=job).handle(invalid))

    assert job.calls == []


def test_job_handler_exception_propagates() -> None:
    expected = RuntimeError("job failed")
    job = RecordingJobHandler(expected)

    with pytest.raises(RuntimeError, match="job failed") as caught:
        asyncio.run(AssistantExecutionRequestedEventHandler(job_handler=job).handle(event()))

    assert caught.value is expected
    assert len(job.calls) == 1


def test_no_op_job_handler_completes_normally() -> None:
    class NoOpJobHandler:
        async def handle(self, *, actor, execution_id) -> None:  # type: ignore[no-untyped-def]
            return None

    asyncio.run(
        AssistantExecutionRequestedEventHandler(job_handler=NoOpJobHandler()).handle(event())
    )


def test_composition_builds_job_with_supplied_gateway() -> None:
    gateway = FakeModelGateway(
        ModelExecutionResult(
            content="answer",
            provider="fake",
            model="fake-model",
            usage=ModelUsage(1, 1, 2),
            finish_reason="stop",
            latency_ms=1,
            estimated_cost=0.0,
        )
    )

    job = build_assistant_execution_job_handler(engine=object(), model_gateway=gateway)  # type: ignore[arg-type]

    assert isinstance(job, AssistantExecutionJobHandler)
    assert job._orchestrator._model_gateway is gateway  # type: ignore[attr-defined]
