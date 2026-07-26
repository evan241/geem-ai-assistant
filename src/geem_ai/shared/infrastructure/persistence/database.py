from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Integer, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

NAMING_CONVENTION = {
    "ix": "ix_%(table_name)s__%(column_0_name)s",
    "uq": "uq_%(table_name)s__%(column_0_name)s",
    "ck": "ck_%(table_name)s__%(column_0_name)s",
    "fk": "fk_%(table_name)s__%(column_0_name)s__%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )


class VersionMixin:
    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )
