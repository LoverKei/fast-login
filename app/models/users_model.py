from pydantic import BaseModel, Field
from app.models.py_objectid import PyObjectId
from bson import ObjectId

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str
    nickname: str
    password: str
    name: str
    phone: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
