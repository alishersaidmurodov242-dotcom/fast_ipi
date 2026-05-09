"""rename_content_to_body_in_posts

Revision ID: 55438254978e
Revises: 0f4dfd86c200
Create Date: 2026-05-07 17:56:17.462626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55438254978e'
down_revision: Union[str, Sequence[str], None] = '0f4dfd86c200'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.alter_column(
        'posts',
        'content',      # Eski nom
        new_column_name='body'   # Yangi nom
    )

def downgrade() -> None:
    op.alter_column(
        'posts',
        'body',
        new_column_name='content'
    )