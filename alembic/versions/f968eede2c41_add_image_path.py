"""add image path

Revision ID: f968eede2c41
Revises: ddc31c3281c5
Create Date: 2023-02-23 20:23:47.960561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f968eede2c41'
down_revision = 'ddc31c3281c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('Recepies',
                   sa.Column('image_path',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('Recepies','image_path')
    pass


