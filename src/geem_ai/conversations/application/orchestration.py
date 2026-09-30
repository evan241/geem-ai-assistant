from __future__ import annotations

from collections.abc import Callable

from geem_ai.ai_runtime.public import ModelGateway
from geem_ai.conversations.application.commands import (
    ClaimAssistantExecutionCommand,
    CompleteAssistantExecutionCommand,
)
from geem_ai.conversations.application.execution_context import (
    DEFAULT_EXECUTION_MESSAGE_LIMIT,
    ConversationExecutionContextLoader,
    ModelExecutionRequestBuilder,
)
from geem_ai.conversations.application.handlers import (
    ClaimAssistantExecutionHandler,
    CompleteAssistantExecutionHandler,
)
from geem_ai.conversations.application.ports.unit_of_work import (
    ConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ExecutionId, MessageId


class AssistantExecutionOrchestrator:
    """Coordinate direct responses without holding a DB UoW across model I/O."""

    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        claim_handler: ClaimAssistantExecutionHandler,
        request_builder: ModelExecutionRequestBuilder,
        model_gateway: ModelGateway,
        complete_handler: CompleteAssistantExecutionHandler,
        message_id_factory: Callable[[], MessageId],
        context_message_limit: int = DEFAULT_EXECUTION_MESSAGE_LIMIT,
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._claim_handler = claim_handler
        self._request_builder = request_builder
        self._model_gateway = model_gateway
        self._complete_handler = complete_handler
        self._message_id_factory = message_id_factory
        self._context_message_limit = context_message_limit

    async def execute(self, *, actor: Actor, execution_id: ExecutionId) -> None:
        claimed = self._claim_handler.handle(
            ClaimAssistantExecutionCommand(actor=actor, execution_id=execution_id)
        )

        with self._unit_of_work_factory.create(actor) as unit_of_work:
            context = ConversationExecutionContextLoader(
                unit_of_work.messages,
                message_limit=self._context_message_limit,
            ).load(claimed.execution)
            request = self._request_builder.build(claimed.execution, context)

        result = await self._model_gateway.execute(request)

        self._complete_handler.handle(
            CompleteAssistantExecutionCommand(
                actor=actor,
                execution_id=execution_id,
                result=result,
                assistant_message_id=self._message_id_factory(),
            )
        )
