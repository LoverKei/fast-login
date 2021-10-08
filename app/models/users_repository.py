from bson.objectid import ObjectId
from fastapi import HTTPException
import pymongo

from app.core.mongodb import MongoDB
from app.models.interfaces.users_interface import user_create_model
from app.models.py_objectid import convert_id

users = MongoDB().get_client()["users"]

def find_user_by_id(id: str):
    print(id)
    result = users.find_one({ "_id": ObjectId(id) })

    return convert_id(result)

def add_user(user: user_create_model):
    try:
        result = users.insert_one(user.dict())
        new_user = find_user_by_id(result.inserted_id)

        return new_user
    except pymongo.errors.DuplicateKeyError:
        print(Exception)
        raise HTTPException(status_code=400, detail="Duplicated user")
    except Exception:
        raise HTTPException(status_code=500, detail="Oops!")
