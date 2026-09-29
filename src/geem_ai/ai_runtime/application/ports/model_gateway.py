from typing import Protocol, runtime_checkable

from geem_ai.ai_runtime.application.models import ModelExecutionRequest, ModelExecutionResult


@runtime_checkable
class ModelGateway(Protocol):
    async def execute(self, request: ModelExecutionRequest) -> ModelExecutionResult: ...
