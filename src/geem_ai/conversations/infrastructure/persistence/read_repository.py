from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from geem_ai.conversations.application.views import ConversationView
from geem_ai.conversations.infrastructure.persistence.models import (
    ConversationModel,
)
from geem_ai.shared.domain.ids import ConversationId, TenantId, UserId


class SQLAlchemyConversationReadRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_view(
        self,
        tenant_id: TenantId,
        conversation_id: ConversationId,
    ) -> ConversationView | None:
        statement = select(ConversationModel).where(
            ConversationModel.tenant_id == tenant_id.value,
            ConversationModel.id == conversation_id.value,
            ConversationModel.deleted_at.is_(None),
        )

        model = self._session.scalar(statement)

        if model is None:
            return None

        return ConversationView(
            conversation_id=ConversationId(model.id),
            owner_user_id=UserId(model.owner_user_id),
            title=model.title,
            status=model.status,
            language=model.language,
            created_at=model.created_at,
            updated_at=model.updated_at,
            version=model.version,
        )
