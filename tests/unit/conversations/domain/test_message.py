from datetime import UTC, datetime
from uuid import uuid4

import pytest

from geem_ai.conversations.domain.enums import MessageRole, MessageStatus
from geem_ai.conversations.domain.exceptions import MessageContentLockedError
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.ids import ConversationId, MessageId, TenantId, UserId


def test_user_message_is_created_completed() -> None:
    now = datetime.now(UTC)

    message = Message.create_user(
        message_id=MessageId(uuid4()),
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        author_id=UserId(uuid4()),
        content="Hola",
        now=now,
    )

    assert message.role is MessageRole.USER
    assert message.status is MessageStatus.COMPLETED
    assert message.content == "Hola"
    assert message.created_at == now


def test_completed_message_cannot_change_content() -> None:
    now = datetime.now(UTC)

    message = Message.create_user(
        message_id=MessageId(uuid4()),
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        author_id=UserId(uuid4()),
        content="Contenido original",
        now=now,
    )

    with pytest.raises(MessageContentLockedError):
        message.replace_content("Contenido modificado")


def test_assistant_message_can_stream_before_completion() -> None:
    now = datetime.now(UTC)

    message = Message.create_assistant(
        message_id=MessageId(uuid4()),
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        content="",
        now=now,
    )

    assert message.role is MessageRole.ASSISTANT
    assert message.status is MessageStatus.STREAMING

    message.append_content("Hola")
    message.append_content(", mundo")
    message.complete(now=now)

    assert message.content == "Hola, mundo"
    assert message.status is MessageStatus.COMPLETED


def test_completed_message_cannot_be_completed_again() -> None:
    now = datetime.now(UTC)

    message = Message.create_assistant(
        message_id=MessageId(uuid4()),
        conversation_id=ConversationId(uuid4()),
        tenant_id=TenantId(uuid4()),
        content="Respuesta",
        now=now,
    )

    message.complete(now=now)

    with pytest.raises(MessageContentLockedError):
        message.complete(now=now)
