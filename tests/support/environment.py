from __future__ import annotations

import pytest

from geem_ai.shared.infrastructure.configuration.settings import get_settings


def configure_test_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    environment = {
        "GEEM_APP_ENV": "test",
        "GEEM_DATABASE_URL": ("postgresql+psycopg://geem_ai:geem_ai_dev@localhost:5432/geem_ai"),
        "GEEM_REDIS_URL": "redis://localhost:6379/0",
        "GEEM_STORAGE_ENDPOINT": "http://localhost:9000",
        "GEEM_STORAGE_BUCKET": "geem-ai-documents",
        "GEEM_STORAGE_ACCESS_KEY": "test-access-key",
        "GEEM_STORAGE_SECRET_KEY": "test-secret-key",
        "GEEM_OTEL_ENDPOINT": "http://localhost:4317",
        "GEEM_DEV_AUTH_ENABLED": "false",
    }

    for key, value in environment.items():
        monkeypatch.setenv(key, value)

    get_settings.cache_clear()
