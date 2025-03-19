from fastapi import APIRouter
from app.presentation.users.users import router as UsersRouter
from app.presentation.auth.auth import router as AuthRouter
from app.presentation.tasks.tasks import router as TasksRouter
from app.presentation.statistics.statistics import router as StatsRouter

router = APIRouter(prefix="/api/v1")
router.include_router(router=UsersRouter)
router.include_router(router=AuthRouter)
router.include_router(router=TasksRouter)
router.include_router(router=StatsRouter)