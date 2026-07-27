from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from geem_ai.shared.domain.ids import ConversationId


@dataclass(frozen=True, slots=True)
class CreateConversationResult:
    conversation_id: ConversationId
    title: str
    status: str
    language: str
    created_at: datetime
    updated_at: datetime
    version: int
