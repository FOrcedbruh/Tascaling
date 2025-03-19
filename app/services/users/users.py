from app.repositories import UsersRepository
from app.dto.users.users import UserReadSchema, UserUpdateSchema, UserQueryParamsSchema, UserOnlyReadSchema
from app.dto.tasks.tasks import TaskReadSchema


class UsersService:
    
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    async def get_user_by_id(self, id: int, query_params: UserQueryParamsSchema) -> UserReadSchema:
        user = await self.repository.get_user_with_ideas_and_tasks(id)
        ideas = None
        tasks= None

        if query_params.tasks:
            tasks = [TaskReadSchema(**x.__dict__) for x in await user.tasks]
        if query_params.ideas:
            ideas = []
        return UserReadSchema(
            **user.__dict__,
            tasks=tasks,
            ideas=ideas
        )
    
    async def update_user_by_id(self, id: int, data: UserUpdateSchema) -> UserOnlyReadSchema:
        row = await self.repository.update_user_by_id(id=id, data=data.model_dump(exclude_none=True))
        return UserOnlyReadSchema(**row.__dict__)
    
    
    
