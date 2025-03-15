from app.repositories.abc_repository import BaseRepository
from app.models import Task
from app.utils.exceptions.NotFoundExceptions import TaskNotFound





class TasksRepository(BaseRepository):
    table = Task

    async def get_one_by_id(self, id: int) -> Task:
        row = await self.table.get_or_none(id=id)
        return row

    async def get_all(self, limit: int, offset: int, order_by: str, asc: bool) -> list[Task]:
        return await self.table.filter().limit(limit).offset(offset).order_by(f"{order_by if asc else f"-{order_by}"}")
    
    async def create_one(self, data: dict) -> Task:
        row = await self.table.create(**data)
        return row
    
    async def delete_one(self, id: int) -> None:
        row = await self.table.get_or_none(id=id)

        if not row:
            raise TaskNotFound(detail=f"Task with id {id} not found")
        
        await row.delete()

    async def update_one(self, id: int, data: dict) -> Task:
        row = await self.table.get_or_none(id=id)
        if not row:
            raise TaskNotFound(detail=f"Task with id {id} not found")
        
        await row.update_from_dict(data)
        return row