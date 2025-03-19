from app.models import Statistics, User, Task, Idea
from app.models.tasks.tasks import TaskStatus
from app.repositories.abc_repository import BaseRepository
from app.utils.exceptions.NotFoundExceptions import StatisticNotFound
from tortoise.transactions import atomic

class StatisticRepository(BaseRepository):
    table = Statistics

    async def update_one(self, id: int, data: dict) -> Statistics:
        row = await self.table.get_or_none(id=id)
        if not row:
            raise StatisticNotFound(f"Statistics with id {id} not found")
        await row.update_from_dict(data)
        await row.save()

        return row
    
    async def get_one_by_user_id(self, user_id: int) -> Statistics:
        row = await self.table.get_or_none(user_id=user_id)
        if not row:
            raise StatisticNotFound(f"Statistics with user id {user_id} not found")
        return row
        
    async def create_one(self, data: dict) -> Statistics:
        row  = await self.table.create(**data)
        return row
    
    async def get_one_by_id(self, id: int) -> Statistics:
        row = await self.table.get_or_none(id=id)
        if not row:
            raise StatisticNotFound(f"Statistics with id {id} not found")
        return row
    
    def calc_tasks(self, tasks: list[Task]) -> list[int]:
        completed_tasks = 0
        total_tasks = 0

        for task in tasks:
            if task.status == TaskStatus.COMPLETED:
                completed_tasks += 1
            elif task.status in (TaskStatus.IN_PROGRESS, TaskStatus.CREATED):
                total_tasks += 1

        return total_tasks, completed_tasks
    
    def calc_ideas(self, ideas: list[Idea]) -> int:
        return len(ideas)

    @atomic()
    async def calculate_and_get_statistics(self, user_id: int) -> Statistics:
        row = await self.table.filter(user_id=user_id).select_for_update().first()
        if not row:
            raise StatisticNotFound(f"Statistics with user id {user_id} not found")
        user_row = await User.filter(id=user_id).prefetch_related("tasks", "ideas").first()

        row.total_tasks, row.completed_tasks = self.calc_tasks(tasks=user_row.tasks)
        row.total_ideas = self.calc_ideas(ideas=user_row.ideas)

        await row.save(update_fields=["total_tasks", "total_ideas", "completed_tasks"])
        return row

    async def get_all(self, limit, offset) -> ...:
        ...

    async def delete_one(self, id) -> ...:
        ...


    