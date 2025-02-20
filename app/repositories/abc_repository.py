from abc import ABC, abstractmethod
from typing import Any

class BaseRepository(ABC):
    @abstractmethod
    async def get_one_by_id(self, id: int) -> Any: ... 

    @abstractmethod
    async def get_all(self, limit: int, offset: int) -> Any: ...

    @abstractmethod
    async def create_one(self, *args, **kwargs) -> Any: ...

    @abstractmethod
    async def delete_one(self, id: int) -> Any | None: ...