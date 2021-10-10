from typing import Optional
from pydantic import BaseModel

class token_response(BaseModel):
    access_token: str
    token_type: str

class verify_token_request(BaseModel):
    phone: str

class verify_token_response(BaseModel):
    verify_token: str