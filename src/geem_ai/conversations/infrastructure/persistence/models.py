from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import cast
from uuid import UUID

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKeyConstraint,
    Index,
    Integer,
    Numeric,
    String,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from geem_ai.shared.infrastructure.persistence.database import Base


class ConversationModel(Base):
    __tablename__ = "conversations"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
    )
    tenant_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=False,
    )
    owner_user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        String(160),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    language: Mapped[str] = mapped_column(
        String(8),
        nullable=False,
        server_default="es",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    last_message_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        server_default="1",
    )

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "id",
            name="uq_conversations__tenant_id_id",
        ),
        CheckConstraint(
            "status IN ('active', 'archived', 'locked', 'deleted')",
            name="ck_conversations__status",
        ),
        CheckConstraint(
            "language IN ('es', 'en')",
            name="ck_conversations__language",
        ),
        Index(
            "ix_conversations__tenant_owner_updated",
            "tenant_id",
            "owner_user_id",
            text("updated_at DESC"),
            text("id DESC"),
            postgresql_where=text("deleted_at IS NULL"),
        ),
        Index(
            "ix_conversations__tenant_status",
            "tenant_id",
            "status",
        ),
    )


class MessageModel(Base):
    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
    )
    tenant_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=False,
    )
    conversation_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=False,
    )
    author_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    author_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=True,
    )
    role: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    execution_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=True,
    )
    metadata_json: Mapped[dict[str, object]] = mapped_column(
        "metadata",
        JSONB,
        nullable=False,
        default=dict,
        server_default=text("'{}'::jsonb"),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "id",
            name="uq_messages__tenant_id_id",
        ),
        ForeignKeyConstraint(
            ["tenant_id", "conversation_id"],
            ["conversations.tenant_id", "conversations.id"],
            name="fk_messages__conversation_tenant",
        ),
        CheckConstraint(
            "author_type IN ('user', 'assistant', 'system', 'tool')",
            name="ck_messages__author_type",
        ),
        CheckConstraint(
            "role IN ('user', 'assistant', 'system', 'tool')",
            name="ck_messages__role",
        ),
        CheckConstraint(
            ("status IN ('pending', 'streaming', 'completed', 'failed', 'cancelled', 'redacted')"),
            name="ck_messages__status",
        ),
        Index(
            "ix_messages__tenant_conversation_created",
            "tenant_id",
            "conversation_id",
            "created_at",
            "id",
        ),
    )


class AssistantExecutionModel(Base):
    __tablename__ = "assistant_executions"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
    )
    tenant_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=False,
    )
    conversation_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=False,
    )
    user_message_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=True,
    )
    assistant_message_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )
    capability: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )

    prompt_key: Mapped[str | None] = mapped_column(
        String(160),
        nullable=True,
    )
    prompt_version: Mapped[str | None] = mapped_column(
        String(40),
        nullable=True,
    )
    prompt_checksum: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
    )

    provider: Mapped[str | None] = mapped_column(
        String(80),
        nullable=True,
    )
    model: Mapped[str | None] = mapped_column(
        String(160),
        nullable=True,
    )
    routing_policy_version: Mapped[str | None] = mapped_column(
        String(40),
        nullable=True,
    )
    fallback_used: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    input_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    output_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    cached_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    reasoning_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    total_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)

    cost_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 8),
        nullable=True,
    )
    cost_currency: Mapped[str | None] = mapped_column(
        String(3),
        nullable=True,
    )
    latency_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

    failure_code: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
    )
    failure_detail: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        server_default="1",
    )

    __table_args__ = (
        ForeignKeyConstraint(
            ["tenant_id", "conversation_id"],
            ["conversations.tenant_id", "conversations.id"],
            name="fk_assistant_executions__conversation_tenant",
        ),
        CheckConstraint(
            (
                "status IN "
                "('created', 'running', 'waiting_for_approval', "
                "'completed', 'failed', 'cancelled', 'timed_out')"
            ),
            name="ck_assistant_executions__status",
        ),
        CheckConstraint(
            (
                "capability IN "
                "('direct_response', 'knowledge_query', 'tool_request', "
                "'memory_operation', 'workflow')"
            ),
            name="ck_assistant_executions__capability",
        ),
        CheckConstraint(
            (
                "COALESCE(input_tokens, 0) >= 0 AND "
                "COALESCE(output_tokens, 0) >= 0 AND "
                "COALESCE(cached_tokens, 0) >= 0 AND "
                "COALESCE(reasoning_tokens, 0) >= 0 AND "
                "COALESCE(total_tokens, 0) >= 0"
            ),
            name="ck_assistant_executions__token_values",
        ),
        CheckConstraint(
            "cost_amount IS NULL OR cost_amount >= 0",
            name="ck_assistant_executions__cost",
        ),
        CheckConstraint(
            "latency_ms IS NULL OR latency_ms >= 0",
            name="ck_assistant_executions__latency",
        ),
        Index(
            "ix_assistant_executions__tenant_conversation_created",
            "tenant_id",
            "conversation_id",
            text("created_at DESC"),
        ),
        Index(
            "ix_assistant_executions__tenant_status",
            "tenant_id",
            "status",
        ),
        Index(
            "ix_assistant_executions__created_running",
            "created_at",
            postgresql_where=text("status IN ('created', 'running', 'waiting_for_approval')"),
        ),
    )


message_table = cast(Table, MessageModel.__table__)

message_table.append_constraint(
    ForeignKeyConstraint(
        ["execution_id"],
        ["assistant_executions.id"],
        name="fk_messages__assistant_executions",
    )
)
