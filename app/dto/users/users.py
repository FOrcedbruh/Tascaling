from pydantic import BaseModel, Field, field_validator
from starlette.exceptions import HTTPException
from datetime import datetime

class UserReadSchema(BaseModel):
    username: str = Field(min_length=4, max_length=20)
    age: int
    avatar: str | None = None
    tasks: None = None
    ideas: None = None

    created_at: datetime


class UserUpdateSchema(BaseModel):
    username: str | None = None
    age: int | None = None
    avatar: str | None = None

    @field_validator("age")
    @classmethod
    def validate_age(cls, age):
        if age > 100:
            raise HTTPException(
                detail="Age too large",
                status_code=400
            )
        return age

