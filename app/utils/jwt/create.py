from app.utils.jwt.encode_decode import create_token
from enum import Enum
from app.core.settings import get_settings
from app.dto.auth.auth import JWTPayloadAccessSchema, JWTPayloadRefreshSchema

settings = get_settings()


class TokenType(str, Enum):
    ACCESS = "ACCESS"
    REFRESH = "REFRESH"


def create_access_token(
    data: JWTPayloadAccessSchema,
    exp_minutes: int = settings.jwt.access_token_expired_minutes,
) -> str:
    payload = data.model_dump()
    payload["type"] = TokenType.ACCESS
    return create_token(payload=payload, exp_minutes=exp_minutes)


def create_refresh_token(
    data: JWTPayloadRefreshSchema,
    exp_minutes: int = settings.jwt.refresh_token_expired_minutes,
) -> str:
    payload = data.model_dump()
    payload["type"] = TokenType.REFRESH
    return create_token(payload=payload, exp_minutes=exp_minutes)