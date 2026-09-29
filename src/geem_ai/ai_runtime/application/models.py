from __future__ import annotations

from dataclasses import dataclass

from geem_ai.shared.domain.ids import ExecutionId, TenantId


@dataclass(frozen=True, slots=True)
class ModelMessage:
    role: str
    content: str


@dataclass(frozen=True, slots=True)
class ModelUsage:
    input_tokens: int
    output_tokens: int
    total_tokens: int


@dataclass(frozen=True, slots=True)
class ModelExecutionRequest:
    tenant_id: TenantId
    execution_id: ExecutionId
    capability: str
    messages: tuple[ModelMessage, ...]
    prompt_reference: str | None


@dataclass(frozen=True, slots=True)
class ModelExecutionResult:
    content: str
    provider: str
    model: str
    usage: ModelUsage
    finish_reason: str
    latency_ms: int
    estimated_cost: float
