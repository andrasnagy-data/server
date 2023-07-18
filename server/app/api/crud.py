from app.models.schemas import UserInDB
from app.models.tables import Following, User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_followers(db: AsyncSession, user_id: int):  # -> list[UserInDB]:
    """
    Get a user's followers.
    """
    stmt = select(User.followers).where(id=user_id)
    res = await db.execute(stmt)
    return res.all()
