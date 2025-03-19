from pydantic import BaseModel, Field



class StatsCreateSchema(BaseModel):
    user_id: int
    completed_tasks: int = Field(default=0)
    total_tasks: int = Field(default=0)
    total_ideas: int = Field(default=0)
    activity: int = Field(default=0)


class StatsReadSchema(StatsCreateSchema):
    id: int
    completed_tasks: int
    total_ideas: int
    total_tasks: int
    activity: int



class StatsUpdateSchema(BaseModel):
    completed_tasks: int | None = None
    total_ideas: int | None = None
    total_tasks: int | None = None
    activity: int | None = None