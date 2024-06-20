"""author_name image_url and nutriscore properties added

Revision ID: f1806e392a59
Revises: 0a8d0495c803
Create Date: 2024-06-21 00:31:50.583137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1806e392a59'
down_revision = '0a8d0495c803'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_name', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('score', sa.Integer(), nullable=True))
        batch_op.drop_column('prep_time')
        batch_op.drop_column('total_time')
        batch_op.drop_column('cook_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cook_time', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('total_time', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('prep_time', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_column('score')
        batch_op.drop_column('image_url')
        batch_op.drop_column('author_name')

    # ### end Alembic commands ###