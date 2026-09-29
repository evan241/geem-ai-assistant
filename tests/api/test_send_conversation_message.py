from uuid import UUID

import pytest
from apps.api.dependencies.auth import get_actor
from apps.api.dependencies.conversations import get_send_conversation_message_handler
from apps.api.main import create_app
from fastapi.testclient import TestClient

from geem_ai.conversations.application.commands import SendConversationMessageCommand
from geem_ai.conversations.application.exceptions import (
    ConversationNotFoundError,
    IdempotencyKeyConflictError,
    IdempotencyRequestInProgressError,
    InvalidIdempotencyKeyError,
)
from geem_ai.conversations.application.results import SendConversationMessageResult
from geem_ai.conversations.domain.exceptions import (
    ConversationNotActiveError,
    InvalidMessageContentError,
)
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ExecutionId, MessageId, TenantId, UserId

CONVERSATION_ID = UUID("30000000-0000-0000-0000-000000000001")
USER_MESSAGE_ID = MessageId(UUID("40000000-0000-0000-0000-000000000001"))
EXECUTION_ID = ExecutionId(UUID("50000000-0000-0000-0000-000000000001"))


class FakeSendConversationMessageHandler:
    def __init__(self, error: Exception | None = None) -> None:
        self.commands: list[SendConversationMessageCommand] = []
        self.error = error

    def handle(self, command: SendConversationMessageCommand) -> SendConversationMessageResult:
        self.commands.append(command)
        if self.error is not None:
            raise self.error
        return SendConversationMessageResult(
            user_message_id=USER_MESSAGE_ID,
            assistant_execution_id=EXECUTION_ID,
            execution_status="created",
            capability="direct_response",
        )


def build_client(
    handler: FakeSendConversationMessageHandler,
) -> tuple[TestClient, Actor]:
    actor = Actor.user(
        tenant_id=TenantId(UUID("10000000-0000-0000-0000-000000000001")),
        user_id=UserId(UUID("20000000-0000-0000-0000-000000000001")),
    )
    app = create_app()
    app.dependency_overrides[get_actor] = lambda: actor
    app.dependency_overrides[get_send_conversation_message_handler] = lambda: handler
    return TestClient(app), actor


def test_send_message_accepts_request_and_wires_command() -> None:
    handler = FakeSendConversationMessageHandler()
    client, actor = build_client(handler)

    with client:
        response = client.post(
            f"/api/v1/conversations/{CONVERSATION_ID}/messages",
            headers={"Idempotency-Key": "exact-key"},
            json={
                "content": "  Preserve this content  ",
                "response_mode": "stream",
                "capability_hint": "direct_response",
            },
        )

    assert response.status_code == 202
    assert response.json() == {
        "user_message_id": str(USER_MESSAGE_ID.value),
        "assistant_execution_id": str(EXECUTION_ID.value),
        "execution_status": "created",
        "capability": "direct_response",
    }
    assert handler.commands == [
        SendConversationMessageCommand(
            actor=actor,
            conversation_id=handler.commands[0].conversation_id,
            content="  Preserve this content  ",
            capability_hint="direct_response",
            idempotency_key="exact-key",
        )
    ]
    assert handler.commands[0].conversation_id.value == CONVERSATION_ID


@pytest.mark.parametrize(
    ("path", "headers", "body"),
    [
        (str(CONVERSATION_ID), {}, {"content": "hello"}),
        ("not-a-uuid", {"Idempotency-Key": "key"}, {"content": "hello"}),
        (
            str(CONVERSATION_ID),
            {"Idempotency-Key": "key"},
            {"content": "hello", "capability_hint": "knowledge_query"},
        ),
        (
            str(CONVERSATION_ID),
            {"Idempotency-Key": "key"},
            {"content": "hello", "response_mode": "blocking"},
        ),
    ],
)
def test_send_message_rejects_invalid_http_contract_without_calling_handler(
    path: str,
    headers: dict[str, str],
    body: dict[str, str],
) -> None:
    handler = FakeSendConversationMessageHandler()
    client, _ = build_client(handler)

    with client:
        response = client.post(f"/api/v1/conversations/{path}/messages", headers=headers, json=body)

    assert response.status_code == 422
    assert handler.commands == []


@pytest.mark.parametrize(
    ("error", "expected_status", "expected_detail"),
    [
        (ConversationNotFoundError(), 404, "Conversation not found."),
        (ConversationNotActiveError(), 409, "Conversation is not active."),
        (InvalidMessageContentError(), 422, "Message content is invalid."),
        (InvalidIdempotencyKeyError(), 422, "Idempotency key is invalid."),
        (IdempotencyKeyConflictError(), 409, "Idempotency key conflicts with another request."),
        (
            IdempotencyRequestInProgressError(),
            409,
            "A request with this idempotency key is still processing.",
        ),
    ],
)
def test_send_message_maps_application_errors(
    error: Exception,
    expected_status: int,
    expected_detail: str,
) -> None:
    handler = FakeSendConversationMessageHandler(error)
    client, _ = build_client(handler)

    with client:
        response = client.post(
            f"/api/v1/conversations/{CONVERSATION_ID}/messages",
            headers={"Idempotency-Key": "key"},
            json={"content": "hello"},
        )

    assert response.status_code == expected_status
    assert response.json() == {"detail": expected_detail}


def test_send_message_replay_returns_same_acceptance_response() -> None:
    handler = FakeSendConversationMessageHandler()
    client, _ = build_client(handler)
    request = {
        "headers": {"Idempotency-Key": "replayed-key"},
        "json": {"content": "hello"},
    }

    with client:
        first = client.post(f"/api/v1/conversations/{CONVERSATION_ID}/messages", **request)
        replay = client.post(f"/api/v1/conversations/{CONVERSATION_ID}/messages", **request)

    assert first.status_code == replay.status_code == 202
    assert first.json() == replay.json()


def test_send_message_contract_is_in_openapi() -> None:
    app = create_app()
    operation = app.openapi()["paths"]["/api/v1/conversations/{conversation_id}/messages"]["post"]

    idempotency_header = next(
        parameter for parameter in operation["parameters"] if parameter["name"] == "Idempotency-Key"
    )
    assert idempotency_header["required"] is True
    assert idempotency_header["schema"]["minLength"] == 1
    assert idempotency_header["schema"]["maxLength"] == 255
    assert operation["requestBody"]["required"] is True
    assert "202" in operation["responses"]
    assert operation["responses"]["202"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/SendConversationMessageResponse"
    }
