"""rename_content_to_body_in_posts

Revision ID: e4c617b9406b
Revises: 55438254978e
Create Date: 2026-05-08 15:52:22.437099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4c617b9406b'
down_revision: Union[str, Sequence[str], None] = '55438254978e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
