from __future__ import annotations

from datetime import datetime
from typing import cast
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from geem_ai.conversations.application.idempotency import (
    IdempotencyRecord,
    IdempotencyStatus,
)
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
    IdempotencyRecordModel,
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


class SQLAlchemyIdempotencyRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, tenant_id: TenantId, scope: str, key: str) -> IdempotencyRecord | None:
        model = self._session.scalar(
            select(IdempotencyRecordModel).where(
                IdempotencyRecordModel.tenant_id == tenant_id.value,
                IdempotencyRecordModel.scope == scope,
                IdempotencyRecordModel.idempotency_key == key,
            )
        )
        return None if model is None else self._to_record(model)

    def reserve(self, record: IdempotencyRecord) -> bool:
        statement = (
            insert(IdempotencyRecordModel)
            .values(**self._values(record))
            .on_conflict_do_nothing(index_elements=["tenant_id", "scope", "idempotency_key"])
        )
        result = self._session.execute(statement)
        return result.rowcount == 1

    def complete(
        self,
        record: IdempotencyRecord,
        *,
        response_status: int,
        response_body: dict[str, object],
        resource_type: str,
        resource_id: UUID,
        completed_at: datetime,
    ) -> None:
        record.status = "completed"
        record.response_status = response_status
        record.response_body = response_body
        record.resource_type = resource_type
        record.resource_id = resource_id
        record.completed_at = completed_at
        self._session.execute(
            update(IdempotencyRecordModel)
            .where(
                IdempotencyRecordModel.id == record.id,
                IdempotencyRecordModel.tenant_id == record.tenant_id,
            )
            .values(
                status="completed",
                response_status=response_status,
                response_body=response_body,
                resource_type=resource_type,
                resource_id=resource_id,
                completed_at=completed_at,
            )
        )

    @staticmethod
    def _values(record: IdempotencyRecord) -> dict[str, object]:
        return {
            "id": record.id,
            "tenant_id": record.tenant_id,
            "scope": record.scope,
            "idempotency_key": record.idempotency_key,
            "request_hash": record.request_hash,
            "status": record.status,
            "response_status": record.response_status,
            "response_body": record.response_body,
            "resource_type": record.resource_type,
            "resource_id": record.resource_id,
            "created_at": record.created_at,
            "completed_at": record.completed_at,
            "expires_at": record.expires_at,
        }

    @staticmethod
    def _to_record(model: IdempotencyRecordModel) -> IdempotencyRecord:
        return IdempotencyRecord(
            id=model.id,
            tenant_id=model.tenant_id,
            scope=model.scope,
            idempotency_key=model.idempotency_key,
            request_hash=model.request_hash,
            status=cast(IdempotencyStatus, model.status),
            response_status=model.response_status,
            response_body=model.response_body,
            resource_type=model.resource_type,
            resource_id=model.resource_id,
            created_at=model.created_at,
            completed_at=model.completed_at,
            expires_at=model.expires_at,
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
