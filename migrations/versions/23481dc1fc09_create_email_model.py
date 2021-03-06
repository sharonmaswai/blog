"""create email model

Revision ID: 23481dc1fc09
Revises: 64f8f4cec306
Create Date: 2019-06-03 10:30:11.395866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23481dc1fc09'
down_revision = '64f8f4cec306'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email_data', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emails')
    # ### end Alembic commands ###
