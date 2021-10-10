from datetime import datetime, timedelta
from typing import Optional
import traceback
import hashlib
import re

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from app.models.users_repository import UserRepository
from app.models.interfaces.users_interface import (
    user_signin_model
)
from app.models.auth_repository import AuthRepository
from app.services.sms_service import sendSMS

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
        self.authRepository = AuthRepository()

    def __verify_password(self, plain_password, hashed_password):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)

    def __create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)
        return encoded_jwt

    def get_signin_type(self, key):
        email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_format = r'[\d]{3}-[\d]{4}-[\d]{4}'
        if (re.fullmatch(email_format, key)):
            return 'email'
        elif(re.fullmatch(phone_format, key)):
            return 'phone'
        else:
            return 'id'

    def authenticate_user(self, requester: user_signin_model):
        type = self.get_signin_type(requester.id)
        if type == 'id':
            db_user = self.userRepository.find_user_by_id(requester.id)
        else:
            db_user = self.userRepository.find_user({ type: requester.id })

        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        if not self.__verify_password(requester.password, db_user["password"]):
            raise HTTPException(status_code=400, detail="Invalid password")

        token_data: TokenData = { "id": db_user["id"], "role": "user" }
        return self.__create_access_token(token_data)

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

    def request_verify_code(self, verify_input):
        code = self.__generate_verify_code()
        token = self.__generate_verify_token(verify_input)

        msg = "[CODE] %s. Please input this code to verify page." % code

        verify_data = {
            "phone": verify_input.phone,
            "code": code
        }
        self.authRepository.add_verify_token(token, verify_data)
        sendSMS(verify_input.phone, msg)
        return token

    def __generate_verify_code(self):
        # FAKE CODE: 0000
        return '0000'

    def __generate_verify_token(self, data):
        to_encode = "%s%s" % (data, datetime.utcnow())
        token = hashlib.shake_256(to_encode.encode("utf-8")).hexdigest(length=16)

        return token

    def verify_signup_code(self, user):
        verify_data = self.authRepository.find_verify_by_token(user.verify_token)
        if not verify_data:
            raise HTTPException(status_code=404, detail="Can not find verify token")
        if not verify_data["code"] == user.code:
            raise HTTPException(status_code=400, detail="Invalid code")
        if not verify_data["phone"] == user.phone:
            raise HTTPException(status_code=400, detail="Invalid phone")

        return True
