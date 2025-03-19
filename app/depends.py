from app.repositories import UsersRepository, TasksRepository, StatisticRepository
from app.services import UsersService, AuthService, TasksService, StatisticService
from fastapi import Depends
from app.utils.cache_service import RedisCacheService


def get_user_repository() -> UsersRepository:
    return UsersRepository()

def get_tasks_repository() -> TasksRepository:
    return TasksRepository()

def get_statistics_repository() -> StatisticRepository:
    return StatisticRepository()

def get_cache_service() -> RedisCacheService:
    return RedisCacheService()

def get_user_service(repository: UsersRepository = Depends(get_user_repository)) -> UsersService:
    return UsersService(repository=repository)

def get_auth_service(repository: UsersRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(repository=repository)

def get_tasks_service(repository: TasksRepository = Depends(get_tasks_repository)) -> TasksService:
    return TasksService(repository=repository)

def get_statistics_service(repository: StatisticRepository = Depends(get_statistics_repository), cache_service: RedisCacheService = Depends(get_cache_service)) -> StatisticService:
    return StatisticService(repository=repository, cache_service=cache_service)

