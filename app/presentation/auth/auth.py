from fastapi import APIRouter, Depends, Body
from app.dto.auth.auth import LoginSuccessSchema, LoginSchema, RegistrationSchema, RerfreshTokenRequestSchema
from app.services import AuthService
from app.depends import get_auth_service
from starlette.requests import Request
from app.dto.users.users import UserOnlyReadSchema


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginSuccessSchema)
async def login(
    user: LoginSchema = Body(),
    auth_service: AuthService = Depends(get_auth_service)
) -> LoginSuccessSchema:
    return await auth_service.login(data=user)


@router.post("/registration", response_model=LoginSuccessSchema)
async def registration(
    user: RegistrationSchema = Body(),
    auth_service: AuthService = Depends(get_auth_service)
) -> LoginSuccessSchema:
    return await auth_service.registration(data=user)


@router.post("/refresh", response_model=LoginSuccessSchema, response_model_exclude_none=True)
async def refresh(
    data: RerfreshTokenRequestSchema = Body(),
    auth_service: AuthService = Depends(get_auth_service)
) -> LoginSuccessSchema:
    return await auth_service.refresh(refresh_token=data.refresh_token)


@router.get("/me", response_model=UserOnlyReadSchema)
async def get_me(
    request: Request,
    auth_service: AuthService = Depends(get_auth_service)
) -> UserOnlyReadSchema:
    return await auth_service.me(user=request.user)
