from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase, AsyncAttrs):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    version: Mapped[int] = mapped_column()  # schema version

    followers: Mapped[List["Following"]] = relationship(
        back_populates="follower", lazy="selectin"
    )
    followees: Mapped[List["Following"]] = relationship(
        back_populates="followee", lazy="selectin"
    )


class Following(Base):
    __tablename__ = "following"

    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    followee_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    follower: Mapped["User"] = relationship(
        back_populates="followers", lazy="selectin"
    )
    followee: Mapped["User"] = relationship(
        back_populates="followees", lazy="selectin"
    )
