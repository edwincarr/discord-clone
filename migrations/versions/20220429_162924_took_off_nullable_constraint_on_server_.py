"""took off nullable constraint on server table

Revision ID: 567bd5a45b23
Revises: f9af2ec6526a
Create Date: 2022-04-29 16:29:24.133582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '567bd5a45b23'
down_revision = 'f9af2ec6526a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('channels_server2_id_fkey', 'channels', type_='foreignkey')
    op.drop_column('channels', 'server2_id')
    op.alter_column('servers', 'invite_url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('servers', 'invite_url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('channels', sa.Column('server2_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('channels_server2_id_fkey', 'channels', 'servers', ['server2_id'], ['id'])
    # ### end Alembic commands ###
