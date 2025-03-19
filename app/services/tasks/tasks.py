from app.dto.tasks.tasks import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from app.repositories import TasksRepository
from app.utils.exceptions.NotFoundExceptions import TaskNotFound
from app.dto.pagination.pagination import BaseParamsSchema
from tortoise.transactions import atomic


class TasksService:

    def __init__(self, repository: TasksRepository):
        self.repository = repository

    async def get_task_by_id(self, id: int) -> TaskReadSchema:
        task = await self.repository.get_one_by_id(id)
        if not task:
            raise TaskNotFound(detail=f"Task with id {id} not found")
        
        return TaskReadSchema(
            **task.__dict__
        )
    
    async def create_task(self, data: TaskCreateSchema) -> TaskReadSchema:
        task = await self.repository.create_one(data=data.model_dump(exclude_none=True))

        return TaskReadSchema(
            **task.__dict__
        )
    
    async def update_task(self, data: TaskUpdateSchema, id: int) -> TaskReadSchema:
        return await self.repository.update_one(id=id, data=data.model_dump(exclude_none=True))
    
    async def delete_task(self, id: int) -> dict:
        await self.repository.delete_one(id=id)

        return {
            "message": f"Task with id {id} successfully deleted"
        }
    
    async def get_all_tasks(self, query_params: BaseParamsSchema) -> list[TaskReadSchema]:
        return await self.repository.get_all(
            **query_params.model_dump(exclude_none=True)
        )