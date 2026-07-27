from typing import cast

from sqlalchemy import (
    CheckConstraint,
    ForeignKeyConstraint,
    Index,
    Table,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID

from geem_ai.conversations.infrastructure.persistence.models import (
    AssistantExecutionModel,
    ConversationModel,
    MessageModel,
)


def test_conversation_model_matches_persistence_contract() -> None:
    table = cast(Table, ConversationModel.__table__)

    assert table.name == "conversations"

    assert isinstance(table.c.id.type, UUID)
    assert isinstance(table.c.tenant_id.type, UUID)
    assert isinstance(table.c.owner_user_id.type, UUID)

    assert table.c.id.nullable is False
    assert table.c.tenant_id.nullable is False
    assert table.c.owner_user_id.nullable is False
    assert table.c.title.nullable is False
    assert table.c.status.nullable is False
    assert table.c.language.nullable is False
    assert table.c.version.nullable is False

    unique_constraints = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, UniqueConstraint)
    }
    assert "uq_conversations__tenant_id_id" in unique_constraints

    check_constraints = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, CheckConstraint)
    }
    assert "ck_conversations__status" in check_constraints
    assert "ck_conversations__language" in check_constraints

    indexes = {index.name for index in table.indexes if isinstance(index, Index)}
    assert "ix_conversations__tenant_owner_updated" in indexes
    assert "ix_conversations__tenant_status" in indexes


def test_message_model_matches_persistence_contract() -> None:
    table = cast(Table, MessageModel.__table__)

    assert table.name == "messages"

    assert isinstance(table.c.id.type, UUID)
    assert isinstance(table.c.tenant_id.type, UUID)
    assert isinstance(table.c.conversation_id.type, UUID)
    assert isinstance(table.c.metadata.type, JSONB)

    unique_constraints = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, UniqueConstraint)
    }
    assert "uq_messages__tenant_id_id" in unique_constraints

    check_constraints = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, CheckConstraint)
    }
    assert "ck_messages__author_type" in check_constraints
    assert "ck_messages__role" in check_constraints
    assert "ck_messages__status" in check_constraints

    foreign_keys = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, ForeignKeyConstraint)
    }
    assert "fk_messages__conversation_tenant" in foreign_keys
    assert "fk_messages__assistant_executions" in foreign_keys

    indexes = {index.name for index in table.indexes if isinstance(index, Index)}
    assert "ix_messages__tenant_conversation_created" in indexes


def test_assistant_execution_model_matches_persistence_contract() -> None:
    table = cast(Table, AssistantExecutionModel.__table__)

    assert table.name == "assistant_executions"

    assert isinstance(table.c.id.type, UUID)
    assert isinstance(table.c.tenant_id.type, UUID)
    assert isinstance(table.c.conversation_id.type, UUID)

    assert table.c.status.nullable is False
    assert table.c.capability.nullable is False
    assert table.c.fallback_used.nullable is False
    assert table.c.version.nullable is False

    check_constraints = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, CheckConstraint)
    }
    assert "ck_assistant_executions__status" in check_constraints
    assert "ck_assistant_executions__capability" in check_constraints
    assert "ck_assistant_executions__token_values" in check_constraints
    assert "ck_assistant_executions__cost" in check_constraints
    assert "ck_assistant_executions__latency" in check_constraints

    foreign_keys = {
        constraint.name
        for constraint in table.constraints
        if isinstance(constraint, ForeignKeyConstraint)
    }

    assert "fk_assistant_executions__conversation_tenant" in foreign_keys

    indexes = {index.name for index in table.indexes if isinstance(index, Index)}
    assert "ix_assistant_executions__tenant_conversation_created" in indexes
    assert "ix_assistant_executions__tenant_status" in indexes
    assert "ix_assistant_executions__created_running" in indexes
