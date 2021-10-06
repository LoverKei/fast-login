from fastapi import APIRouter

from app.services.users_service import (
    hello_user,
    get_user_by_id
)

router = APIRouter()

@router.get("")
def helloUser ():
    return hello_user()

@router.get("/{userId}")
def getUser(userId: str):
    return get_user_by_id(userId)
