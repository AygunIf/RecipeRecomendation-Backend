"""change recipes table recipe_ingredients and recipe_instructions type to array

Revision ID: 0a8d0495c803
Revises: feb9c7fde48f
Create Date: 2024-06-16 11:19:00.459250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0a8d0495c803'
down_revision = 'feb9c7fde48f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('recipe_name', sa.String(length=255), nullable=True),
    sa.Column('recipe_category', sa.String(length=150), nullable=True),
    sa.Column('recipe_rating', sa.Integer(), nullable=True),
    sa.Column('calories', sa.Float(), nullable=True),
    sa.Column('fat_content', sa.Float(), nullable=True),
    sa.Column('saturated_fat_content', sa.Float(), nullable=True),
    sa.Column('cholesterol_content', sa.Float(), nullable=True),
    sa.Column('sodium_content', sa.Float(), nullable=True),
    sa.Column('carbohydrate_content', sa.Float(), nullable=True),
    sa.Column('fiber_content', sa.Float(), nullable=True),
    sa.Column('sugar_content', sa.Float(), nullable=True),
    sa.Column('protein_content', sa.Float(), nullable=True),
    sa.Column('recipe_servings', sa.Float(), nullable=True),
    sa.Column('recipe_ingredient', postgresql.ARRAY(sa.Text()), nullable=True),
    sa.Column('recipe_instructions', postgresql.ARRAY(sa.Text()), nullable=True),
    sa.Column('cooktime_min', sa.Float(), nullable=True),
    sa.Column('preptime_min', sa.Float(), nullable=True),
    sa.Column('totaltime_min', sa.Float(), nullable=True),
    sa.Column('vata_dosha_score', sa.Integer(), nullable=True),
    sa.Column('pitta_dosha_score', sa.Integer(), nullable=True),
    sa.Column('kapha_dosha_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('recipe_id')
    )
    with op.batch_alter_table('answers', schema=None) as batch_op:
        batch_op.drop_column('question_no')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_no', sa.INTEGER(), autoincrement=False, nullable=True))

    op.drop_table('recipes')
    # ### end Alembic commands ###
