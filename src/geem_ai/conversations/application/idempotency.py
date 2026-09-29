from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from typing import Final, Literal
from uuid import UUID

from geem_ai.conversations.application.results import SendConversationMessageResult
from geem_ai.shared.domain.ids import ConversationId, ExecutionId, MessageId

SEND_MESSAGE_IDEMPOTENCY_SCOPE: Final = "conversations.send-message"
IDEMPOTENCY_TTL_HOURS: Final = 24
IdempotencyStatus = Literal["processing", "completed", "failed"]


@dataclass(slots=True)
class IdempotencyRecord:
    id: UUID
    tenant_id: UUID
    scope: str
    idempotency_key: str
    request_hash: str
    status: IdempotencyStatus
    response_status: int | None
    response_body: dict[str, object] | None
    resource_type: str | None
    resource_id: UUID | None
    created_at: datetime
    completed_at: datetime | None
    expires_at: datetime


def send_message_request_hash(
    *, conversation_id: ConversationId, content: str, capability: str
) -> str:
    payload = {
        "capability": capability,
        "content": content,
        "conversation_id": str(conversation_id.value),
    }
    canonical = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def serialize_send_message_result(result: SendConversationMessageResult) -> dict[str, object]:
    return {
        "assistant_execution_id": str(result.assistant_execution_id.value),
        "capability": result.capability,
        "execution_status": result.execution_status,
        "user_message_id": str(result.user_message_id.value),
    }


def deserialize_send_message_result(body: dict[str, object]) -> SendConversationMessageResult:
    try:
        return SendConversationMessageResult(
            user_message_id=MessageId(UUID(str(body["user_message_id"]))),
            assistant_execution_id=ExecutionId(UUID(str(body["assistant_execution_id"]))),
            execution_status=str(body["execution_status"]),
            capability=str(body["capability"]),
        )
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("Stored idempotency response is invalid.") from error
