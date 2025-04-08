"""
This file contains the user repository
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import SessionDep
from app.models import User


class UserRepository:
    """
    This class contains the user repository
    """

    def __init__(self, db: Session):
        """
        Constructor for the UserRepository class
        :param db: Database session
        """
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        """
        Get a user by email
        :param email: User email
        :return: User object
        """
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: dict) -> User:
        """
        Create a new user in the database
        :param user: User object
        :return: User object
        """
        user_db = User(**user)
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db


def get_user_repository(db: SessionDep):
    """
    Dependency to get the user repository
    :param db: Database session
    :return: UserRepository object
    """
    return UserRepository(db)


UserRepoDep = Annotated[UserRepository, Depends(get_user_repository)]
