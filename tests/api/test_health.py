from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from tests.support.environment import configure_test_environment

from geem_ai.shared.infrastructure.configuration.settings import get_settings


def test_health(monkeypatch: pytest.MonkeyPatch) -> None:
    configure_test_environment(monkeypatch)

    try:
        from apps.api.main import create_app

        client = TestClient(create_app())
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    finally:
        get_settings.cache_clear()
