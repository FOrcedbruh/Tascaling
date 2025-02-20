from app.core.settings import Settings
from app.repositories import UsersRepository
from app.services import UsersService
from fastapi import Depends


def get_settings() -> Settings:
    return Settings()


def get_user_repository() -> UsersRepository:
    return UsersRepository()


def get_user_service(repository: UsersRepository = Depends(get_user_repository)) -> UsersService:
    return UsersService(repository=repository)