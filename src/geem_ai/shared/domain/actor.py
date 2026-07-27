from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from geem_ai.shared.domain.ids import TenantId, UserId


class ActorType(StrEnum):
    USER = "user"
    SERVICE = "service"
    SYSTEM = "system"
    MCP_CLIENT = "mcp_client"
    WORKER = "worker"


@dataclass(frozen=True, slots=True)
class Actor:
    actor_type: ActorType
    tenant_id: TenantId
    user_id: UserId | None
    roles: frozenset[str] = frozenset()

    @classmethod
    def user(
        cls,
        *,
        tenant_id: TenantId,
        user_id: UserId,
        roles: frozenset[str] = frozenset(),
    ) -> Actor:
        return cls(
            actor_type=ActorType.USER,
            tenant_id=tenant_id,
            user_id=user_id,
            roles=roles,
        )
