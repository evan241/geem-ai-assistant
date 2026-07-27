from datetime import UTC, datetime
from uuid import uuid4

import pytest

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.exceptions import ConversationNotActiveError
from geem_ai.shared.domain.ids import ConversationId, MessageId, TenantId, UserId


def test_active_conversation_accepts_message() -> None:
    now = datetime.now(UTC)
    conversation = Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        owner_user_id=UserId(uuid4()),
        title="First conversation",
        language="es",
        now=now,
    )

    message = conversation.add_user_message(
        message_id=MessageId(uuid4()),
        content="Hola",
        author_id=conversation.owner_user_id,
        now=now,
    )

    assert message.content == "Hola"
    assert message.tenant_id == conversation.tenant_id
    assert conversation.last_message_at == now


def test_archived_conversation_rejects_message() -> None:
    now = datetime.now(UTC)
    conversation = Conversation.create(
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        owner_user_id=UserId(uuid4()),
        title="Archived conversation",
        language="es",
        now=now,
    )
    conversation.archive()

    with pytest.raises(ConversationNotActiveError):
        conversation.add_user_message(
            message_id=MessageId(uuid4()),
            content="No debería aceptarse",
            author_id=conversation.owner_user_id,
            now=now,
        )


def test_unsupported_language_is_rejected() -> None:
    now = datetime.now(UTC)

    with pytest.raises(ValueError):
        Conversation.create(
            conversation_id=ConversationId(uuid4()),
            tenant_id=TenantId(uuid4()),
            owner_user_id=UserId(uuid4()),
            title="Unsupported language",
            language="fr",
            now=now,
        )
