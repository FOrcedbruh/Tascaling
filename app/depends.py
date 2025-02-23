from app.core.settings import Settings
from app.repositories import UsersRepository
from app.services import UsersService, AuthService
from fastapi import Depends




def get_user_repository() -> UsersRepository:
    return UsersRepository()


def get_user_service(repository: UsersRepository = Depends(get_user_repository)) -> UsersService:
    return UsersService(repository=repository)

def get_auth_service(repository: UsersRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(repository=repository)