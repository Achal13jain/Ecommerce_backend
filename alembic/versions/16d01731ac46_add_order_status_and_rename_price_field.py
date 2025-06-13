"""Add order status and rename price field

Revision ID: 16d01731ac46
Revises: df403ae33600
Create Date: 2025-06-13 13:07:14.608824

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16d01731ac46'
down_revision: Union[str, None] = 'df403ae33600'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

order_status_enum = sa.Enum(
    "pending", "paid", "cancelled", name="orderstatus"
)

def upgrade() -> None:
    """Upgrade schema to add order status and rename price field."""

    order_status_enum.create(op.get_bind(), checkfirst=True)
    op.add_column("orders", sa.Column("status", order_status_enum, nullable=True))
    op.add_column("order_items", sa.Column("price_at_purchase", sa.Float(), nullable=True))
    op.drop_column("order_items", "price")


def downgrade() -> None:
    """Downgrade schema (reverse changes)."""

    op.add_column("order_items", sa.Column("price", sa.Float(), nullable=True))
    op.drop_column("order_items", "price_at_purchase")
    op.drop_column("orders", "status")
    order_status_enum.drop(op.get_bind(), checkfirst=True)