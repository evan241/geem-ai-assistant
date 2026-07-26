from __future__ import annotations

import httpx
import pytest
from tests.support.environment import configure_test_environment

from geem_ai.shared.infrastructure.configuration.settings import get_settings


@pytest.mark.asyncio
async def test_liveness(monkeypatch: pytest.MonkeyPatch) -> None:
    configure_test_environment(monkeypatch)

    try:
        from apps.api.main import create_app

        transport = httpx.ASGITransport(app=create_app())

        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            response = await client.get("/api/v1/health/live")

        assert response.status_code == 200
        assert response.json() == {"status": "alive"}
    finally:
        get_settings.cache_clear()


@pytest.mark.asyncio
async def test_readiness_returns_service_unavailable_when_database_is_not_ready(
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

        transport = httpx.ASGITransport(app=create_app())

        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            response = await client.get("/api/v1/health/ready")

        assert response.status_code == 503
        assert response.json() == {"status": "not_ready"}
    finally:
        get_settings.cache_clear()
