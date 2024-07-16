import asyncio
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# Configuration for the database URL
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/pokemon-db"
# Create an asynchronous engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False,
    future=True,
)

# Create a sessionmaker
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Async context manager to get a session
@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# Function to test the database connection
async def test_connection():
    try:
        async with get_session() as session:
            result = await session.execute(text("SELECT 1"))
            scalar_result = result.scalar()
            print(scalar_result)
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")

# Run the test
if __name__ == "__main__":
    asyncio.run(test_connection())
