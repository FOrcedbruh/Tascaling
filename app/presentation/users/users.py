from fastapi import APIRouter, Query, Depends, Body
from app.dto.pagination.pagination import BaseParamsSchema
from app.dto.users.users import UserReadSchema, UserUpdateSchema
from app.depends import get_user_service
from app.services import UsersService

router = APIRouter(prefix="/users", tags=["Users"])



@router.get("/{id}", response_model=UserReadSchema)
async def get_user(
    id: int,
    tasks: bool | None = Query(default=None),
    ideas: bool | None = Query(default=None),
    user_service: UsersService = Depends(get_user_service)
) -> UserReadSchema:
    return await user_service.get_user_by_id(id=id, tasks=tasks, ideas=ideas)


@router.patch("/{id}", response_model=UserReadSchema)
async def update_user(
    id: int,
    user: UserUpdateSchema = Body(),
    user_service: UsersService = Depends(get_user_service)
) -> UserReadSchema:
    return await user_service.update_user_by_id(id=id, data=user)