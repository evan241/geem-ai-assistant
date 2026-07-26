from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from tests.support.environment import configure_test_environment

from geem_ai.shared.infrastructure.configuration.settings import get_settings


def test_liveness(monkeypatch: pytest.MonkeyPatch) -> None:
    configure_test_environment(monkeypatch)

    try:
        from apps.api.main import create_app

        client = TestClient(create_app())
        response = client.get("/api/v1/health/live")

        assert response.status_code == 200
        assert response.json() == {"status": "alive"}
    finally:
        get_settings.cache_clear()


def test_readiness_returns_service_unavailable_when_database_is_not_ready(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_test_environment(monkeypatch)
    get_settings.cache_clear()

    try:
        from apps.api.main import create_app

        monkeypatch.setattr(
            "apps.api.routes.health.is_database_ready",
            lambda engine: False,
        )

        client = TestClient(create_app())
        response = client.get("/api/v1/health/ready")

        assert response.status_code == 503
        assert response.json() == {"status": "not_ready"}
    finally:
        get_settings.cache_clear()
