"""change score column type from integer to float

Revision ID: b1a9f5723142
Revises: 59c27f61b918
Create Date: 2024-06-21 01:05:38.655551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1a9f5723142'
down_revision = '59c27f61b918'
branch_labels = None
depends_on = None



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('score',
               existing_type=sa.Integer,
               type_=sa.Float,
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('score',
               existing_type=sa.Float,
               type_=sa.Integer,
               existing_nullable=True)
    # ### end Alembic commands ###