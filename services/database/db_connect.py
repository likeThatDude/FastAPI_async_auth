from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import as_declarative, declared_attr, sessionmaker
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

engine = create_async_engine(f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=False)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


@as_declarative()
class Base:
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
