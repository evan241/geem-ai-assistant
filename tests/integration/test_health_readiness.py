from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from tests.support.environment import configure_test_environment

from geem_ai.shared.infrastructure.configuration.settings import get_settings


def test_readiness_with_healthy_database(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_test_environment(monkeypatch)

    monkeypatch.setenv(
        "GEEM_DATABASE_URL",
        "postgresql+psycopg://geem_ai:geem_ai_dev@postgres:5432/geem_ai",
    )
    get_settings.cache_clear()

    try:
        from apps.api.main import create_app

        client = TestClient(create_app())
        response = client.get("/api/v1/health/ready")

        assert response.status_code == 200
        assert response.json() == {"status": "ready"}
    finally:
        get_settings.cache_clear()
