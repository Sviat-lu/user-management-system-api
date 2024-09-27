from fastapi import APIRouter

from .endpoints import users_router

api_v1_router = APIRouter(prefix="/v1")


api_v1_router.include_router(users_router, prefix="/users", tags=["Users"])
