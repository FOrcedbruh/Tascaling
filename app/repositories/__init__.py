__all__ = (
    "UsersRepository",
    "TasksRepository",
    "StatisticRepository"
)

from app.repositories.users.users import UsersRepository
from app.repositories.tasks.tasks import TasksRepository
from app.repositories.statistics.statistics import StatisticRepository