"""Enable pgvector extension.

Revision ID: 0133d60c5d23
Revises: 203f33c87712
Create Date: 2026-07-26 05:22:49.127313
"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0133d60c5d23"
down_revision: str | Sequence[str] | None = "203f33c87712"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Enable the pgvector PostgreSQL extension."""
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")


def downgrade() -> None:
    """Disable the pgvector PostgreSQL extension."""
    op.execute("DROP EXTENSION IF EXISTS vector")
