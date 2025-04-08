"""
This file contains the subscription schema for the api
"""

from enum import Enum

from pydantic import BaseModel, Field


class Period(str, Enum):
    """
    Represents the period of the subscription.
    """

    MONTHLY = "monthly"
    YEARLY = "yearly"


class Plan(str, Enum):
    """
    Represents the plan of the subscription.
    """

    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"


class Subscription(BaseModel):
    """
    Represents a subscription in the system.
    """

    id: int = Field(..., description="ID of the subscription")
    user_id: int = Field(..., description="ID of the user")
    plan: Plan = Field(..., description="Name of the plan")
    status: str = Field(..., description="Status of the subscription")
    start_date: str = Field(..., description="Start date of the subscription")
    end_date: str = Field(..., description="End date of the subscription")

    class Config:
        from_attributes = True


class SubscriptionCreate(BaseModel):
    """
    Represents a subscription creation request.
    """

    plan: Plan = Field(..., description="Name of the plan")
    period: Period = Field(..., description="Period of the subscription")

    class Config:
        from_attributes = True
