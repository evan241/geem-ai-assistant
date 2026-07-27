from typing import Protocol

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.shared.domain.ids import ConversationId, TenantId


class ConversationRepository(Protocol):
    def add(self, conversation: Conversation) -> None: ...

    def get_by_id(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> Conversation | None: ...

    def exists(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> bool: ...
