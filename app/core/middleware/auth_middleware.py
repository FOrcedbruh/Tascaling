from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.types import ASGIApp
from starlette.requests import Request
from starlette.responses import Response
from app.repositories import UsersRepository
from app.models import User
from app.utils.jwt.encode_decode import decode_jwt
from fastapi.security import HTTPBearer
from starlette.exceptions import HTTPException



class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, dispatch: DispatchFunction | None = None):
        super().__init__(app, dispatch)
        
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        user_repository: UsersRepository = UsersRepository()
        request.scope["user"] = await get_user(request, user_repository)
        
        return await call_next(request)


async def get_user(request: Request, repository: UsersRepository) -> User:
    token: str = request.headers.get("authorization", "").replace("Bearer ", "")
    if not token:
        return None
    
    payload: dict = decode_jwt(token)
    user = await repository.get_one_by_id(id=int(payload["sub"]))
    if not user:
        return None
    return user

class AuthHTTPBearer(HTTPBearer):
    async def __call__(self, request: Request):
        if not request.user:
            raise HTTPException(
                status_code=401,
                detail="Unauthorizied"
            )