from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import (
    ConversationLanguage,
    ConversationStatus,
)
from geem_ai.conversations.infrastructure.persistence.models import ConversationModel
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


class SQLAlchemyConversationRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, conversation: Conversation) -> None:
        model = ConversationModel(
            id=conversation.id.value,
            tenant_id=conversation.tenant_id.value,
            owner_user_id=conversation.owner_user_id.value,
            title=conversation.title,
            status=conversation.status.value,
            language=conversation.language.value,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            last_message_at=conversation.last_message_at,
            deleted_at=None,
            version=conversation.version,
        )

        self._session.add(model)

    def get_by_id(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> Conversation | None:
        statement = select(ConversationModel).where(
            ConversationModel.tenant_id == tenant_id.value,
            ConversationModel.id == conversation_id.value,
            ConversationModel.deleted_at.is_(None),
        )

        model = self._session.scalar(statement)

        if model is None:
            return None

        return self._to_domain(model)

    def exists(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> bool:
        statement = select(ConversationModel.id).where(
            ConversationModel.tenant_id == tenant_id.value,
            ConversationModel.id == conversation_id.value,
            ConversationModel.deleted_at.is_(None),
        )

        return self._session.scalar(statement) is not None

    @staticmethod
    def _to_domain(model: ConversationModel) -> Conversation:
        return Conversation(
            id=ConversationId(model.id),
            tenant_id=TenantId(model.tenant_id),
            owner_user_id=UserId(model.owner_user_id),
            title=model.title,
            status=ConversationStatus(model.status),
            language=ConversationLanguage(model.language),
            created_at=model.created_at,
            updated_at=model.updated_at,
            last_message_at=model.last_message_at,
            version=model.version,
        )
