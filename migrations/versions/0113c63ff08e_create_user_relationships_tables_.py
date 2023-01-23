"""Create user & relationships tables; populate tables with demo data.

Revision ID: 0113c63ff08e
Revises: 
Create Date: 2023-01-22 20:01:31.482641

"""
from json import loads
from pathlib import Path

import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "0113c63ff08e"
down_revision = None
branch_labels = None
depends_on = None


## path (for demo data)
server_folder = Path(".").parent


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user = op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column(
            "email",
            sqlalchemy_utils.types.email.EmailType(length=255),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    # add demo data
    with open(server_folder.joinpath("migrations/demo-data/users.json")) as f:
        user_data = loads(f.read())
    op.bulk_insert(user, user_data)
    relationships = op.create_table(
        "relationships",
        sa.Column("follower", sa.Integer(), nullable=True),
        sa.Column("followee", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["followee"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower"],
            ["user.id"],
        ),
    )
    # add demo data
    with open(
        server_folder.joinpath("migrations/demo-data/relationships.json")
    ) as f:
        relationship_data = loads(f.read())
    op.bulk_insert(relationships, relationship_data)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("relationships")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
