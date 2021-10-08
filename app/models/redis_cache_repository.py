import json
from app.core.redis import Redis
from app.models.base.cache_repository import CacheRepository

class RedisCacheRepository(CacheRepository):
    __DEFAULT_EXPIRED = -1

    def get_json(self, key: str):
        client = Redis().get_client()
        data = client.get(key)
        if data:
            return dict(json.loads(data.decode('utf-8')))

        return None

    def set_json(self, key: str, value: any, expired = -1):
        client = Redis().get_client()
        client.set(key, json.dumps(value, ensure_ascii=False).encode('utf-8'))
        
        if expired >= self.__DEFAULT_EXPIRED:
            client.expire(key, expired)
