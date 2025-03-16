from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware.auth_middleware import AuthMiddleware
from app.core.middleware.auth_middleware import AuthHTTPBearer

__all__ = (
    "middlewares",
    "AuthHTTPBearer"
)


middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_credentials = True,
        allow_headers = ["*"],
    ),
    Middleware(AuthMiddleware),
]
