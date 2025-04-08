"""
This file contains the user schema
"""

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    is_active: bool | None = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    password: str

    class Config:
        from_attributes = True


class Session(BaseModel):
    user: User
    token: Token


class UserLogin(BaseModel):
    email: str
    password: str = Field(..., min_length=8, max_length=64, examples=["strongpass"])
