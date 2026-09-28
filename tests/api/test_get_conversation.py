from datetime import UTC, datetime
from uuid import uuid4

from apps.api.dependencies.auth import get_actor
from apps.api.dependencies.conversations import get_get_conversation_handler
from apps.api.main import create_app
from fastapi import FastAPI
from fastapi.testclient import TestClient

from geem_ai.conversations.application.handlers import GetConversationHandler
from geem_ai.conversations.application.views import ConversationView
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


class InMemoryConversationReadRepository:
    def __init__(
        self,
        *,
        tenant_id: TenantId,
        conversation: ConversationView,
        deleted: bool = False,
    ) -> None:
        self._tenant_id = tenant_id
        self._conversation = conversation
        self._deleted = deleted

    def get_view(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> ConversationView | None:
        if (
            self._deleted
            or tenant_id != self._tenant_id
            or conversation_id != self._conversation.conversation_id
        ):
            return None
        return self._conversation


def build_view() -> ConversationView:
    timestamp = datetime(2026, 9, 28, 10, 30, tzinfo=UTC)
    return ConversationView(
        conversation_id=ConversationId(uuid4()),
        owner_user_id=UserId(uuid4()),
        title="Consulta sobre instalación",
        status="active",
        language="es",
        created_at=timestamp,
        updated_at=timestamp,
        version=1,
    )


def build_app(
    *,
    actor_tenant_id: TenantId,
    stored_tenant_id: TenantId,
    conversation: ConversationView,
    deleted: bool = False,
) -> FastAPI:
    actor = Actor.user(tenant_id=actor_tenant_id, user_id=UserId(uuid4()))
    repository = InMemoryConversationReadRepository(
        tenant_id=stored_tenant_id,
        conversation=conversation,
        deleted=deleted,
    )
    app = create_app()
    app.dependency_overrides[get_actor] = lambda: actor
    app.dependency_overrides[get_get_conversation_handler] = lambda: GetConversationHandler(
        repository=repository
    )
    return app


def test_get_conversation_returns_200_for_actor_tenant() -> None:
    tenant_id = TenantId(uuid4())
    conversation = build_view()
    app = build_app(
        actor_tenant_id=tenant_id,
        stored_tenant_id=tenant_id,
        conversation=conversation,
    )

    with TestClient(app) as client:
        response = client.get(f"/api/v1/conversations/{conversation.conversation_id.value}")

    assert response.status_code == 200
    assert response.json() == {
        "id": str(conversation.conversation_id.value),
        "title": "Consulta sobre instalación",
        "status": "active",
        "language": "es",
        "created_at": "2026-09-28T10:30:00Z",
        "updated_at": "2026-09-28T10:30:00Z",
    }


def test_get_conversation_returns_404_for_unknown_id() -> None:
    tenant_id = TenantId(uuid4())
    conversation = build_view()
    app = build_app(
        actor_tenant_id=tenant_id,
        stored_tenant_id=tenant_id,
        conversation=conversation,
    )

    with TestClient(app) as client:
        response = client.get(f"/api/v1/conversations/{uuid4()}")

    assert response.status_code == 404


def test_get_conversation_returns_404_for_another_tenants_conversation() -> None:
    conversation = build_view()
    app = build_app(
        actor_tenant_id=TenantId(uuid4()),
        stored_tenant_id=TenantId(uuid4()),
        conversation=conversation,
    )

    with TestClient(app) as client:
        response = client.get(f"/api/v1/conversations/{conversation.conversation_id.value}")

    assert response.status_code == 404


def test_get_conversation_returns_404_for_soft_deleted_conversation() -> None:
    tenant_id = TenantId(uuid4())
    conversation = build_view()
    app = build_app(
        actor_tenant_id=tenant_id,
        stored_tenant_id=tenant_id,
        conversation=conversation,
        deleted=True,
    )

    with TestClient(app) as client:
        response = client.get(f"/api/v1/conversations/{conversation.conversation_id.value}")

    assert response.status_code == 404


def test_get_conversation_returns_422_for_invalid_uuid() -> None:
    tenant_id = TenantId(uuid4())
    app = build_app(
        actor_tenant_id=tenant_id,
        stored_tenant_id=tenant_id,
        conversation=build_view(),
    )

    with TestClient(app) as client:
        response = client.get("/api/v1/conversations/not-a-uuid")

    assert response.status_code == 422
