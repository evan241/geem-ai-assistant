from __future__ import annotations

import httpx
import pytest

from geem_ai.shared.infrastructure.configuration.settings import get_settings


@pytest.mark.asyncio
async def test_readiness_with_healthy_database() -> None:
    get_settings.cache_clear()

    try:
        from apps.api.main import create_app

        transport = httpx.ASGITransport(app=create_app())

        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            response = await client.get("/api/v1/health/ready")

        assert response.status_code == 200
        assert response.json() == {"status": "ready"}
    finally:
        get_settings.cache_clear()
