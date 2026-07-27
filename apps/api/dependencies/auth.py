from __future__ import annotations

from fastapi import HTTPException, status

from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings


def get_actor() -> Actor:
    settings = get_settings()

    if not settings.dev_auth_enabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication is required.",
        )

    if settings.dev_actor_tenant_id is None or settings.dev_actor_user_id is None:
        raise RuntimeError("Development actor is not configured.")

    return Actor.user(
        tenant_id=TenantId(settings.dev_actor_tenant_id),
        user_id=UserId(settings.dev_actor_user_id),
    )
