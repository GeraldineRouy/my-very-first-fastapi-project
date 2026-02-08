from fastapi import APIRouter

from app.api.v1.endpoints import creatures

api_router = APIRouter()

api_router.include_router(
    creatures.router,
    prefix="/creatures",
    tags=["creatures"],
)
