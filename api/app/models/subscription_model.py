"""
This file contains the subscription model for the api
"""

from app.database import Base

from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship


class Subscription(Base):
    """
    Represents a subscription in the system.
    """

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plan = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    start_date = Column(String(50), nullable=False)
    end_date = Column(String(50), nullable=False)

    user = relationship("User", back_populates="subscriptions")

    def __repr__(self):
        return f"<Subscription(id='{self.id}', user_id={self.user_id}, plan_id={self.plan_id})>"
