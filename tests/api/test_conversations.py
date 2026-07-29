from uuid import UUID, uuid4

from apps.api.main import create_app
from fastapi.testclient import TestClient

from geem_ai.shared.infrastructure.configuration.settings import get_settings


def test_create_conversation_returns_201(monkeypatch) -> None:
    tenant_id = uuid4()
    user_id = uuid4()

    monkeypatch.setenv("GEEM_APP_ENV", "test")
    monkeypatch.setenv("GEEM_DEV_AUTH_ENABLED", "true")
    monkeypatch.setenv("GEEM_DEV_ACTOR_TENANT_ID", str(tenant_id))
    monkeypatch.setenv("GEEM_DEV_ACTOR_USER_ID", str(user_id))

    get_settings.cache_clear()

    try:
        app = create_app()

        with TestClient(app) as client:
            response = client.post(
                "/api/v1/conversations",
                json={
                    "title": "Consulta sobre instalación",
                    "language": "es",
                },
            )

        assert response.status_code == 201

        payload = response.json()

        UUID(payload["id"])
        assert payload["title"] == "Consulta sobre instalación"
        assert payload["status"] == "active"
        assert payload["language"] == "es"
        assert "created_at" in payload
        assert "updated_at" in payload
    finally:
        get_settings.cache_clear()
