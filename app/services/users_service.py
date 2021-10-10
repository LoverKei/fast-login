from fastapi import HTTPException
from app.models.users_repository import UserRepository
from app.models.interfaces.users_interface import (
    user_create_model
)
from app.models.users_model import User

class UserService:
    def __init__(self):
        self.userRepository = UserRepository()

    def get_user_by_id(self, id: str) -> User:
        user = self.userRepository.find_user_by_id(id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create_user(self, user: user_create_model) -> User:
        return self.userRepository.add_user(user)
