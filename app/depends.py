from app.repositories import UsersRepository, TasksRepository
from app.services import UsersService, AuthService, TasksService
from fastapi import Depends



def get_user_repository() -> UsersRepository:
    return UsersRepository()

def get_tasks_repository() -> TasksRepository:
    return TasksRepository()

def get_user_service(repository: UsersRepository = Depends(get_user_repository)) -> UsersService:
    return UsersService(repository=repository)

def get_auth_service(repository: UsersRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(repository=repository)

def get_tasks_service(repository: TasksRepository = Depends(get_tasks_repository)) -> TasksService:
    return TasksService(repository=repository)