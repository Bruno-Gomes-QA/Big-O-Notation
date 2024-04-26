from alembic import op
import sqlalchemy as sa
import datetime


revision = 'Init Migrate'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('department', sa.String(length=120), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False, default=datetime.datetime.utcnow),
        sa.Column('updated', sa.DateTime(), nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('variable_weight', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )

def downgrade():
    op.drop_table('products')