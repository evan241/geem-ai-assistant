from __future__ import annotations

from typing import cast

from sqlalchemy import DateTime, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column

from geem_ai.shared.infrastructure.persistence.database import (
    NAMING_CONVENTION,
    Base,
    TimestampMixin,
    VersionMixin,
)


class ExampleModel(TimestampMixin, VersionMixin, Base):
    __tablename__ = "example"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)


def test_base_uses_project_naming_convention() -> None:
    assert Base.metadata.naming_convention["ix"] == NAMING_CONVENTION["ix"]
    assert Base.metadata.naming_convention["uq"] == NAMING_CONVENTION["uq"]
    assert Base.metadata.naming_convention["ck"] == NAMING_CONVENTION["ck"]
    assert Base.metadata.naming_convention["fk"] == NAMING_CONVENTION["fk"]
    assert Base.metadata.naming_convention["pk"] == NAMING_CONVENTION["pk"]


def test_timestamp_mixin_defines_required_columns() -> None:
    table = ExampleModel.__table__

    created_at_type = cast(DateTime, table.c.created_at.type)
    updated_at_type = cast(DateTime, table.c.updated_at.type)

    assert table.c.created_at.nullable is False
    assert table.c.updated_at.nullable is False
    assert created_at_type.timezone is True
    assert updated_at_type.timezone is True


def test_version_mixin_starts_at_version_one() -> None:
    version = ExampleModel.__table__.c.version

    assert version.nullable is False
    assert version.default is not None
    assert version.default.arg == 1


def test_primary_key_uses_naming_convention() -> None:
    table = cast(Table, ExampleModel.__table__)

    assert table.primary_key.name == "pk_example"
