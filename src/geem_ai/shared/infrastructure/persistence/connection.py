from __future__ import annotations

from sqlalchemy import Engine, create_engine


def create_database_engine(
    database_url: str,
    *,
    connect_timeout_seconds: int | None = None,
) -> Engine:
    connect_args: dict[str, object] = {}

    if connect_timeout_seconds is not None:
        connect_args["connect_timeout"] = connect_timeout_seconds

    return create_engine(
        database_url,
        pool_pre_ping=True,
        connect_args=connect_args,
    )
