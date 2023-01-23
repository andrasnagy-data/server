"""
Users end-point's CRUD.
"""
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from server.db.models import User, relationships
from server.schemas import UserInDB


def get_user_followers(db: Session, user_id: int) -> list[UserInDB]:
    """
    Get a user's followers.
    """
    stmt = (
        select(User.first_name, User.last_name, User.email)
        .join(relationships, User.id == relationships.c.follower)
        .where(relationships.c.followee == user_id)
        .order_by(User.first_name, User.last_name)
    )
    return db.execute(stmt).all()
