"""empty message

Revision ID: 370b9ebf9ff3
Revises: 3cb9a6f8d713
Create Date: 2022-08-01 12:40:31.815766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '370b9ebf9ff3'
down_revision = '3cb9a6f8d713'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('phone_number', sa.Unicode(length=255), nullable=True))
    op.add_column('Artist', sa.Column('phone_country_code', sa.Unicode(length=8), nullable=True))
    op.drop_column('Artist', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'phone_country_code')
    op.drop_column('Artist', 'phone_number')
    # ### end Alembic commands ###