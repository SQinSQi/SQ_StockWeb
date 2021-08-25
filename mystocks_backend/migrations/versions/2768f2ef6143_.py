"""empty message

Revision ID: 2768f2ef6143
Revises: 
Create Date: 2021-08-24 23:38:19.568918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2768f2ef6143'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False, auto_increment=True),
    sa.Column('number', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('price', sa.Float(precision=10), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('buy_price', sa.Float(precision=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('stock')
    # ### end Alembic commands ###
