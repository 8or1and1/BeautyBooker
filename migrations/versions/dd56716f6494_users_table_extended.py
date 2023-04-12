"""users table extended

Revision ID: dd56716f6494
Revises: 43ae4cc565e6
Create Date: 2023-04-12 02:44:44.653120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd56716f6494'
down_revision = '43ae4cc565e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('surname', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('surname')
        batch_op.drop_column('name')

    # ### end Alembic commands ###