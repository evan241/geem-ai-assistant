from __future__ import annotations

from collections.abc import Callable
from datetime import datetime

from geem_ai.conversations.application.commands import CreateConversationCommand
from geem_ai.conversations.application.ports.unit_of_work import (
    ConversationUnitOfWorkFactory,
)
from geem_ai.conversations.application.results import CreateConversationResult
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.shared.domain.ids import ConversationId


class CreateConversationHandler:
    def __init__(
        self,
        *,
        unit_of_work_factory: ConversationUnitOfWorkFactory,
        conversation_id_factory: Callable[[], ConversationId],
        clock: Callable[[], datetime],
    ) -> None:
        self._unit_of_work_factory = unit_of_work_factory
        self._conversation_id_factory = conversation_id_factory
        self._clock = clock

    def handle(
        self,
        command: CreateConversationCommand,
    ) -> CreateConversationResult:
        if command.actor.user_id is None:
            raise ValueError("User actor is required to create a conversation.")

        now = self._clock()

        conversation = Conversation.create(
            conversation_id=self._conversation_id_factory(),
            tenant_id=command.actor.tenant_id,
            owner_user_id=command.actor.user_id,
            title=command.title or "",
            language=command.language,
            now=now,
        )

        with self._unit_of_work_factory.create(command.actor) as unit_of_work:
            unit_of_work.conversations.add(conversation)
            unit_of_work.commit()

        return CreateConversationResult(
            conversation_id=conversation.id,
            title=conversation.title,
            status=conversation.status.value,
            language=conversation.language.value,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            version=conversation.version,
        )
