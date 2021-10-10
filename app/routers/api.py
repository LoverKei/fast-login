from fastapi import APIRouter

from app.routers import users_router
from app.routers import auth_router

router = APIRouter()
router.include_router(users_router.router, tags=["users"], prefix="/users")
router.include_router(auth_router.router, tags=["auth"], prefix="/auth")
