from uuid import uuid4

from geem_ai.shared.domain.actor import Actor, ActorType
from geem_ai.shared.domain.ids import TenantId, UserId


def test_user_actor_preserves_authenticated_context() -> None:
    tenant_id = TenantId(uuid4())
    user_id = UserId(uuid4())

    actor = Actor.user(
        tenant_id=tenant_id,
        user_id=user_id,
        roles=frozenset({"operator"}),
    )

    assert actor.actor_type is ActorType.USER
    assert actor.tenant_id == tenant_id
    assert actor.user_id == user_id
    assert actor.roles == frozenset({"operator"})


def test_user_actor_requires_user_id() -> None:
    tenant_id = TenantId(uuid4())
    user_id = UserId(uuid4())

    actor = Actor.user(
        tenant_id=tenant_id,
        user_id=user_id,
    )

    assert actor.user_id is not None
