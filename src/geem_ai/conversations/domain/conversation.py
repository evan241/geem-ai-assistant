from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from geem_ai.conversations.domain.enums import (
    ConversationLanguage,
    ConversationStatus,
)
from geem_ai.conversations.domain.exceptions import ConversationNotActiveError
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.ids import (
    ConversationId,
    MessageId,
    TenantId,
    UserId,
)


@dataclass(slots=True)
class Conversation:
    id: ConversationId
    tenant_id: TenantId
    owner_user_id: UserId
    title: str
    status: ConversationStatus
    language: ConversationLanguage
    created_at: datetime
    updated_at: datetime
    last_message_at: datetime | None = None
    version: int = 1

    @classmethod
    def create(
        cls,
        *,
        conversation_id: ConversationId,
        tenant_id: TenantId,
        owner_user_id: UserId,
        title: str,
        language: ConversationLanguage | str,
        now: datetime,
    ) -> Conversation:
        try:
            resolved_language = ConversationLanguage(language)
        except ValueError as exc:
            raise ValueError(f"Unsupported conversation language: {language}") from exc
        return cls(
            id=conversation_id,
            tenant_id=tenant_id,
            owner_user_id=owner_user_id,
            title=title,
            status=ConversationStatus.ACTIVE,
            language=resolved_language,
            created_at=now,
            updated_at=now,
        )

    def add_user_message(
        self,
        *,
        message_id: MessageId,
        content: str,
        author_id: UserId,
        now: datetime,
    ) -> Message:
        if self.status is not ConversationStatus.ACTIVE:
            raise ConversationNotActiveError("Conversation must be active to accept messages.")

        message = Message.create_user(
            message_id=message_id,
            conversation_id=self.id,
            tenant_id=self.tenant_id,
            author_id=author_id,
            content=content,
            now=now,
        )

        self.last_message_at = now
        self.updated_at = now

        return message

    def archive(self) -> None:
        self.status = ConversationStatus.ARCHIVED
