from fastapi import APIRouter, Query, Depends, Body
from app.dto.pagination.pagination import BaseParamsSchema
from app.dto.users.users import UserReadSchema, UserUpdateSchema, UserQueryParamsSchema
from app.depends import get_user_service
from app.services import UsersService
from app.core.middleware import AuthHTTPBearer

secutiry = AuthHTTPBearer()

router = APIRouter(prefix="/users", tags=["Users"], dependencies=[Depends(secutiry)])



@router.get("/{id}", response_model=UserReadSchema, response_model_exclude_none=True)
async def get_user(
    id: int,
    params: UserQueryParamsSchema = Query(),
    user_service: UsersService = Depends(get_user_service)
) -> UserReadSchema:
    return await user_service.get_user_by_id(id, params)


@router.patch("/{id}", response_model=UserReadSchema)
async def update_user(
    id: int,
    user: UserUpdateSchema = Body(),
    user_service: UsersService = Depends(get_user_service)
) -> UserReadSchema:
    return await user_service.update_user_by_id(id=id, data=user)