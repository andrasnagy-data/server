"""
User end-point.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.engine.row import Row
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

import server.db.models as models
from server.api.utils.user import get_user_followers
from server.db.conn import get_db
from server.internals import logger
from server.schemas import User

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/followers/{user_id}", response_model=list[User])
def get_followers_of_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get followers of user.
    """
    try:
        if db.get(models.User, user_id) is None:
            logger.error(f"Error: User not in DB.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found",
            )
        list_of_followers: list[User] = [
            User(
                name=follower.first_name + " " + follower.last_name,
                email=follower.email,
            )
            for follower in get_user_followers(db=db, user_id=user_id)
        ]
        logger.info(f"Success: {get_followers_of_user.__name__}")
        return list_of_followers
    except SQLAlchemyError as e:
        logger.error(f"Error: {e}")
        raise e
