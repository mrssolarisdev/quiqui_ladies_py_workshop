from enum import Enum

from sqlalchemy import Metadata, Table, Column, Integer, String, Index

from enums.user_status_enum import UserStatusEnum

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

Index("first_last_name_idx", user_table.c.first_name, user_table.c.last_name)