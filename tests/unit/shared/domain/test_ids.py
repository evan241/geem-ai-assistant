from __future__ import annotations

from uuid import uuid4

from geem_ai.shared.domain.ids import TenantId


def test_tenant_id_preserves_uuid_value() -> None:
    value = uuid4()

    tenant_id = TenantId(value=value)

    assert tenant_id.value == value


def test_tenant_id_has_value_semantics() -> None:
    value = uuid4()

    assert TenantId(value=value) == TenantId(value=value)


def test_tenant_id_is_immutable() -> None:
    tenant_id = TenantId(value=uuid4())

    try:
        tenant_id.value = uuid4()  # type: ignore[misc]
    except AttributeError:
        pass
    else:
        raise AssertionError("TenantId must be immutable")
