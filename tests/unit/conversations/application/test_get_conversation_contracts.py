from datetime import UTC, datetime
from uuid import uuid4

from geem_ai.conversations.application.queries import GetConversationQuery
from geem_ai.conversations.application.views import ConversationView
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


def test_get_conversation_query_preserves_authenticated_actor() -> None:
    actor = Actor.user(
        tenant_id=TenantId(uuid4()),
        user_id=UserId(uuid4()),
    )
    conversation_id = ConversationId(uuid4())

    query = GetConversationQuery(
        actor=actor,
        conversation_id=conversation_id,
    )

    assert query.actor == actor
    assert query.conversation_id == conversation_id


def test_conversation_view_exposes_query_data() -> None:
    now = datetime(2026, 7, 26, 12, 0, tzinfo=UTC)

    view = ConversationView(
        conversation_id=ConversationId(uuid4()),
        owner_user_id=UserId(uuid4()),
        title="Consulta sobre instalación",
        status="active",
        language="es",
        created_at=now,
        updated_at=now,
        version=1,
    )

    assert view.title == "Consulta sobre instalación"
    assert view.status == "active"
    assert view.language == "es"
    assert view.created_at == now
    assert view.updated_at == now
    assert view.version == 1
