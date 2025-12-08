"""Create phone number for user column

Revision ID: 648864403e70
Revises: 
Create Date: 2025-12-08 16:36:09.001796

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '648864403e70'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number2', sa.String(len=255), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
