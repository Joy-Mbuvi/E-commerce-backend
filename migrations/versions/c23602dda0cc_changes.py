"""changes

Revision ID: c23602dda0cc
Revises: b403039e2b27
Create Date: 2024-08-07 14:57:04.081133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c23602dda0cc'
down_revision = 'b403039e2b27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'image_url',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=4000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'image_url',
               existing_type=sa.String(length=4000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    # ### end Alembic commands ###
