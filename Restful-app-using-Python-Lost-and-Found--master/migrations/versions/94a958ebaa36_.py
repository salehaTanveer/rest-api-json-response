"""empty message

Revision ID: 94a958ebaa36
Revises: 9110110a7a31
Create Date: 2020-09-11 12:37:37.154015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a958ebaa36'
down_revision = '9110110a7a31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('Images', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'Images')
    # ### end Alembic commands ###
