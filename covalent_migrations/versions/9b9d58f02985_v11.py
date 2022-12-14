"""v11

Revision ID: 9b9d58f02985
Revises: b60c5ecdf927
Create Date: 2022-08-01 17:57:39.385604

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
# pragma: allowlist nextline secret
revision = "9b9d58f02985"
# pragma: allowlist nextline secret
down_revision = "b60c5ecdf927"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("electrons", sa.Column("executor", sa.Text(), nullable=True))
    op.add_column("electrons", sa.Column("executor_data_filename", sa.Text(), nullable=True))
    op.drop_column("electrons", "key_filename")
    op.drop_column("electrons", "attribute_name")
    op.drop_column("electrons", "executor_filename")
    op.add_column("lattices", sa.Column("executor", sa.Text(), nullable=True))
    op.add_column("lattices", sa.Column("executor_data_filename", sa.Text(), nullable=True))
    op.add_column("lattices", sa.Column("workflow_executor", sa.Text(), nullable=True))
    op.add_column(
        "lattices", sa.Column("workflow_executor_data_filename", sa.Text(), nullable=True)
    )
    op.add_column("lattices", sa.Column("named_args_filename", sa.Text(), nullable=True))
    op.add_column("lattices", sa.Column("named_kwargs_filename", sa.Text(), nullable=True))
    op.drop_column("lattices", "executor_filename")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("lattices", sa.Column("executor_filename", sa.TEXT(), nullable=True))
    op.drop_column("lattices", "named_kwargs_filename")
    op.drop_column("lattices", "named_args_filename")
    op.drop_column("lattices", "workflow_executor_data_filename")
    op.drop_column("lattices", "workflow_executor")
    op.drop_column("lattices", "executor_data_filename")
    op.drop_column("lattices", "executor")
    op.add_column("electrons", sa.Column("executor_filename", sa.TEXT(), nullable=True))
    op.add_column("electrons", sa.Column("attribute_name", sa.TEXT(), nullable=True))
    op.add_column("electrons", sa.Column("key_filename", sa.TEXT(), nullable=True))
    op.drop_column("electrons", "executor_data_filename")
    op.drop_column("electrons", "executor")
    # ### end Alembic commands ###
