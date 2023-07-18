import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(os.environ.get("DATABASE_URL"))
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
