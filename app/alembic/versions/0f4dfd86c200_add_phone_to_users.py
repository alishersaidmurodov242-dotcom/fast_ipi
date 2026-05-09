"""add_phone_to_users

Revision ID: 0f4dfd86c200
Revises: 85183ea311bd
Create Date: 2026-05-07 17:44:16.113540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f4dfd86c200'
down_revision: Union[str, Sequence[str], None] = '85183ea311bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('phone', sa.String(20), nullable=True)
    )
    # Index ham qo'shamiz:
    op.create_index(
        'ix_users_phone',
        'users',
        ['phone'],
        unique=False
    )

def downgrade() -> None:
    op.drop_index('ix_users_phone', table_name='users')
    op.drop_column('users', 'phone')