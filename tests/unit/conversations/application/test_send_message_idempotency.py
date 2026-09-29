from uuid import UUID

from geem_ai.conversations.application.idempotency import send_message_request_hash
from geem_ai.shared.domain.ids import ConversationId


def test_request_hash_is_deterministic_and_preserves_content_exactly() -> None:
    conversation_id = ConversationId(UUID("10000000-0000-0000-0000-000000000001"))
    arguments = {
        "conversation_id": conversation_id,
        "content": "  café  ",
        "capability": "direct_response",
    }
    first = send_message_request_hash(**arguments)

    assert first == send_message_request_hash(**arguments)
    assert len(first) == 64
    assert first != send_message_request_hash(**{**arguments, "content": "café"})
    assert first != send_message_request_hash(
        **{**arguments, "conversation_id": ConversationId(UUID(int=2))}
    )
    assert first != send_message_request_hash(**{**arguments, "capability": "knowledge_query"})
