from fastapi import APIRouter
from app.presentation.users.users import router as UsersRouter
from app.presentation.auth.auth import router as AuthRouter


router = APIRouter(prefix="/api/v1")
router.include_router(router=UsersRouter)
router.include_router(router=AuthRouter)