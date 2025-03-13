from pydantic import BaseModel, Field, field_validator
from starlette.exceptions import HTTPException
from datetime import datetime
from app.dto.tasks.tasks import TaskReadSchema
from typing import Any



class UserReadSchema(BaseModel):
    username: str = Field(min_length=4, max_length=20)
    age: int
    avatar: str | None = None
    tasks: list[TaskReadSchema] | None = None
    ideas: Any = None

    created_at: datetime

class UserQueryParamsSchema(BaseModel):
    tasks: bool = True
    ideas: bool = False


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

