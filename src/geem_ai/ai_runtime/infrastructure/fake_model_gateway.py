from geem_ai.ai_runtime.application.models import ModelExecutionRequest, ModelExecutionResult


class FakeModelGateway:
    def __init__(self, result: ModelExecutionResult) -> None:
        self.result = result
        self.requests: list[ModelExecutionRequest] = []

    async def execute(self, request: ModelExecutionRequest) -> ModelExecutionResult:
        self.requests.append(request)
        return self.result
