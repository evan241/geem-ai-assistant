from __future__ import annotations

from typing import Protocol, Self

from geem_ai.conversations.application.ports.repositories import (
    AssistantExecutionRepository,
    ConversationRepository,
    IdempotencyRepository,
    MessageRepository,
    OutboxRepository,
)
from geem_ai.shared.domain.actor import Actor


class ConversationUnitOfWork(Protocol):
    conversations: ConversationRepository
    messages: MessageRepository
    executions: AssistantExecutionRepository
    idempotency: IdempotencyRepository
    outbox: OutboxRepository

    def __enter__(self) -> Self: ...

    def __exit__(
        self,
        exc_type: object,
        exc_value: object,
        traceback: object,
    ) -> None: ...

    def commit(self) -> None: ...

    def rollback(self) -> None: ...


class ConversationUnitOfWorkFactory(Protocol):
    def create(self, actor: Actor) -> ConversationUnitOfWork: ...
