"""v3

Revision ID: 83da2c92516e
Revises: d20ab23449b6
Create Date: 2023-04-12 03:24:33.837174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83da2c92516e'
down_revision = 'd20ab23449b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('master', 'user_id', new_column_name='user')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('master', 'user', new_column_name='user_id')
    # ### end Alembic commands ###
