from fastapi import FastAPI
import uvicorn
from app.depends import get_settings
from app.utils.lifespan.lifespan import lifespan
from app.presentation import router
from app.utils.exceptions.base import BaseException
from starlette.requests import Request
from starlette.exceptions import HTTPException

settings = get_settings()


app = FastAPI(
    title="Tascaling",
    description="Server side of Tascaling application",
    lifespan=lifespan,
    docs_url="/swagger"
)
app.include_router(router=router)

@app.exception_handler(BaseException)
async def exc_handler(request: Request, exception: BaseException):
    raise HTTPException(
        status_code=exception.status,
        detail=exception.detail
    )

@app.get("/")
async def index():
    return {
        "message": "Welcome to app!"
    }


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.run.port), host=str(settings.run.host), reload=True)