from sqlalchemy import (
    MetaData,
    Boolean,
    Integer,
    String,
    TIMESTAMP,
    ForeignKey,
    Table,
    Column,
    JSON, func
)

metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON),
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('created_at', TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()),
    Column('modified_at', TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
)