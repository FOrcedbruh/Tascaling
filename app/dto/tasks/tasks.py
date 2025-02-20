from pydantic import BaseModel, Field
from datetime import datetime


class TaskReadSchema(BaseModel):
    title: str = Field(max_length=100)
    description: str | None = Field(max_length=600, default=None)
    date_to_complete: datetime | None
    
