from __future__ import annotations

from dataclasses import dataclass

from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, ExecutionId


@dataclass(frozen=True, slots=True)
class CreateConversationCommand:
    actor: Actor
    title: str | None
    language: str
    idempotency_key: str | None = None


@dataclass(frozen=True, slots=True)
class SendConversationMessageCommand:
    actor: Actor
    conversation_id: ConversationId
    content: str
    idempotency_key: str
    capability_hint: str | None = None


@dataclass(frozen=True, slots=True)
class ClaimAssistantExecutionCommand:
    actor: Actor
    execution_id: ExecutionId
