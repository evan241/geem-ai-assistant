from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from geem_ai.conversations.domain.assistant_execution import AssistantExecution

ASSISTANT_EXECUTION_REQUESTED = "assistant.execution.requested"


@dataclass(frozen=True, slots=True)
class OutboxEvent:
    id: UUID
    tenant_id: UUID | None
    event_type: str
    event_version: int
    aggregate_type: str
    aggregate_id: UUID
    correlation_id: str | None
    causation_id: str | None
    payload: dict[str, object]
    status: str
    attempt: int
    available_at: datetime
    created_at: datetime
    published_at: datetime | None
    last_error: str | None


def assistant_execution_requested(
    *,
    event_id: UUID,
    execution: AssistantExecution,
    now: datetime,
) -> OutboxEvent:
    return OutboxEvent(
        id=event_id,
        tenant_id=execution.tenant_id.value,
        event_type=ASSISTANT_EXECUTION_REQUESTED,
        event_version=1,
        aggregate_type="assistant_execution",
        aggregate_id=execution.id.value,
        correlation_id=None,
        causation_id=None,
        payload={
            "assistant_execution_id": str(execution.id.value),
            "conversation_id": str(execution.conversation_id.value),
            "user_message_id": str(execution.user_message_id.value),
            "capability": execution.capability.value,
        },
        status="pending",
        attempt=0,
        available_at=now,
        created_at=now,
        published_at=None,
        last_error=None,
    )
