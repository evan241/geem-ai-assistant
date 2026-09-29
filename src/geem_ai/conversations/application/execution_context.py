from __future__ import annotations

from dataclasses import dataclass

from geem_ai.ai_runtime.public import ModelExecutionRequest, ModelMessage
from geem_ai.conversations.application.exceptions import (
    ExecutionUserMessageNotFoundError,
    UnsupportedExecutionCapabilityError,
)
from geem_ai.conversations.application.ports.repositories import MessageRepository
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import ExecutionCapability
from geem_ai.shared.domain.ids import ConversationId

DEFAULT_EXECUTION_MESSAGE_LIMIT = 20


@dataclass(frozen=True, slots=True)
class ConversationExecutionContext:
    conversation_id: ConversationId
    messages: tuple[ModelMessage, ...]


class ConversationExecutionContextLoader:
    """Load the small, deterministic conversation slice used by M1 execution."""

    def __init__(
        self,
        message_repository: MessageRepository,
        *,
        message_limit: int = DEFAULT_EXECUTION_MESSAGE_LIMIT,
    ) -> None:
        if message_limit < 1:
            raise ValueError("message_limit must be positive")
        self._messages = message_repository
        self._message_limit = message_limit

    def load(self, execution: AssistantExecution) -> ConversationExecutionContext:
        recent = list(
            self._messages.list_recent_for_execution(
                execution.tenant_id,
                execution.conversation_id,
                limit=self._message_limit,
            )
        )
        user_message = self._messages.get_for_execution(
            execution.tenant_id,
            execution.conversation_id,
            execution.user_message_id,
        )
        if user_message is None:
            raise ExecutionUserMessageNotFoundError(
                "Execution user message was not found in its tenant conversation."
            )

        if all(message.id != user_message.id for message in recent):
            # Retain the accepted user input without allowing the context to exceed its bound.
            recent = recent[-(self._message_limit - 1) :] if self._message_limit > 1 else []
            recent.append(user_message)

        recent.sort(key=lambda message: (message.created_at, message.id.value))
        return ConversationExecutionContext(
            conversation_id=execution.conversation_id,
            messages=tuple(
                ModelMessage(role=message.role.value, content=message.content) for message in recent
            ),
        )


class ModelExecutionRequestBuilder:
    def build(
        self,
        execution: AssistantExecution,
        context: ConversationExecutionContext,
    ) -> ModelExecutionRequest:
        if execution.capability is not ExecutionCapability.DIRECT_RESPONSE:
            raise UnsupportedExecutionCapabilityError(
                f"Unsupported execution capability: {execution.capability.value}."
            )

        return ModelExecutionRequest(
            tenant_id=execution.tenant_id,
            execution_id=execution.id,
            capability=execution.capability.value,
            messages=context.messages,
            prompt_reference=None,
        )
