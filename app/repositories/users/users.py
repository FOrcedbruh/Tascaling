from abc_repository import BaseRepository
from app.models import User


class UsersRepository(BaseRepository):
    table = User

    async def get_one_by_id(self, id: int) -> User:
        return await self.table.get(id=id)
    
    async def get_all(self, limit: int = 100, offset: int = 0) -> list[User]:
        return await self.table.filter().limit(limit).offset(offset)
    
    async def create_one(self, data: User) -> User:
        return await self.table.create(data)
    
    async def delete_one(self, id: int) -> None:
        row_to_delete = await self.table.get(id=id)
        await self.table.delete(row_to_delete)

    async def get_user_with_relations(self, id: int, tasks: bool = False, ideas: bool = True):
        if tasks:
            return await self.table.get(id=id).prefetch_related("tasks")
        elif ideas:
            return await self.table.get(id=id).prefetch_related("ideas")
        elif ideas and tasks:
            return await self.table.get(id=id).prefetch_related("tasks").prefetch_related("ideas")
    
    