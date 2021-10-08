from pymongo import MongoClient
from app.core.config import (
    MONGODB_NAME,
    MONGODB_URL
)

class MongoDB(object):
    __client = None

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            print("MongoDB - connection...")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):
            client = MongoClient(MONGODB_URL)
            self.__client = client[MONGODB_NAME]
            self.__init_index()
            cls._init = True

    def __init_index(self):
        print("MondoDB - create index.")
        self.__client.users.create_index([('email', -1)], name='_email_', unique=True)
        self.__client.users.create_index([('phone', -1)], name='_phone_', unique=True)

    def get_client(self):
        return self.__client
