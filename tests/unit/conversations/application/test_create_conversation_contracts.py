from datetime import UTC, datetime
from uuid import uuid4

from geem_ai.conversations.application.commands import CreateConversationCommand
from geem_ai.conversations.application.results import CreateConversationResult
from geem_ai.shared.domain.actor import Actor
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


def test_create_conversation_command_preserves_authenticated_actor() -> None:
    actor = Actor.user(
        tenant_id=TenantId(uuid4()),
        user_id=UserId(uuid4()),
    )

    command = CreateConversationCommand(
        actor=actor,
        title="Consulta sobre instalación",
        language="es",
    )

    assert command.actor == actor
    assert command.title == "Consulta sobre instalación"
    assert command.language == "es"
    assert command.idempotency_key is None


def test_create_conversation_result_exposes_application_data() -> None:
    now = datetime.now(UTC)

    result = CreateConversationResult(
        conversation_id=ConversationId(uuid4()),
        title="Consulta sobre instalación",
        status="active",
        language="es",
        created_at=now,
        updated_at=now,
        version=1,
    )

    assert result.status == "active"
    assert result.language == "es"
    assert result.created_at == now
    assert result.updated_at == now
    assert result.version == 1
