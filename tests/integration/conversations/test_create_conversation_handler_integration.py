from datetime import UTC, datetime
from uuid import uuid4

from geem_ai.conversations.application.commands import CreateConversationCommand
from geem_ai.conversations.application.handlers import CreateConversationHandler
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)


def test_create_conversation_handler_persists_conversation() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        actor = Actor.user(
            tenant_id=TenantId(uuid4()),
            user_id=UserId(uuid4()),
        )

        conversation_id = ConversationId(uuid4())
        now = datetime(2026, 7, 27, 12, 0, tzinfo=UTC)

        unit_of_work_factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

        handler = CreateConversationHandler(
            unit_of_work_factory=unit_of_work_factory,
            conversation_id_factory=lambda: conversation_id,
            clock=lambda: now,
        )

        result = handler.handle(
            CreateConversationCommand(
                actor=actor,
                title="Consulta sobre instalación",
                language="es",
            )
        )

        assert result.conversation_id == conversation_id
        assert result.title == "Consulta sobre instalación"
        assert result.status == "active"
        assert result.language == "es"

        with unit_of_work_factory.create(actor) as unit_of_work:
            persisted = unit_of_work.conversations.get_by_id(
                actor.tenant_id,
                conversation_id,
            )

            assert persisted is not None
            assert persisted.id == conversation_id
            assert persisted.tenant_id == actor.tenant_id
            assert persisted.owner_user_id == actor.user_id
            assert persisted.title == "Consulta sobre instalación"
            assert persisted.status.value == "active"
            assert persisted.language.value == "es"
            assert persisted.created_at == now
    finally:
        engine.dispose()
