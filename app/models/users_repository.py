import traceback
from bson.objectid import ObjectId
from fastapi import HTTPException
import pymongo

from app.models.base.py_objectid import convert_id
from app.models.base.base_mongo import BaseMongoRepository
from app.models.redis_cache_repository import RedisCacheRepository
from app.models.interfaces.users_interface import user_create_model

class UserRepository(BaseMongoRepository):
    def __init__(self, cacheRepo = RedisCacheRepository):
        super().__init__()
        self.__db = super().get_client()["users"]
        self.__cache = cacheRepo()
        self.__CACHE_EXPIRED = 30


    def find_user_by_id(self, id: str):
        cached_user = self.get_cache_user(id)
        if cached_user:
            return cached_user

        result = self.__db.find_one({ "_id": ObjectId(id) })

        return convert_id(result)

    def add_user(self, user: user_create_model):
        try:
            result = self.__db.insert_one(user.dict())
            new_user = self.find_user_by_id(str(result.inserted_id))
            self.set_cache_user(new_user)

            return new_user
        except pymongo.errors.DuplicateKeyError:
            traceback.print_exc()
            raise HTTPException(status_code=400, detail="Duplicated user")
        except Exception:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Oops!")

    def set_cache_user(self, user):
        if self.__cache:
            self.__cache.set_json(str(user["id"]), user, self.__CACHE_EXPIRED)

    def get_cache_user(self, id: str):
        if self.__cache:
            return self.__cache.get_json(id)
        return None
