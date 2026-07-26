"""Initial database baseline.

Revision ID: 203f33c87712
Revises:
Create Date: 2026-07-26 05:06:10.811319
"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "203f33c87712"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Establish the initial database migration baseline."""


def downgrade() -> None:
    """Return the database to the pre-baseline state."""
