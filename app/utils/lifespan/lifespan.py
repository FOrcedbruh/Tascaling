from contextlib import asynccontextmanager
import aerich
from app.core.db import DB_CONFIG




@asynccontextmanager
async def lifespan():
    aerich_command = aerich.Command(
        tortoise_config=DB_CONFIG,
        location="../../migrations"
    )
    await aerich_command.init()
    await aerich_command.upgrade()
    yield