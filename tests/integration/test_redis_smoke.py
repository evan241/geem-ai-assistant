from __future__ import annotations

import os

from geem_ai.shared.infrastructure.cache.redis import create_redis_client


def test_redis_can_connect_and_ping() -> None:
    redis_url = os.environ["REDIS_URL"]
    client = create_redis_client(redis_url)

    try:
        assert client.ping() is True
    finally:
        client.close()
