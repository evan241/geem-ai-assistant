from __future__ import annotations

from sqlalchemy import text

from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)


def test_postgres_can_connect_and_execute_query() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar_one() == 1
    finally:
        engine.dispose()
