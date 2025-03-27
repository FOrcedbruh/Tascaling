from pydantic import BaseModel, Field, field_validator, EmailStr
from starlette.exceptions import HTTPException

class LoginSchema(BaseModel):
    username: str = Field(max_length=12)
    password: str = Field(min_length=6)

class RegistrationSchema(LoginSchema):
    age: int
    email: EmailStr

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value > 100:
            raise HTTPException(
                status_code=400,
                detail="Age too large"
            )
        return value


class JWTPayloadAccessSchema(BaseModel):
    username: str
    age: int
    sub: str


class JWTPayloadRefreshSchema(BaseModel):
    sub: str


class RerfreshTokenRequestSchema(BaseModel):
    refresh_token: str

class LoginSuccessSchema(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None