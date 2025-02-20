from fastapi import APIRouter
from app.presentation.users.users import router as UsersRouter

router = APIRouter(prefix="/api/v1")
router.include_router(router=UsersRouter)