"""
This module contains the user model for the api
"""

from app.database import Base

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    """
    Represents a user in the system.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)

    is_active = Column(Boolean, default=True)

    subscriptions = relationship("Subscription", back_populates="user")

    def __repr__(self):
        return f"<User(id='{self.id}', first_name={self.first_name})>"
