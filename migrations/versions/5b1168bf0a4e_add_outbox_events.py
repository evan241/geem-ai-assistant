"""add outbox events

Revision ID: 5b1168bf0a4e
Revises: b65a4cb9c3af
Create Date: 2026-09-29 00:00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "5b1168bf0a4e"
down_revision: str | Sequence[str] | None = "b65a4cb9c3af"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "outbox_events",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("tenant_id", sa.UUID(), nullable=True),
        sa.Column("event_type", sa.String(length=200), nullable=False),
        sa.Column("event_version", sa.Integer(), nullable=False),
        sa.Column("aggregate_type", sa.String(length=100), nullable=False),
        sa.Column("aggregate_id", sa.UUID(), nullable=False),
        sa.Column("correlation_id", sa.String(length=160), nullable=True),
        sa.Column("causation_id", sa.String(length=160), nullable=True),
        sa.Column("payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("status", sa.String(length=32), server_default="pending", nullable=False),
        sa.Column("attempt", sa.Integer(), server_default="0", nullable=False),
        sa.Column("available_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_error", sa.Text(), nullable=True),
        sa.CheckConstraint("attempt >= 0", name="ck_outbox_events__attempt"),
        sa.CheckConstraint(
            "status IN ('pending', 'publishing', 'published', 'failed', 'dead_letter')",
            name="ck_outbox_events__status",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_outbox_events")),
    )
    op.create_index(
        "ix_outbox_events__pending_available",
        "outbox_events",
        ["available_at", "created_at"],
        unique=False,
        postgresql_where=sa.text("status IN ('pending', 'failed')"),
    )


def downgrade() -> None:
    op.drop_index("ix_outbox_events__pending_available", table_name="outbox_events")
    op.drop_table("outbox_events")
