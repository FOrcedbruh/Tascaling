from fastapi import APIRouter, Depends, Body
from app.dto.auth.auth import LoginSuccessSchema, LoginSchema, RegistrationSchema
from app.services import AuthService
from app.depends import get_auth_service

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
