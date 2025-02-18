from fastapi import FastAPI
import uvicorn
from app.depends import get_settings
from app.utils.lifespan.lifespan import lifespan

settings = get_settings()



app = FastAPI(
    title="Tascaling",
    description="Server side of Tascaling application",
    lifespan=lifespan,
    docs_url="/swagger"
)

@app.get("/")
async def index():
    return {
        "message": "Welcome to app!"
    }

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=int(settings.run.port), host=str(settings.run.host), reload=True)