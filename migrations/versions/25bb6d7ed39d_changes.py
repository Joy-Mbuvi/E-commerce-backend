"""changes

Revision ID: 25bb6d7ed39d
Revises: 1815bbe00285
Create Date: 2024-08-11 15:40:12.260788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25bb6d7ed39d'
down_revision = '1815bbe00285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favourites')
    # ### end Alembic commands ###
