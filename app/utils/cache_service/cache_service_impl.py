from app.utils.cache_service.base import CacheStorageInterface
from redis.asyncio import Redis
from redis.typing import KeyT
from app.core.settings import Settings
from typing import Any
from datetime import timedelta
from app.utils.hashing import HashingUtility
import json

cache_settings = Settings().cache

class RedisCacheService(CacheStorageInterface):

    def __init__(self):
        self.storage = Redis(host=cache_settings.host, port=cache_settings.port, db=0)

    async def get(self, key: KeyT) -> Any:
        name = HashingUtility.hash_str(key)
        res = await self.storage.get(name=name)
        return json.loads(res) if res else None

    async def set(self, key: KeyT, value: Any, ttl: int | timedelta = cache_settings.ttl):
        name = HashingUtility.hash_str(key)
        await self.storage.setex(name=name, value=json.dumps(value), time=ttl)