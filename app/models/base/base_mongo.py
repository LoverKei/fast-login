from app.core.mongodb import MongoDB

class BaseMongoRepository:
    def __init__(self):
        self.__client = MongoDB().get_client()

    def get_client(self):
        return self.__client
