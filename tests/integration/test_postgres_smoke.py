from __future__ import annotations

import os

from sqlalchemy import text

from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)


def test_postgres_can_connect_and_execute_query() -> None:
    database_url = os.environ["DATABASE_URL"]
    engine = create_database_engine(database_url)

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar_one() == 1
    finally:
        engine.dispose()
