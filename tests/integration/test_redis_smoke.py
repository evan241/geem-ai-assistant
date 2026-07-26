from __future__ import annotations

from geem_ai.shared.infrastructure.cache.redis import create_redis_client
from geem_ai.shared.infrastructure.configuration.settings import get_settings


def test_redis_can_connect_and_ping() -> None:
    settings = get_settings()
    client = create_redis_client(settings.redis_url)

    try:
        assert client.ping() is True
    finally:
        client.close()
