"""empty message

Revision ID: c31ee42f6bb5
Revises: 00e9a5723531
Create Date: 2020-09-23 12:16:01.790884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31ee42f6bb5'
down_revision = '00e9a5723531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('msg_read', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'msg_read')
    # ### end Alembic commands ###
