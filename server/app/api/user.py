import app.models.tables as tables
from app.api.crud import get_followers
from app.db import async_get_db
from app.models.schemas import User
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/user", tags=["user"])


@router.get(
    "/followers/{user_id}",
    # response_model=list[User],
)
async def get_followers_of_user(
    user_id: int, db: AsyncSession = Depends(async_get_db)
):
    user = await db.get(tables.User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found",
        )
    return get_followers(db, user_id)
