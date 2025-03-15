from pydantic import BaseModel



class BaseParamsSchema(BaseModel):
    limit: int = 100
    offset: int = 0
    order_by: str | None = "id"
    asc: bool | None = False
