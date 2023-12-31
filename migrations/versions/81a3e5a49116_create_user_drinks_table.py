"""Create user_drinks table

Revision ID: 81a3e5a49116
Revises: 3aa817230f57
Create Date: 2023-10-15 10:32:33.951454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81a3e5a49116'
down_revision = '3aa817230f57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_drinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('drink_type', sa.String(length=64), nullable=True),
    sa.Column('drink_size', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_drinks')
    # ### end Alembic commands ###
