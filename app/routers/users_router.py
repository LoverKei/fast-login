from fastapi import APIRouter, Depends, HTTPException

from app.services.users_service import UserService
from app.models.interfaces.users_interface import (
    user_response_model
)
from app.services.auth_service import AuthService

router = APIRouter()
userService = UserService()
authService = AuthService()

@router.get("/{userId}", response_model = user_response_model)
def getUser(userId: str, token_data = Depends(authService.verify_user)):
    if (userId != token_data.id):
        raise HTTPException(status_code=403, detail="Permission denied. Can not access others info.")

    return userService.get_user_by_id(userId)
