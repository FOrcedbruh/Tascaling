from contextlib import asynccontextmanager
import aerich
from app.core.db import DB_CONFIG
from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app: FastAPI):
    # aerich_command = aerich.Command(
    #     tortoise_config=DB_CONFIG,
    #     location="../../migrations"
    # )
    # await aerich_command.init()
    # await aerich_command.upgrade()
    yield