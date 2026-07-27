from datetime import UTC, datetime
from typing import Self
from uuid import uuid4

from geem_ai.conversations.application.commands import CreateConversationCommand
from geem_ai.conversations.application.handlers import CreateConversationHandler
from geem_ai.conversations.application.ports.repositories import (
    ConversationRepository,
)
from geem_ai.conversations.application.ports.unit_of_work import (
    ConversationUnitOfWork,
)
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


class FakeConversationRepository:
    def __init__(self) -> None:
        self.added: list[Conversation] = []

    def add(self, conversation: Conversation) -> None:
        self.added.append(conversation)

    def get_by_id(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> Conversation | None:
        return next(
            (
                conversation
                for conversation in self.added
                if conversation.tenant_id == tenant_id and conversation.id == conversation_id
            ),
            None,
        )

    def exists(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> bool:
        return self.get_by_id(tenant_id, conversation_id) is not None


class FakeConversationUnitOfWork:
    def __init__(self) -> None:
        self.conversation_repository = FakeConversationRepository()
        self.conversations: ConversationRepository = self.conversation_repository
        self.committed = False
        self.rolled_back = False

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: object,
        exc_value: object,
        traceback: object,
    ) -> None:
        if exc_type is not None:
            self.rollback()

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        self.rolled_back = True


class FakeConversationUnitOfWorkFactory:
    def __init__(self, unit_of_work: FakeConversationUnitOfWork) -> None:
        self.unit_of_work = unit_of_work
        self.actor: Actor | None = None

    def create(self, actor: Actor) -> ConversationUnitOfWork:
        self.actor = actor
        return self.unit_of_work


def test_create_conversation_handler_creates_and_commits_conversation() -> None:
    now = datetime(2026, 7, 26, 12, 0, tzinfo=UTC)
    conversation_id = ConversationId(uuid4())

    actor = Actor.user(
        tenant_id=TenantId(uuid4()),
        user_id=UserId(uuid4()),
    )

    unit_of_work = FakeConversationUnitOfWork()
    unit_of_work_factory = FakeConversationUnitOfWorkFactory(unit_of_work)

    handler = CreateConversationHandler(
        unit_of_work_factory=unit_of_work_factory,
        conversation_id_factory=lambda: conversation_id,
        clock=lambda: now,
    )

    result = handler.handle(
        CreateConversationCommand(
            actor=actor,
            title="Consulta sobre instalación",
            language="es",
        )
    )

    assert unit_of_work_factory.actor == actor
    assert unit_of_work.committed is True

    assert len(unit_of_work.conversation_repository.added) == 1

    conversation = unit_of_work.conversation_repository.added[0]

    assert conversation.id == conversation_id
    assert conversation.tenant_id == actor.tenant_id
    assert conversation.owner_user_id == actor.user_id
    assert conversation.title == "Consulta sobre instalación"
    assert conversation.created_at == now

    assert result.conversation_id == conversation_id
    assert result.title == "Consulta sobre instalación"
    assert result.status == "active"
    assert result.language == "es"
    assert result.created_at == now
    assert result.updated_at == now
    assert result.version == 1
