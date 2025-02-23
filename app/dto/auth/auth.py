from pydantic import BaseModel, Field, field_validator
from starlette.exceptions import HTTPException

class LoginSchema(BaseModel):
    username: str = Field(max_length=12)
    password: str = Field(min_length=6)

class RegistrationSchema(LoginSchema):
    age: int

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
    sub: int = Field(alias="id")


class JWTPayloadRefreshSchema(BaseModel):
    sub: int = Field(alias="id")

class LoginSuccessSchema(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None