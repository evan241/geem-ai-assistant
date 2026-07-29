from __future__ import annotations

from collections.abc import Iterator
from datetime import UTC, datetime
from uuid import uuid4

from geem_ai.conversations.application.handlers import CreateConversationHandler
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.ids import ConversationId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)


def get_create_conversation_handler() -> Iterator[CreateConversationHandler]:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        yield CreateConversationHandler(
            unit_of_work_factory=SQLAlchemyConversationUnitOfWorkFactory(engine),
            conversation_id_factory=lambda: ConversationId(uuid4()),
            clock=lambda: datetime.now(UTC),
        )
    finally:
        engine.dispose()
