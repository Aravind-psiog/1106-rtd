"""v12

Revision ID: 26d71848a404
Revises: 9b9d58f02985
Create Date: 2022-09-08 10:46:11.140472

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
# pragma: allowlist nextline secret
revision = "26d71848a404"
# pragma: allowlist nextline secret
down_revision = "9b9d58f02985"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lattices", schema=None) as batch_op:
        batch_op.add_column(sa.Column("docstring_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("deps_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("call_before_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("call_after_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("cova_imports_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("lattice_imports_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("results_dir", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("root_dispatch_id", sa.String(length=64), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lattices", schema=None) as batch_op:
        batch_op.drop_column("root_dispatch_id")
        batch_op.drop_column("results_dir")
        batch_op.drop_column("lattice_imports_filename")
        batch_op.drop_column("cova_imports_filename")
        batch_op.drop_column("call_after_filename")
        batch_op.drop_column("call_before_filename")
        batch_op.drop_column("deps_filename")
        batch_op.drop_column("docstring_filename")

    # ### end Alembic commands ###
