from app.repositories import UsersRepository
from app.dto.users.users import UserReadSchema, UserUpdateSchema


class UsersService:
    
    def __init__(self, repository: UsersRepository):
        self.repository = repository


    async def get_user_by_id(self, id: int, tasks: bool = True, ideas: bool = False) -> UserReadSchema:
        return await self.repository.get_user_with_relations(id=id, tasks=tasks, ideas=ideas)
    
    async def update_user_by_id(self, id: int, data: UserUpdateSchema) -> UserReadSchema:
        return await self.repository.update_user_by_id(id=id, data=data.model_dump(exclude_none=True))
    
