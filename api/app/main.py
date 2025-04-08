"""
Main module of the API.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.routers import users_router, subscription_router

load_dotenv()

app = FastAPI(
    title="Subscriptions API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOW_ORIGINS"),
    allow_credentials=os.getenv("ALLOW_CREDENTIALS"),
    allow_methods=os.getenv("ALLOW_METHODS"),
    allow_headers=os.getenv("ALLOW_HEADERS"),
)

app.include_router(users_router)
app.include_router(subscription_router)
