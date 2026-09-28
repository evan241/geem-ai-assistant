from __future__ import annotations

from dataclasses import dataclass

from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId


@dataclass(frozen=True, slots=True)
class GetConversationQuery:
    actor: Actor
    conversation_id: ConversationId
