from datetime import UTC, datetime, timedelta
from uuid import UUID, uuid4

from sqlalchemy import Engine, delete
from sqlalchemy.orm import Session

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.message import Message
from geem_ai.conversations.infrastructure.persistence.models import ConversationModel, MessageModel
from geem_ai.conversations.infrastructure.persistence.repositories import (
    SQLAlchemyConversationRepository,
    SQLAlchemyMessageRepository,
)
from geem_ai.shared.domain.ids import ConversationId, MessageId, TenantId, UserId
from geem_ai.shared.infrastructure.configuration.settings import get_settings
from geem_ai.shared.infrastructure.persistence.connection import create_database_engine

TENANT_ID = TenantId(UUID("91000000-0000-0000-0000-000000000001"))
CONVERSATION_ID = ConversationId(UUID("92000000-0000-0000-0000-000000000001"))
USER_ID = UserId(UUID("93000000-0000-0000-0000-000000000001"))
NOW = datetime(2026, 9, 29, tzinfo=UTC)


def clean(engine: Engine) -> None:
    with Session(engine) as session:
        session.execute(
            delete(MessageModel).where(MessageModel.conversation_id == CONVERSATION_ID.value)
        )
        session.execute(
            delete(ConversationModel).where(ConversationModel.id == CONVERSATION_ID.value)
        )
        session.commit()


def test_execution_message_reads_are_scoped_bounded_and_deterministic() -> None:
    engine = create_database_engine(get_settings().database_url)
    clean(engine)
    conversation = Conversation.create(
        conversation_id=CONVERSATION_ID,
        tenant_id=TENANT_ID,
        owner_user_id=USER_ID,
        title="Execution context",
        language="en",
        now=NOW,
    )
    messages = tuple(
        Message.create_user(
            message_id=MessageId(UUID(int=100 + number)),
            conversation_id=CONVERSATION_ID,
            tenant_id=TENANT_ID,
            author_id=USER_ID,
            content=f"message {number}",
            now=NOW + timedelta(minutes=4 if number in {3, 4} else number),
        )
        for number in range(1, 6)
    )

    try:
        with Session(engine) as session:
            SQLAlchemyConversationRepository(session).add(conversation)
            repository = SQLAlchemyMessageRepository(session)
            for message in messages:
                repository.add(message)
            session.commit()

        with Session(engine) as session:
            repository = SQLAlchemyMessageRepository(session)
            recent = repository.list_recent_for_execution(TENANT_ID, CONVERSATION_ID, limit=3)
            hidden = repository.list_recent_for_execution(
                TenantId(uuid4()), CONVERSATION_ID, limit=20
            )
            found = repository.get_for_execution(TENANT_ID, CONVERSATION_ID, messages[3].id)
            wrong_tenant = repository.get_for_execution(
                TenantId(uuid4()), CONVERSATION_ID, messages[3].id
            )
            wrong_conversation = repository.get_for_execution(
                TENANT_ID, ConversationId(uuid4()), messages[3].id
            )

        # The newest three are selected; tied timestamps use ascending id chronologically.
        assert [message.content for message in recent] == [
            "message 3",
            "message 4",
            "message 5",
        ]
        assert hidden == ()
        assert found == messages[3]
        assert wrong_tenant is None
        assert wrong_conversation is None
    finally:
        clean(engine)
        engine.dispose()
