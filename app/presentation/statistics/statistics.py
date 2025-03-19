from fastapi import APIRouter, Depends
from app.depends import get_statistics_service
from app.services import StatisticService
from app.dto.statistics.statistics import StatsReadSchema
from app.core.middleware import AuthHTTPBearer
from starlette.requests import Request

security = AuthHTTPBearer()


router = APIRouter(prefix="/statistics", tags=["Stats"], dependencies=[Depends(security)])


@router.get("/{user_id}", response_model=StatsReadSchema)
async def get_stats(
    user_id: int,
    request: Request,
    stats_service: StatisticService = Depends(get_statistics_service)
) -> StatsReadSchema:
    return await stats_service.get_stats(user_id=user_id, request=request)