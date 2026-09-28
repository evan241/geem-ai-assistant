from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import update
from sqlalchemy.orm import Session

from geem_ai.conversations.application.views import ConversationView
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.infrastructure.persistence.models import ConversationModel
from geem_ai.conversations.infrastructure.persistence.read_repository import (
    SQLAlchemyConversationReadRepository,
)
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
        title="Read repository test",
        language="es",
        now=now,
    )


def persist_conversation(
    session: Session,
    conversation: Conversation,
) -> None:
    repository = SQLAlchemyConversationRepository(session)
    repository.add(conversation)
    session.commit()


def test_read_repository_returns_conversation_view() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        conversation = build_conversation()

        with Session(engine) as session:
            persist_conversation(session, conversation)

        with Session(engine) as session:
            repository = SQLAlchemyConversationReadRepository(session)

            view = repository.get_view(
                conversation.tenant_id,
                conversation.id,
            )

            assert isinstance(view, ConversationView)
            assert view.conversation_id == conversation.id
            assert view.owner_user_id == conversation.owner_user_id
            assert view.title == conversation.title
            assert view.status == conversation.status.value
            assert view.language == conversation.language.value
            assert view.created_at == conversation.created_at
            assert view.updated_at == conversation.updated_at
            assert view.version == conversation.version
    finally:
        engine.dispose()


def test_read_repository_does_not_return_another_tenants_conversation() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        conversation = build_conversation()

        with Session(engine) as session:
            persist_conversation(session, conversation)

        with Session(engine) as session:
            repository = SQLAlchemyConversationReadRepository(session)

            view = repository.get_view(
                TenantId(uuid4()),
                conversation.id,
            )

            assert view is None
    finally:
        engine.dispose()


def test_read_repository_does_not_return_soft_deleted_conversation() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        conversation = build_conversation()

        with Session(engine) as session:
            persist_conversation(session, conversation)

            session.execute(
                update(ConversationModel)
                .where(
                    ConversationModel.tenant_id == conversation.tenant_id.value,
                    ConversationModel.id == conversation.id.value,
                )
                .values(deleted_at=datetime.now(UTC))
            )
            session.commit()

        with Session(engine) as session:
            repository = SQLAlchemyConversationReadRepository(session)

            view = repository.get_view(
                conversation.tenant_id,
                conversation.id,
            )

            assert view is None
    finally:
        engine.dispose()


def test_read_repository_returns_none_for_unknown_conversation() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        with Session(engine) as session:
            repository = SQLAlchemyConversationReadRepository(session)

            view = repository.get_view(
                TenantId(uuid4()),
                ConversationId(uuid4()),
            )

            assert view is None
    finally:
        engine.dispose()
