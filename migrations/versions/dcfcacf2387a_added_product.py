"""added product

Revision ID: dcfcacf2387a
Revises: cbcd1d8175d4
Create Date: 2024-08-05 20:02:10.923901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcfcacf2387a'
down_revision = 'cbcd1d8175d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'cart', 'product', ['product_id'], ['id'])
    op.create_foreign_key(None, 'productimage', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'productimage', type_='foreignkey')
    op.drop_constraint(None, 'cart', type_='foreignkey')
    op.drop_table('product')
    # ### end Alembic commands ###
