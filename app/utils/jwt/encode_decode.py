import jwt
from app.depends import get_settings
from datetime import datetime, UTC, timedelta



settings = get_settings()

def create_token(
    payload: dict,
    exp_minutes: int,
    algorithm: str = settings.jwt.algorithm,
    secret: str = settings.jwt.secret,
) -> str:
    payload["exp"] = datetime.now(UTC) + timedelta(minutes=exp_minutes)
    payload["iat"] = datetime.now(UTC)

    return jwt.encode(payload=payload, key=secret, algorithm=algorithm)

def decode_jwt(
    token: str,
    algorithm: str = settings.jwt.algorithm,
    secret: str = settings.jwt.secret
) -> dict:
    return jwt.decode(jwt=token, key=secret, algorithms=algorithm)

