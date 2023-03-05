"""create recipes

Revision ID: 334dcb49f1a9
Revises: da1176308d60
Create Date: 2023-02-22 21:58:38.113987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '334dcb49f1a9'
down_revision = 'da1176308d60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('Recepies', sa.Column('dishname', sa.String(), nullable=False, primary_key=True),
                    sa.Column('instructions',sa.String(),nullable=False),sa.Column('ingredients',sa.String(),nullable=False) )
    pass


def downgrade() -> None:
    op.drop_table('Recepies')
    pass
