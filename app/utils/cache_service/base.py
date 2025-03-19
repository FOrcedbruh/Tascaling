from abc import ABC, abstractmethod
from typing import Any


class CacheStorageInterface(ABC):
    @abstractmethod
    async def get(self, key: Any) -> Any: ...

    @abstractmethod
    async def set(self, key: Any, value: Any) -> Any: ...