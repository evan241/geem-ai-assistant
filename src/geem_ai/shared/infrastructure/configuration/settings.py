from __future__ import annotations

from enum import StrEnum
from functools import lru_cache
from uuid import UUID

from pydantic import Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvironment(StrEnum):
    LOCAL = "local"
    TEST = "test"
    CI = "ci"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.local",
        extra="ignore",
        case_sensitive=True,
    )

    app_env: AppEnvironment = Field(alias="GEEM_APP_ENV")
    app_name: str = Field(
        default="GEEM AI Assistant",
        alias="GEEM_APP_NAME",
    )

    api_host: str = Field(
        default="0.0.0.0",
        alias="GEEM_API_HOST",
    )
    api_port: int = Field(
        default=8000,
        ge=1,
        le=65535,
        alias="GEEM_API_PORT",
    )

    database_url: str = Field(alias="GEEM_DATABASE_URL")
    redis_url: str = Field(alias="GEEM_REDIS_URL")

    storage_endpoint: str = Field(alias="GEEM_STORAGE_ENDPOINT")
    storage_bucket: str = Field(alias="GEEM_STORAGE_BUCKET")
    storage_access_key: SecretStr = Field(alias="GEEM_STORAGE_ACCESS_KEY")
    storage_secret_key: SecretStr = Field(alias="GEEM_STORAGE_SECRET_KEY")

    otel_service_name: str = Field(
        default="geem-ai-api",
        alias="GEEM_OTEL_SERVICE_NAME",
    )
    otel_endpoint: str = Field(alias="GEEM_OTEL_ENDPOINT")

    dev_auth_enabled: bool = Field(
        default=False,
        alias="GEEM_DEV_AUTH_ENABLED",
    )

    dev_actor_tenant_id: UUID | None = Field(
        default=None,
        alias="GEEM_DEV_ACTOR_TENANT_ID",
    )
    dev_actor_user_id: UUID | None = Field(
        default=None,
        alias="GEEM_DEV_ACTOR_USER_ID",
    )

    @model_validator(mode="after")
    def validate_environment_guards(self) -> Settings:
        if self.dev_auth_enabled and self.app_env is AppEnvironment.PRODUCTION:
            raise ValueError("Development authentication cannot run in production.")

        if self.dev_auth_enabled and self.app_env not in {
            AppEnvironment.LOCAL,
            AppEnvironment.TEST,
        }:
            raise ValueError(
                "Development authentication can only run in local or test environments."
            )

        if self.dev_auth_enabled and (
            self.dev_actor_tenant_id is None or self.dev_actor_user_id is None
        ):
            raise ValueError("Development authentication requires tenant and user IDs.")

        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
