"""empty message

Revision ID: 171ed23fc4b3
Revises: 94a958ebaa36
Create Date: 2020-09-11 14:57:55.601600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '171ed23fc4b3'
down_revision = '94a958ebaa36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'user_id')
    # ### end Alembic commands ###