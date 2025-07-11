"""Create phone number for user column

Revision ID: dda3339b3d47
Revises: 
Create Date: 2025-07-08 03:14:52.915016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dda3339b3d47'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))

def downgrade() -> None:
    op.drop_column('users',"phone_number")