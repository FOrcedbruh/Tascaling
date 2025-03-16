from fastapi import APIRouter
from app.presentation.users.users import router as UsersRouter
from app.presentation.auth.auth import router as AuthRouter
from app.presentation.tasks.tasks import router as TasksRouter


router = APIRouter(prefix="/api/v1")
router.include_router(router=UsersRouter)
router.include_router(router=AuthRouter)
router.include_router(router=TasksRouter)