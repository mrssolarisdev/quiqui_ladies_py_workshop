from enum import Enum

from sqlalchemy import Metadata, Table, Column, Integer, String, Index

from domain.enums.user_status_enum import UserStatusEnum

metadata_obj = Metadata()

user_table = Table(
    "user",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(10), nullable=False),
    Column("first_name", String(10), nullable=False),
    Column("last_name", String(20), nullable=False),
    Column("status", Enum(UserStatusEnum), default=UserStatusEnum.ACTIVE, server_default=UserStatusEnum.ACTIVE),
)

# Disclaimer: We're creating an index on the combination of columns we are going to use the most, but it is not safe to assume a 
# user can be identified by just their first and last name. This is just an example, always use an information that uniquely identifies 
# the user, like the username. I'm doing this just to show you can use a combination of columns (composition) if need be.
Index("first_last_name_idx", user_table.c.first_name, user_table.c.last_name) 