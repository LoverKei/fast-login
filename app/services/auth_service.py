from datetime import datetime, timedelta
from typing import Optional
import traceback

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.models.users_repository import UserRepository
from app.models.interfaces.users_interface import (
    user_signin_model
)
from app.models.users_model import User

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str
    role: str

class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    def __init__(self):
        self.__SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        self.__ALGORITHM = "HS256"
        self.__ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.userRepository = UserRepository()

    def verify_password(self, plain_password, hashed_password):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, requester: user_signin_model):
        db_user = self.userRepository.find_user_by_id(requester.id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        if not self.verify_password(requester.password, db_user["password"]):
            raise HTTPException(status_code=400, detail="Invalid password")

        token_data: TokenData = { "id": requester.id, "role": "user" }
        return self.create_access_token(token_data)

    def verify_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGORITHM])
            userId = payload["id"]
            if userId is None:
                raise credentials_exception
            token_data = TokenData(**payload)
            return token_data
        except JWTError:
            traceback.print_exc()
            raise credentials_exception
