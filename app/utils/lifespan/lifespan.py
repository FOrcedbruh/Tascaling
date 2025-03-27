from contextlib import asynccontextmanager
import aerich
from app.core.db import DB_CONFIG
from fastapi import FastAPI
from app.utils.broker import KafkaClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    aerich_command = aerich.Command(
        tortoise_config=DB_CONFIG,
        location="app/migrations"
    )
    await aerich_command.init()
    await aerich_command.upgrade()
    yield