"""
This file contains the authentication service for the FastAPI application.
"""

import os
from datetime import datetime, timedelta, timezone, UTC
from typing import Annotated, Optional

import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from app.models import User
from app.repositories import UserRepository, UserRepoDep
from app.schemas.user_scheme import TokenData

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


def verify_password(plain_password: str | bytes, password: str | bytes) -> bool:
    """
    Verifica si la contraseña es correcta
    :param plain_password: String o bytes de la contraseña
    :param password: String de la contraseña encriptada
    :return: True si la contraseña es correcta, False si no
    """
    return plain_password == password


def authenticate_user(
    email: str, password: str, user_repo: UserRepository
) -> Optional[User]:
    user = user_repo.get_user_by_email(email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_token(
    email: str, password: str, user_repo: UserRepository
) -> tuple[str, User]:
    user = authenticate_user(email, password, user_repo)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credeciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=36)
    return (
        create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        ),
        user,
    )


def validate_token(token: str, user_repo: UserRepository) -> Optional[User]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except Exception as e:
        raise credentials_exception from e

    user = user_repo.get_user_by_email(email=email)
    if user is None:
        raise credentials_exception

    return user


def get_refresh_token(token: str, user_repo: UserRepository) -> tuple[str, User]:
    user = validate_token(token, user_repo)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    new_access_token_expires = timedelta(minutes=36)
    return (
        create_access_token(
            data={"sub": user.email}, expires_delta=new_access_token_expires
        ),
        user,
    )


async def get_current_user(
    user_repo: UserRepoDep, token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except Exception as e:
        raise credentials_exception from e

    user = user_repo.get_user_by_email(token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    return current_user
