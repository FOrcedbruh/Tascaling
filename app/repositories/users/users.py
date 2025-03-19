from app.repositories.abc_repository import BaseRepository
from app.models import User
from app.utils.exceptions import UserNotFound
from tortoise import Tortoise

class UsersRepository(BaseRepository):
    table = User

    async def get_one_by_id(self, id: int) -> User:
        user = await self.table.get_or_none(id=id)
        return user
    
    async def get_all(self, limit: int = 100, offset: int = 0) -> list[User]:
        return await self.table.filter().limit(limit).offset(offset)
    
    async def create_one(self, data: dict) -> User:
        return await self.table.create(**data)
    
    async def delete_one(self, id: int) -> None:
        row_to_delete = await self.table.get(id=id)
        await self.table.delete(row_to_delete)

    async def get_user_by_username(self, data: str) -> User:
        row = await self.table.get_or_none(username=data)
        if not row:
            raise UserNotFound(f"User with username {data} does not exists")
        return row
    
    async def get_user_for_create(self, data: str) -> User:
        row = await self.table.get_or_none(username=data)
        return row

    async def get_user_with_ideas_and_tasks(self, id: int):
        user = await self.table.get_or_none(id=id)
        
        if not user:
            raise UserNotFound(f"User with id {id} does not exists")
        return user
    
    async def update_user_by_id(self, id: int, data: dict) -> dict:
        user = await self.table.get_or_none(id=id)
        if not user:
            raise UserNotFound(f"User with id {id} does not exists")
        await user.update_from_dict(data)
        await user.save()
        return user



    
    