import asyncio
from uuid import UUID

from geem_ai.ai_runtime.infrastructure.fake_model_gateway import FakeModelGateway
from geem_ai.ai_runtime.public import (
    ModelExecutionRequest,
    ModelExecutionResult,
    ModelGateway,
    ModelMessage,
    ModelUsage,
)
from geem_ai.shared.domain.ids import ExecutionId, TenantId


def _request(*, capability: str = "conversation.reply") -> ModelExecutionRequest:
    return ModelExecutionRequest(
        tenant_id=TenantId(UUID("00000000-0000-0000-0000-000000000001")),
        execution_id=ExecutionId(UUID("00000000-0000-0000-0000-000000000002")),
        capability=capability,
        messages=(
            ModelMessage(role="system", content="Answer concisely."),
            ModelMessage(role="user", content="What is the status?"),
        ),
        prompt_reference="assistant-response:v1",
    )


def _result() -> ModelExecutionResult:
    usage = ModelUsage(input_tokens=12, output_tokens=4, total_tokens=16)
    return ModelExecutionResult(
        content="Everything is operational.",
        provider="fake-provider",
        model="fake-model-v1",
        usage=usage,
        finish_reason="stop",
        latency_ms=25,
        estimated_cost=0.0012,
    )


def test_model_execution_request_preserves_conversation_input() -> None:
    request = _request()

    assert request.tenant_id == TenantId(UUID("00000000-0000-0000-0000-000000000001"))
    assert request.execution_id == ExecutionId(UUID("00000000-0000-0000-0000-000000000002"))
    assert request.capability == "conversation.reply"
    assert request.messages == (
        ModelMessage(role="system", content="Answer concisely."),
        ModelMessage(role="user", content="What is the status?"),
    )
    assert request.prompt_reference == "assistant-response:v1"


def test_model_usage_preserves_token_metrics() -> None:
    usage = ModelUsage(input_tokens=12, output_tokens=4, total_tokens=16)

    assert usage.input_tokens == 12
    assert usage.output_tokens == 4
    assert usage.total_tokens == 16


def test_model_execution_result_preserves_response_metadata() -> None:
    result = _result()

    assert result.content == "Everything is operational."
    assert result.provider == "fake-provider"
    assert result.model == "fake-model-v1"
    assert result.usage == ModelUsage(input_tokens=12, output_tokens=4, total_tokens=16)
    assert result.finish_reason == "stop"
    assert result.latency_ms == 25
    assert result.estimated_cost == 0.0012


def test_fake_model_gateway_returns_result_and_captures_exact_request() -> None:
    result = _result()
    gateway = FakeModelGateway(result)
    request = _request()

    actual = asyncio.run(gateway.execute(request))

    assert actual is result
    assert gateway.requests == [request]
    assert gateway.requests[0] is request


def test_fake_model_gateway_preserves_invocation_order() -> None:
    gateway = FakeModelGateway(_result())
    first_request = _request(capability="conversation.first")
    second_request = _request(capability="conversation.second")

    asyncio.run(gateway.execute(first_request))
    asyncio.run(gateway.execute(second_request))

    assert gateway.requests == [first_request, second_request]


def test_fake_model_gateway_satisfies_model_gateway_protocol() -> None:
    gateway = FakeModelGateway(_result())

    assert isinstance(gateway, ModelGateway)
