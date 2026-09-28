from datetime import UTC, datetime
from uuid import uuid4

import pytest

from geem_ai.conversations.application.exceptions import ConversationNotFoundError
from geem_ai.conversations.application.handlers import GetConversationHandler
from geem_ai.conversations.application.ports.repositories import (
    ConversationReadRepository,
)
from geem_ai.conversations.application.queries import GetConversationQuery
from geem_ai.conversations.application.views import ConversationView
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


class FakeConversationReadRepository:
    def __init__(self, conversation: ConversationView | None) -> None:
        self.conversation = conversation
        self.received_tenant_id: TenantId | None = None
        self.received_conversation_id: ConversationId | None = None

    def get_view(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> ConversationView | None:
        self.received_tenant_id = tenant_id
        self.received_conversation_id = conversation_id
        return self.conversation


def build_actor() -> Actor:
    return Actor.user(
        tenant_id=TenantId(uuid4()),
        user_id=UserId(uuid4()),
    )


def build_view(conversation_id: ConversationId) -> ConversationView:
    now = datetime(2026, 7, 26, 12, 0, tzinfo=UTC)

    return ConversationView(
        conversation_id=conversation_id,
        owner_user_id=UserId(uuid4()),
        title="Consulta sobre instalación",
        status="active",
        language="es",
        created_at=now,
        updated_at=now,
        version=1,
    )


def test_get_conversation_handler_returns_conversation_view() -> None:
    actor = build_actor()
    conversation_id = ConversationId(uuid4())
    expected = build_view(conversation_id)

    repository: ConversationReadRepository = FakeConversationReadRepository(expected)
    handler = GetConversationHandler(repository=repository)

    result = handler.handle(
        GetConversationQuery(
            actor=actor,
            conversation_id=conversation_id,
        )
    )

    assert result == expected
    assert repository.received_tenant_id == actor.tenant_id
    assert repository.received_conversation_id == conversation_id


def test_get_conversation_handler_raises_when_conversation_is_not_found() -> None:
    actor = build_actor()
    conversation_id = ConversationId(uuid4())

    repository: ConversationReadRepository = FakeConversationReadRepository(None)
    handler = GetConversationHandler(repository=repository)

    with pytest.raises(ConversationNotFoundError):
        handler.handle(
            GetConversationQuery(
                actor=actor,
                conversation_id=conversation_id,
            )
        )
