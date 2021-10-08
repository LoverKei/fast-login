from abc import *

class CacheRepository(metaclass = ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_json(self, key: str):
        pass

    @abstractmethod
    def set_json(self, key: str, value: any, expired: int):
        pass
