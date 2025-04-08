"""
This file contains the subscription router for the api
"""

from datetime import datetime

from fastapi import status, APIRouter, HTTPException, Depends

from app.repositories import SubscriptionRepoDep
from app.schemas import Subscription, SubscriptionCreate
from sqlalchemy.exc import SQLAlchemyError

from app.models import Subscription as SubscriptionModel, User
from app.schemas.subscription_scheme import Period, Plan
from app.services.auth_service import get_current_active_user

subscription_router = APIRouter(
    prefix="/subscription",
    tags=["Subscription"],
    dependencies=[Depends(get_current_active_user)],
)


@subscription_router.post(
    "/subscribe",
    status_code=status.HTTP_201_CREATED,
    response_model=Subscription,
    summary="Crear suscripción",
)
def create_user_subscription(
    data: SubscriptionCreate,
    subs_repo: SubscriptionRepoDep,
    user: User = Depends(get_current_active_user),
):
    """
    Crear una suscripción si el usuario no tiene una activa al mismo plan.
    """
    try:
        # Verificar si ya hay una suscripción activa con el mismo plan
        existing = subs_repo.get_active_subscription_by_user_and_plan(
            user.id, data.plan
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya estás suscrito a este plan.",
            )

        start_date = datetime.now()
        if data.period == Period.MONTHLY:
            end_date = start_date.replace(month=start_date.month + 1)
        else:
            end_date = start_date.replace(month=start_date.month + 12)

        new_subscription = SubscriptionModel(
            user_id=user.id,
            plan=data.plan,
            status="active",
            start_date=start_date.strftime("%Y-%m-%d %H:%M:%S"),
            end_date=end_date.strftime("%Y-%m-%d %H:%M:%S"),
        )
        return subs_repo.create_subscription(new_subscription)

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear la suscripción.",
        ) from e


@subscription_router.get(
    "",
    response_model=list[Subscription],
    summary="Obtener suscripciones por usuario",
)
async def get_subscriptions_by_user(
    subs_repo: SubscriptionRepoDep, user: User = Depends(get_current_active_user)
):
    """
    Get all subscriptions by user ID
    """
    try:
        return subs_repo.get_subscriptions_by_user_id(user.id)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Error en db",
        ) from e


@subscription_router.put(
    "/cancel",
    status_code=status.HTTP_200_OK,
    response_model=Subscription,
    summary="Cancelar suscripción activa",
)
def cancel_user_subscription(
    plan: Plan,
    subs_repo: SubscriptionRepoDep,
    user: User = Depends(get_current_active_user),
):
    """
    Cancela la suscripción activa del usuario al plan especificado.
    """
    try:
        subscription = subs_repo.get_active_subscription_by_user_and_plan(user.id, plan)

        if not subscription:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se encontró una suscripción activa para este plan.",
            )

        subscription.status = "cancelled"
        subscription.end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return subs_repo.update_subscription(subscription)

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al cancelar la suscripción.",
        ) from e
