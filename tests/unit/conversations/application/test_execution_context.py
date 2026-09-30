from datetime import UTC, datetime, timedelta
from uuid import UUID

import pytest

from geem_ai.ai_runtime.public import ModelExecutionRequest, ModelMessage
from geem_ai.conversations.application.exceptions import (
    ExecutionUserMessageNotFoundError,
    UnsupportedExecutionCapabilityError,
)
from geem_ai.conversations.application.execution_context import (
    ConversationExecutionContextLoader,
    ModelExecutionRequestBuilder,
)
from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.enums import (
    ExecutionCapability,
    MessageRole,
    MessageStatus,
)
from geem_ai.conversations.domain.message import Message
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId, TenantId

TENANT_ID = TenantId(UUID("10000000-0000-0000-0000-000000000001"))
CONVERSATION_ID = ConversationId(UUID("20000000-0000-0000-0000-000000000001"))
EXECUTION_ID = ExecutionId(UUID("30000000-0000-0000-0000-000000000001"))
NOW = datetime(2026, 9, 29, tzinfo=UTC)


def make_message(number: int, role: MessageRole = MessageRole.USER) -> Message:
    return Message(
        id=MessageId(UUID(int=number)),
        tenant_id=TENANT_ID,
        conversation_id=CONVERSATION_ID,
        author_id=None,
        role=role,
        content=f"content {number}",
        status=MessageStatus.COMPLETED,
        execution_id=None,
        created_at=NOW + timedelta(minutes=number),
        completed_at=NOW + timedelta(minutes=number),
    )


class FakeMessageRepository:
    def __init__(self, messages: tuple[Message, ...], user_message: Message | None) -> None:
        self.messages = messages
        self.user_message = user_message
        self.list_calls: list[tuple[TenantId, ConversationId, int]] = []
        self.get_calls: list[tuple[TenantId, ConversationId, MessageId]] = []

    def add(self, message: Message) -> None:
        raise AssertionError("add must not be called")

    def list_recent_for_execution(
        self, tenant_id: TenantId, conversation_id: ConversationId, *, limit: int
    ) -> tuple[Message, ...]:
        self.list_calls.append((tenant_id, conversation_id, limit))
        return self.messages[-limit:]

    def get_for_execution(
        self, tenant_id: TenantId, conversation_id: ConversationId, message_id: MessageId
    ) -> Message | None:
        self.get_calls.append((tenant_id, conversation_id, message_id))
        return self.user_message


def make_execution(
    user_message: Message, capability: ExecutionCapability = ExecutionCapability.DIRECT_RESPONSE
) -> AssistantExecution:
    execution = AssistantExecution.create(
        execution_id=EXECUTION_ID,
        tenant_id=TENANT_ID,
        conversation_id=CONVERSATION_ID,
        user_message_id=user_message.id,
        capability=capability,
        now=NOW,
    )
    execution.start(now=NOW)
    return execution


def test_load_and_build_exact_direct_response_request_without_gateway() -> None:
    messages = (
        make_message(1, MessageRole.SYSTEM),
        make_message(2, MessageRole.USER),
        make_message(3, MessageRole.ASSISTANT),
        make_message(4, MessageRole.TOOL),
    )
    repository = FakeMessageRepository(messages, messages[1])
    execution = make_execution(messages[1])

    context = ConversationExecutionContextLoader(repository).load(execution)
    request = ModelExecutionRequestBuilder().build(execution, context)

    assert request == ModelExecutionRequest(
        tenant_id=TENANT_ID,
        execution_id=EXECUTION_ID,
        capability="direct_response",
        messages=tuple(ModelMessage(message.role.value, message.content) for message in messages),
        prompt_reference=None,
    )
    assert context.conversation_id == CONVERSATION_ID
    assert repository.list_calls == [(TENANT_ID, CONVERSATION_ID, 20)]
    assert repository.get_calls == [(TENANT_ID, CONVERSATION_ID, messages[1].id)]


def test_context_is_chronological_bounded_and_retains_user_message_once() -> None:
    user_message = make_message(1)
    recent = tuple(make_message(number) for number in range(2, 8))
    repository = FakeMessageRepository(recent, user_message)

    context = ConversationExecutionContextLoader(repository, message_limit=3).load(
        make_execution(user_message)
    )

    assert context.messages == (
        ModelMessage("user", "content 1"),
        ModelMessage("user", "content 6"),
        ModelMessage("user", "content 7"),
    )
    assert sum(message.content == "content 1" for message in context.messages) == 1


def test_user_message_already_in_window_is_not_duplicated() -> None:
    user_message = make_message(2)
    context = ConversationExecutionContextLoader(
        FakeMessageRepository((make_message(1), user_message, make_message(3)), user_message),
        message_limit=3,
    ).load(make_execution(user_message))

    assert [message.content for message in context.messages] == [
        "content 1",
        "content 2",
        "content 3",
    ]


def test_missing_scoped_user_message_raises_precise_error() -> None:
    user_message = make_message(1)
    with pytest.raises(ExecutionUserMessageNotFoundError):
        ConversationExecutionContextLoader(FakeMessageRepository((), None)).load(
            make_execution(user_message)
        )


@pytest.mark.parametrize(
    "capability",
    [
        ExecutionCapability.KNOWLEDGE_QUERY,
        ExecutionCapability.TOOL_REQUEST,
        ExecutionCapability.MEMORY_OPERATION,
        ExecutionCapability.WORKFLOW,
    ],
)
def test_unsupported_capability_raises(capability: ExecutionCapability) -> None:
    user_message = make_message(1)
    execution = make_execution(user_message, capability)
    context = ConversationExecutionContextLoader(
        FakeMessageRepository((user_message,), user_message)
    ).load(execution)

    with pytest.raises(UnsupportedExecutionCapabilityError, match=capability.value):
        ModelExecutionRequestBuilder().build(execution, context)
