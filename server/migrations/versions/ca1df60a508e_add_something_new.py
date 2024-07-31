"""add something new

Revision ID: ca1df60a508e
Revises: 84e81ea4624d
Create Date: 2024-07-31 10:45:59.134648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca1df60a508e'
down_revision = '84e81ea4624d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('delis_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('some_new_column', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('delis_table', schema=None) as batch_op:
        batch_op.drop_column('some_new_column')

    # ### end Alembic commands ###