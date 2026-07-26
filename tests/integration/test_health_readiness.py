from __future__ import annotations

from fastapi.testclient import TestClient

from geem_ai.shared.infrastructure.configuration.settings import get_settings


def test_readiness_with_healthy_database() -> None:
    get_settings.cache_clear()

    try:
        from apps.api.main import create_app

        client = TestClient(create_app())
        response = client.get("/api/v1/health/ready")

        assert response.status_code == 200
        assert response.json() == {"status": "ready"}
    finally:
        get_settings.cache_clear()
