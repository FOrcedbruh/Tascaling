from app.repositories.abc_repository import BaseRepository
from app.models import User
from app.utils.exceptions import UserNotFound


class UsersRepository(BaseRepository):
    table = User

    async def get_one_by_id(self, id: int) -> User:
        user = await self.table.get(id=id)
        return user
    
    async def get_all(self, limit: int = 100, offset: int = 0) -> list[User]:
        return await self.table.filter().limit(limit).offset(offset)
    
    async def create_one(self, data: dict) -> User:
        return await self.table.create(**data)
    
    async def delete_one(self, id: int) -> None:
        row_to_delete = await self.table.get(id=id)
        await self.table.delete(row_to_delete)

    async def get_user_by_username(self, data: str) -> User:
        row = await User.get_or_none(username=data)
        if not row:
            raise UserNotFound(f"User with username {data} does not exists")
        return row
    
    async def get_user_for_create(self, data: str) -> User:
        row = await User.get_or_none(username=data)
        return row

    async def get_user_with_relations(self, id: int, ideas: bool = False, tasks: bool = True):
        user = None
        if tasks:
            user = await self.table.get(id=id).prefetch_related("tasks")
        elif ideas:
            user = await self.table.get(id=id).prefetch_related("ideas")
        elif ideas and tasks:
            user =  await self.table.get(id=id).prefetch_related("tasks").prefetch_related("ideas")
        
        if user is None:
            raise UserNotFound(f"User with id {id} does not exists")
        return user
    
    async def update_user_by_id(self, id: int, data: dict) -> User:
        user = await User.get_or_none(id=id)
        if not user:
            raise UserNotFound(f"User with id {id} does not exists")
        return user.update_from_dict(data)


    
    