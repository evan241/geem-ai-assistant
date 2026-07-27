from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

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


@dataclass(slots=True)
class AssistantExecution:
    id: ExecutionId
    tenant_id: TenantId
    conversation_id: ConversationId
    user_message_id: MessageId
    assistant_message_id: MessageId | None
    status: ExecutionStatus
    capability: ExecutionCapability

    provider: str | None = None
    model: str | None = None

    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None

    cost_amount: float | None = None
    latency_ms: int | None = None

    failure_code: str | None = None
    failure_detail: str | None = None

    started_at: datetime | None = None
    completed_at: datetime | None = None

    @classmethod
    def create(
        cls,
        *,
        execution_id: ExecutionId,
        tenant_id: TenantId,
        conversation_id: ConversationId,
        user_message_id: MessageId,
        capability: ExecutionCapability,
    ) -> AssistantExecution:
        return cls(
            id=execution_id,
            tenant_id=tenant_id,
            conversation_id=conversation_id,
            user_message_id=user_message_id,
            assistant_message_id=None,
            status=ExecutionStatus.CREATED,
            capability=capability,
        )

    def start(self, *, now: datetime) -> None:
        self._require_status(ExecutionStatus.CREATED)

        self.status = ExecutionStatus.RUNNING
        self.started_at = now

    def complete(
        self,
        *,
        assistant_message_id: MessageId | None,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        total_tokens: int,
        cost_amount: float,
        latency_ms: int,
        now: datetime,
    ) -> None:
        self._require_status(ExecutionStatus.RUNNING)

        if assistant_message_id is None:
            raise MissingExecutionResultError(
                "Completed execution must reference an assistant message."
            )

        self._validate_non_negative_metrics(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            cost_amount=cost_amount,
            latency_ms=latency_ms,
        )

        self.assistant_message_id = assistant_message_id
        self.provider = provider
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens
        self.cost_amount = cost_amount
        self.latency_ms = latency_ms
        self.completed_at = now
        self.status = ExecutionStatus.COMPLETED

    def fail(
        self,
        *,
        failure_code: str,
        failure_detail: str | None,
        now: datetime,
    ) -> None:
        self._require_status(ExecutionStatus.RUNNING)

        if not failure_code.strip():
            raise MissingExecutionFailureError("Failed execution must include a failure code.")

        self.failure_code = failure_code
        self.failure_detail = failure_detail
        self.completed_at = now
        self.status = ExecutionStatus.FAILED

    def _require_status(self, expected: ExecutionStatus) -> None:
        if self.status is not expected:
            raise InvalidExecutionTransitionError(
                f"Execution cannot transition from {self.status!s}; expected {expected!s}."
            )

    @staticmethod
    def _validate_non_negative_metrics(
        *,
        input_tokens: int,
        output_tokens: int,
        total_tokens: int,
        cost_amount: float,
        latency_ms: int,
    ) -> None:
        metrics = {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "cost_amount": cost_amount,
            "latency_ms": latency_ms,
        }

        for name, value in metrics.items():
            if value < 0:
                raise NegativeExecutionMetricError(f"{name} cannot be negative.")

    def cancel(self, *, now: datetime) -> None:
        if self.status not in {
            ExecutionStatus.CREATED,
            ExecutionStatus.RUNNING,
        }:
            raise InvalidExecutionTransitionError(
                f"Execution cannot be cancelled from {self.status!s}."
            )

        self.status = ExecutionStatus.CANCELLED
        self.completed_at = now
