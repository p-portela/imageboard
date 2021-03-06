"""empty message

Revision ID: 2abbc9b75861
Revises: 
Create Date: 2022-01-07 22:08:04.354713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2abbc9b75861'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('boardname', sa.String(length=64), nullable=True),
    sa.Column('subtitle', sa.String(length=64), nullable=True),
    sa.Column('boardpath', sa.String(length=5), nullable=True),
    sa.Column('hidden', sa.Boolean(), nullable=True),
    sa.Column('bump_limit', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('boardname'),
    sa.UniqueConstraint('boardpath')
    )
    op.create_table('op',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_op_timestamp'), 'op', ['timestamp'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('op_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['op_id'], ['op.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('quotes',
    sa.Column('quotes_id', sa.Integer(), nullable=True),
    sa.Column('quoted_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quoted_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['quotes_id'], ['post.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotes')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_op_timestamp'), table_name='op')
    op.drop_table('op')
    op.drop_table('board')
    # ### end Alembic commands ###
