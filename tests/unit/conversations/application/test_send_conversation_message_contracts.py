from dataclasses import FrozenInstanceError
from uuid import uuid4

import pytest

from geem_ai.conversations.application.commands import SendConversationMessageCommand
from geem_ai.conversations.application.results import SendConversationMessageResult
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import (
    ConversationId,
    ExecutionId,
    MessageId,
    TenantId,
    UserId,
)


def test_send_conversation_message_command_is_immutable_and_slotted() -> None:
    command = SendConversationMessageCommand(
        actor=Actor.user(tenant_id=TenantId(uuid4()), user_id=UserId(uuid4())),
        conversation_id=ConversationId(uuid4()),
        content="hello",
        idempotency_key="request-key",
    )

    assert command.capability_hint is None
    assert not hasattr(command, "__dict__")
    with pytest.raises(FrozenInstanceError):
        command.content = "changed"


def test_send_conversation_message_result_has_typed_ids_and_is_immutable() -> None:
    message_id = MessageId(uuid4())
    execution_id = ExecutionId(uuid4())
    result = SendConversationMessageResult(
        user_message_id=message_id,
        assistant_execution_id=execution_id,
        execution_status="created",
        capability="direct_response",
    )

    assert result.user_message_id is message_id
    assert result.assistant_execution_id is execution_id
    assert not hasattr(result, "__dict__")
    with pytest.raises(FrozenInstanceError):
        result.execution_status = "running"
