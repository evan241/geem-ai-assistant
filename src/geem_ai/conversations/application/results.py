from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId


@dataclass(frozen=True, slots=True)
class CreateConversationResult:
    conversation_id: ConversationId
    title: str
    status: str
    language: str
    created_at: datetime
    updated_at: datetime
    version: int


@dataclass(frozen=True, slots=True)
class SendConversationMessageResult:
    user_message_id: MessageId
    assistant_execution_id: ExecutionId
    execution_status: str
    capability: str


@dataclass(frozen=True, slots=True)
class ClaimAssistantExecutionResult:
    execution: AssistantExecution
