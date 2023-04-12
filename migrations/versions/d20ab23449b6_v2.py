"""v2

Revision ID: d20ab23449b6
Revises: 7466f651543d
Create Date: 2023-04-12 03:15:45.730147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd20ab23449b6'
down_revision = '7466f651543d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('master', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('master', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)

    # ### end Alembic commands ###