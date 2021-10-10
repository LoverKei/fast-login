from app.models.redis_cache_repository import RedisCacheRepository

class AuthRepository():
    def __init__(self, cacheRepo = RedisCacheRepository):
        super().__init__()
        self.__prefix = "VERIFYTOKEN"
        self.__cache = cacheRepo()
        self.__CACHE_EXPIRED = 300 # 5mins

    def add_verify_token(self, token: str, verify_input):
        key = "%s:%s" % (self.__prefix, token)
        self.add_token(key, verify_input)

    def add_token(self, k, v):
        # key = "%s:%s" % (self.__prefix, k)
        self.__cache.set_json(k, v, self.__CACHE_EXPIRED)

    def find_verify_by_token(self, token: str):
        key = "%s:%s" % (self.__prefix, token)
        return self.__cache.get_json(key)
