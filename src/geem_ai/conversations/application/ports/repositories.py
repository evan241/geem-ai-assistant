from datetime import datetime
from typing import Protocol
from uuid import UUID

from geem_ai.conversations.application.events import OutboxEvent
from geem_ai.conversations.application.idempotency import IdempotencyRecord
from geem_ai.conversations.application.views import ConversationView
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId


class ConversationRepository(Protocol):
    def add(self, conversation: Conversation) -> None: ...

    def save(self, conversation: Conversation) -> None: ...

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


class MessageRepository(Protocol):
    def add(self, message: Message) -> None: ...

    def list_recent_for_execution(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
        *,
        limit: int,
    ) -> tuple[Message, ...]: ...

    def get_for_execution(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
        message_id: MessageId,
    ) -> Message | None: ...


class AssistantExecutionRepository(Protocol):
    def add(self, execution: AssistantExecution) -> None: ...

    def get_for_update(
        self,
        tenant_id: TenantId,
        execution_id: ExecutionId,
    ) -> AssistantExecution | None: ...

    def save(self, execution: AssistantExecution) -> None: ...


class OutboxRepository(Protocol):
    def add(self, event: OutboxEvent) -> None: ...


class IdempotencyRepository(Protocol):
    def get(self, tenant_id: TenantId, scope: str, key: str) -> IdempotencyRecord | None: ...

    def reserve(self, record: IdempotencyRecord) -> bool: ...

    def complete(
        self,
        record: IdempotencyRecord,
        *,
        response_status: int,
        response_body: dict[str, object],
        resource_type: str,
        resource_id: UUID,
        completed_at: datetime,
    ) -> None: ...


class ConversationReadRepository(Protocol):
    def get_view(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> ConversationView | None: ...
