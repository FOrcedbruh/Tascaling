from app.repositories import StatisticRepository
from app.dto.statistics.statistics import StatsReadSchema
from app.utils.cache_service import RedisCacheService
from starlette.requests import Request


class StatisticService:

    def __init__(self, repository: StatisticRepository, cache_service: RedisCacheService):
        self.repository = repository
        self.cache_service = cache_service

    async def get_stats(self, user_id: int, request: Request) -> StatsReadSchema:
        res = await self.cache_service.get(key=str(request.url).encode())
        if not res:
            res = await self.repository.calculate_and_get_statistics(user_id)
            await self.cache_service.set(key=str(request.url).encode(), value=res.__dict__)
        return res