from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import text

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.infrastructure.persistence.unit_of_work import (
    SQLAlchemyConversationUnitOfWorkFactory,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import (
    create_database_engine,
)


def build_actor() -> Actor:
    return Actor.user(
        tenant_id=TenantId(uuid4()),
        user_id=UserId(uuid4()),
    )


def build_conversation(actor: Actor) -> Conversation:
    assert actor.user_id is not None

    return Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=actor.tenant_id,
        owner_user_id=actor.user_id,
        title="UoW integration test",
        language="es",
        now=datetime.now(UTC),
    )


def test_unit_of_work_commits_conversation() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        actor = build_actor()
        conversation = build_conversation(actor)
        factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

        with factory.create(actor) as unit_of_work:
            unit_of_work.conversations.add(conversation)
            unit_of_work.commit()

        with factory.create(actor) as unit_of_work:
            loaded = unit_of_work.conversations.get_by_id(
                actor.tenant_id,
                conversation.id,
            )

            assert loaded is not None
            assert loaded.id == conversation.id
    finally:
        engine.dispose()


def test_unit_of_work_rolls_back_when_commit_is_not_called() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        actor = build_actor()
        conversation = build_conversation(actor)
        factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

        with factory.create(actor) as unit_of_work:
            unit_of_work.conversations.add(conversation)

        with factory.create(actor) as unit_of_work:
            loaded = unit_of_work.conversations.get_by_id(
                actor.tenant_id,
                conversation.id,
            )

            assert loaded is None
    finally:
        engine.dispose()


def test_unit_of_work_sets_database_actor_context() -> None:
    settings = get_settings()
    engine = create_database_engine(settings.database_url)

    try:
        actor = build_actor()
        factory = SQLAlchemyConversationUnitOfWorkFactory(engine)

        with factory.create(actor) as unit_of_work:
            tenant_value = unit_of_work.session.execute(
                text("SELECT current_setting('app.tenant_id', true)")
            ).scalar_one()

            user_value = unit_of_work.session.execute(
                text("SELECT current_setting('app.user_id', true)")
            ).scalar_one()

            assert tenant_value == str(actor.tenant_id.value)
            assert actor.user_id is not None
            assert user_value == str(actor.user_id.value)
    finally:
        engine.dispose()
