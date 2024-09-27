from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from configs import db_settings

"""
Database connection setup and session management using SQLAlchemy and asyncpg.
"""


SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://"
    f"{db_settings.POSTGRES_USER}:"  # noqa E231
    f"{db_settings.POSTGRES_PASSWORD}@"
    f"{db_settings.POSTGRES_HOST}:"  # noqa E231
    f"{db_settings.POSTGRES_PORT}/"
    f"{db_settings.POSTGRES_DB}"
)

async_engine = create_async_engine(url=SQLALCHEMY_DATABASE_URL, echo=False)

async_session = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
