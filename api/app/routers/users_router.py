"""
This app contains the user router
"""

from fastapi import Depends, status, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.repositories import UserRepoDep
from app.schemas import User, UserCreate, Session
from sqlalchemy.exc import SQLAlchemyError

from app.schemas.user_scheme import UserLogin, Token
from app.services.auth_service import generate_token

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    summary="Crear un nuevo usuario en la app",
)
def create_user(user: UserCreate, user_repo: UserRepoDep):
    """
    Crear un nuevo usuario en la app
    """
    try:
        user_dict = user.model_dump()
        return user_repo.create_user(user_dict)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El usuario ya existe",
        ) from e


@users_router.post("/login", response_model=Session, summary="Iniciar sesión")
async def login_for_access_token(user: UserLogin, ser_repo: UserRepoDep):
    """
    Inicio de sesión para obtener un token de acceso
    """
    access_token, user_authenticated = generate_token(
        user.email, user.password, user_repo=ser_repo
    )
    token = Token(access_token=access_token, token_type="bearer")
    return Session(token=token, user=User.model_validate(user_authenticated))


@users_router.post("/token", response_model=Token, summary="Obtener un token de acceso")
async def get_token(
    user_service: UserRepoDep, form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Obtener un token de acceso
    """
    access_token, _user = generate_token(
        form_data.username, form_data.password, user_service
    )
    return Token(access_token=access_token, token_type="bearer")
