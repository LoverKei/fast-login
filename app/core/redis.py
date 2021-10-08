import redis
from app.core.config import (
    REDIS_URL
)

class Redis(object):
    __client = None

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            print("Redis - connection...")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.__client = redis.StrictRedis(REDIS_URL)
            self.__hello_redis()
            cls._init = True

    def get_client(self):
        return self.__client

    def __hello_redis(self):
        self.get_client().set("hello", "redis")
