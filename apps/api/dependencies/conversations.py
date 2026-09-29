from __future__ import annotations

from collections.abc import Iterator
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from geem_ai.conversations.application.handlers import (
    CreateConversationHandler,
    GetConversationHandler,
    SendConversationMessageHandler,
)
from geem_ai.conversations.infrastructure.persistence.read_repository import (
    SQLAlchemyConversationReadRepository,
)
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId
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


def get_get_conversation_handler() -> Iterator[GetConversationHandler]:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        with Session(engine) as session:
            yield GetConversationHandler(
                repository=SQLAlchemyConversationReadRepository(session),
            )
    finally:
        engine.dispose()


def get_send_conversation_message_handler() -> Iterator[SendConversationMessageHandler]:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        yield SendConversationMessageHandler(
            unit_of_work_factory=SQLAlchemyConversationUnitOfWorkFactory(engine),
            message_id_factory=lambda: MessageId(uuid4()),
            execution_id_factory=lambda: ExecutionId(uuid4()),
            idempotency_id_factory=uuid4,
            outbox_event_id_factory=uuid4,
            clock=lambda: datetime.now(UTC),
        )
    finally:
        engine.dispose()
