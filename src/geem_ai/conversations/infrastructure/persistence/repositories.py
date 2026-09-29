from __future__ import annotations

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from geem_ai.conversations.domain.assistant_execution import AssistantExecution
from geem_ai.conversations.domain.conversation import Conversation
from geem_ai.conversations.domain.enums import (
    ConversationLanguage,
    ConversationStatus,
)
from geem_ai.conversations.domain.message import Message
from geem_ai.conversations.infrastructure.persistence.models import (
    AssistantExecutionModel,
    ConversationModel,
    MessageModel,
)
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

    def save(self, conversation: Conversation) -> None:
        statement = (
            update(ConversationModel)
            .where(
                ConversationModel.tenant_id == conversation.tenant_id.value,
                ConversationModel.id == conversation.id.value,
                ConversationModel.deleted_at.is_(None),
            )
            .values(
                updated_at=conversation.updated_at,
                last_message_at=conversation.last_message_at,
                version=conversation.version,
            )
        )
        self._session.execute(statement)

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


class SQLAlchemyMessageRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, message: Message) -> None:
        model = MessageModel(
            id=message.id.value,
            tenant_id=message.tenant_id.value,
            conversation_id=message.conversation_id.value,
            author_type=message.role.value,
            author_id=message.author_id.value if message.author_id is not None else None,
            role=message.role.value,
            content=message.content,
            status=message.status.value,
            execution_id=(message.execution_id.value if message.execution_id is not None else None),
            metadata_json={},
            created_at=message.created_at,
            completed_at=message.completed_at,
        )
        self._session.add(model)


class SQLAlchemyAssistantExecutionRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, execution: AssistantExecution) -> None:
        model = AssistantExecutionModel(
            id=execution.id.value,
            tenant_id=execution.tenant_id.value,
            conversation_id=execution.conversation_id.value,
            user_message_id=execution.user_message_id.value,
            assistant_message_id=(
                execution.assistant_message_id.value
                if execution.assistant_message_id is not None
                else None
            ),
            status=execution.status.value,
            capability=execution.capability.value,
            provider=execution.provider,
            model=execution.model,
            input_tokens=execution.input_tokens,
            output_tokens=execution.output_tokens,
            total_tokens=execution.total_tokens,
            cost_amount=execution.cost_amount,
            latency_ms=execution.latency_ms,
            failure_code=execution.failure_code,
            failure_detail=execution.failure_detail,
            started_at=execution.started_at,
            completed_at=execution.completed_at,
            created_at=execution.created_at,
            updated_at=execution.updated_at,
        )
        self._session.add(model)
