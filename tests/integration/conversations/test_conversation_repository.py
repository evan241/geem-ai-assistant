from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.infrastructure.persistence.repositories import (
    SQLAlchemyConversationRepository,
)
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)


def build_conversation() -> Conversation:
    now = datetime.now(UTC)

    return Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        owner_user_id=UserId(uuid4()),
        title="Persistence test",
        language="es",
        now=now,
    )


def test_repository_adds_and_reloads_conversation() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        conversation = build_conversation()

        with Session(engine) as session:
            repository = SQLAlchemyConversationRepository(session)

            repository.add(conversation)
            session.commit()

        with Session(engine) as session:
            repository = SQLAlchemyConversationRepository(session)

            loaded = repository.get_by_id(
                conversation.tenant_id,
                conversation.id,
            )

            assert loaded is not None
            assert loaded.id == conversation.id
            assert loaded.tenant_id == conversation.tenant_id
            assert loaded.owner_user_id == conversation.owner_user_id
            assert loaded.title == conversation.title
            assert loaded.status == conversation.status
            assert loaded.language == conversation.language
            assert loaded.version == conversation.version
    finally:
        engine.dispose()


def test_repository_does_not_return_conversation_from_another_tenant() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        conversation = build_conversation()

        with Session(engine) as session:
            repository = SQLAlchemyConversationRepository(session)
            repository.add(conversation)
            session.commit()

        with Session(engine) as session:
            repository = SQLAlchemyConversationRepository(session)

            loaded = repository.get_by_id(
                TenantId(uuid4()),
                conversation.id,
            )

            assert loaded is None
    finally:
        engine.dispose()


def test_repository_exists_is_tenant_aware() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        conversation = build_conversation()

        with Session(engine) as session:
            repository = SQLAlchemyConversationRepository(session)
            repository.add(conversation)
            session.commit()

        with Session(engine) as session:
            repository = SQLAlchemyConversationRepository(session)

            assert repository.exists(
                conversation.tenant_id,
                conversation.id,
            )

            assert not repository.exists(
                TenantId(uuid4()),
                conversation.id,
            )
    finally:
        engine.dispose()
