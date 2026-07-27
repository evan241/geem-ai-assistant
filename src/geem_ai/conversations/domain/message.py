from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from geem_ai.conversations.domain.enums import MessageRole, MessageStatus
from geem_ai.conversations.domain.exceptions import MessageContentLockedError
from geem_ai.shared.domain.ids import (
    ConversationId,
    ExecutionId,
    MessageId,
    TenantId,
    UserId,
)


@dataclass(slots=True)
class Message:
    id: MessageId
    conversation_id: ConversationId
    tenant_id: TenantId
    author_id: UserId | None
    role: MessageRole
    content: str
    status: MessageStatus
    execution_id: ExecutionId | None
    created_at: datetime
    completed_at: datetime | None = None

    @classmethod
    def create_user(
        cls,
        *,
        message_id: MessageId,
        conversation_id: ConversationId,
        tenant_id: TenantId,
        author_id: UserId,
        content: str,
        now: datetime,
    ) -> Message:
        return cls(
            id=message_id,
            conversation_id=conversation_id,
            tenant_id=tenant_id,
            author_id=author_id,
            role=MessageRole.USER,
            content=content,
            status=MessageStatus.COMPLETED,
            execution_id=None,
            created_at=now,
            completed_at=now,
        )

    @classmethod
    def create_assistant(
        cls,
        *,
        message_id: MessageId,
        conversation_id: ConversationId,
        tenant_id: TenantId,
        content: str,
        now: datetime,
        execution_id: ExecutionId | None = None,
    ) -> Message:
        return cls(
            id=message_id,
            conversation_id=conversation_id,
            tenant_id=tenant_id,
            author_id=None,
            role=MessageRole.ASSISTANT,
            content=content,
            status=MessageStatus.STREAMING,
            execution_id=execution_id,
            created_at=now,
        )

    def append_content(self, delta: str) -> None:
        self._ensure_content_is_mutable()
        self.content += delta

    def replace_content(self, content: str) -> None:
        self._ensure_content_is_mutable()
        self.content = content

    def complete(self, *, now: datetime) -> None:
        self._ensure_content_is_mutable()

        self.status = MessageStatus.COMPLETED
        self.completed_at = now

    def _ensure_content_is_mutable(self) -> None:
        if self.status is MessageStatus.COMPLETED:
            raise MessageContentLockedError("Completed message content cannot be modified.")
