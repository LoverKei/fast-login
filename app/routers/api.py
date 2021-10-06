from fastapi import APIRouter

from app.routers import users_router

router = APIRouter()
router.include_router(users_router.router, tags=["users"], prefix="/users")

@router.get("")
async def helloAPI ():
    return "Hello, API!!!"