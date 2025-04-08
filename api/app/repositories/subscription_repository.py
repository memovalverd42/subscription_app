"""
This file contains the subscription repository for the api
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import SessionDep
from app.models import Subscription


class SubscriptionRepository:
    """
    Subscription repository
    """

    def __init__(self, db: Session):
        """
        Constructor for the UserRepository class
        :param db: Database session
        """
        self.db = db

    def create_subscription(self, subscription: Subscription) -> Subscription:
        """
        Create a new user in the database
        :param subscription: subscription object
        :return: subscription object
        """
        self.db.add(subscription)
        self.db.commit()
        self.db.refresh(subscription)
        return subscription

    def update_subscription(self, subscription: Subscription) -> Subscription:
        """
        Update a subscription in the database
        :param subscription: subscription object
        :return: subscription object
        """
        self.db.commit()
        self.db.refresh(subscription)
        return subscription

    def get_subscriptions_by_user_id(self, user_id: int) -> list[Subscription]:
        """
        Get all subscriptions by user ID
        :param user_id: User ID
        :return: List of subscriptions
        """
        return self.db.query(Subscription).filter(Subscription.user_id == user_id).all()

    def get_active_subscription_by_user_and_plan(
        self, user_id: int, plan: str
    ) -> Subscription | None:
        """
        Get active subscription by user ID and plan
        :param user_id: User ID
        :param plan: Plan name
        :return: Subscription object or None
        """
        return (
            self.db.query(Subscription)
            .filter(
                Subscription.user_id == user_id,
                Subscription.plan == plan,
                Subscription.status == "active",
            )
            .first()
        )


def get_subscription_repository(db: SessionDep):
    """
    Dependency to get the user repository
    :param db: Database session
    :return: SubscriptionRepository object
    """
    return SubscriptionRepository(db)


SubscriptionRepoDep = Annotated[
    SubscriptionRepository, Depends(get_subscription_repository)
]
