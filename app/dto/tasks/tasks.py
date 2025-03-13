from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from app.models.tasks.tasks import TaskStatus
from starlette.exceptions import HTTPException



class TaskReadSchema(BaseModel):
    title: str = Field(max_length=100)
    description: str | None = Field(max_length=600, default=None)
    date_to_complete: datetime | None
    status: TaskStatus
    user_id: int
    created_at: datetime



class TaskCreateSchema(BaseModel):
    title: str = Field(max_length=100)
    description: str | None = Field(max_length=600, default=None)
    date_to_complete: datetime | None = None
    user_id: int

    @field_validator("date_to_complete")
    @classmethod
    def check_date(cls, value):
        if value <= datetime.now():
            raise HTTPException(
                status_code=400,
                detail="Impossible date_to_complete"
            )
        return value



class TaskUpdateSchema(BaseModel):
    title: str | None = Field(max_length=100, default=None)
    description: str | None = Field(max_length=600, default=None)
    date_to_complete: datetime | None = None
    status: TaskStatus  | None = None

    @field_validator("date_to_complete")
    @classmethod
    def check_date(cls, value):
        if value <= datetime.now():
            raise HTTPException(
                status_code=400,
                detail="Impossible date_to_complete"
            )
        return value