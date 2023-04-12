"""v4

Revision ID: ea7d54d53eef
Revises: 83da2c92516e
Create Date: 2023-04-12 03:38:49.947770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea7d54d53eef'
down_revision = '83da2c92516e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('master', 'user', new_column_name='user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('master', 'user_id', new_column_name='user')

    # ### end Alembic commands ###