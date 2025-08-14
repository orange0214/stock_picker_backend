from fastapi import APIRouter

from .routes import health, etf

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(etf.router)