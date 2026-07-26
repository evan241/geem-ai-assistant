from __future__ import annotations

import pytest
from pydantic import ValidationError

from geem_ai.shared.infrastructure.configuration.settings import (
    AppEnvironment,
    Settings,
)


def valid_environment() -> dict[str, str]:
    return {
        "GEEM_APP_ENV": "test",
        "GEEM_DATABASE_URL": "postgresql+psycopg://user:password@postgres:5432/geem_ai",
        "GEEM_REDIS_URL": "redis://redis:6379/0",
        "GEEM_STORAGE_ENDPOINT": "http://minio:9000",
        "GEEM_STORAGE_BUCKET": "geem-ai-documents",
        "GEEM_STORAGE_ACCESS_KEY": "test-access-key",
        "GEEM_STORAGE_SECRET_KEY": "test-secret-key",
        "GEEM_OTEL_ENDPOINT": "http://otel-collector:4317",
    }


def test_settings_load_from_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for key, value in valid_environment().items():
        monkeypatch.setenv(key, value)

    settings = Settings(_env_file=None)

    assert settings.app_env is AppEnvironment.TEST
    assert settings.database_url.startswith("postgresql+psycopg://")
    assert settings.redis_url == "redis://redis:6379/0"
    assert settings.storage_bucket == "geem-ai-documents"
    assert settings.api_port == 8000
    assert settings.dev_auth_enabled is False


def test_missing_critical_configuration_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for key, value in valid_environment().items():
        monkeypatch.setenv(key, value)

    monkeypatch.delenv("GEEM_DATABASE_URL")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_invalid_environment_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    environment = valid_environment()
    environment["GEEM_APP_ENV"] = "banana"

    for key, value in environment.items():
        monkeypatch.setenv(key, value)

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_development_authentication_is_forbidden_in_production(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    environment = valid_environment()
    environment["GEEM_APP_ENV"] = "production"
    environment["GEEM_DEV_AUTH_ENABLED"] = "true"

    for key, value in environment.items():
        monkeypatch.setenv(key, value)

    with pytest.raises(
        ValidationError,
        match="Development authentication cannot run in production",
    ):
        Settings(_env_file=None)
