import asyncio
from contextlib import asynccontextmanager
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.database.models.sqlalchemy.base import Base
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
SQLALCHEMY_DATABASE_URI = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/pokemon-db"

# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(SQLModel.metadata.create_all)


# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#     async with async_session() as session:
#         yield session


# @asynccontextmanager
# async def get_session_manager() -> AsyncSession:
#     async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#     async with async_session() as session:
#         yield session


# @asynccontextmanager
# async def get_session() -> AsyncGenerator[AsyncSession, None]:
#     async_session = sessionmaker(
#         engine, class_=AsyncSession, autoflush=True, expire_on_commit=False
#     )
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 yield session
#             finally:
#                 await session.close()


# from sqlalchemy.ext.asyncio import create_async_engine
# engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False)

engine = create_async_engine(
        # settings.SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_DATABASE_URI,
        echo=False,
        # echo=True,
        future=True,
        # poolclass=NullPool,
        # pool_size=1,
    )


async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def test_connection():
    try:
        async with get_session() as session:
            result = await session.execute(text("SELECT 1"))
            print("##########")
            print(result.scalar())
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")


# Run the test
if __name__ == "__main__":
    asyncio.run(test_connection())


# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
