"""Initial DB

Revision ID: be74f2476e82
Revises: 
Create Date: 2019-12-18 22:20:08.092663

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'be74f2476e82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cart',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_cart'))
                    )
    op.create_table('product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.Text(), nullable=True),
                    sa.Column('value', sa.Float(), nullable=True),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
                    )
    op.create_table('cart_product',
                    sa.Column('cart_id', sa.Integer(), nullable=True),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], name=op.f('fk_cart_product_cart_id_cart')),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'],
                                            name=op.f('fk_cart_product_product_id_product'))
                    )


def downgrade():
    op.drop_table('cart_product')
    op.drop_table('product')
    op.drop_table('cart')
