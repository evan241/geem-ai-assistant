from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from geem_ai.shared.domain.ids import ConversationId, UserId


@dataclass(frozen=True, slots=True)
class ConversationView:
    conversation_id: ConversationId
    owner_user_id: UserId
    title: str
    status: str
    language: str
    created_at: datetime
    updated_at: datetime
    version: int
