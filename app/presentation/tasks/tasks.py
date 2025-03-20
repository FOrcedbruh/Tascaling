from fastapi import APIRouter, Depends, Body, Query
from app.dto.tasks.tasks import TaskReadSchema, TaskCreateSchema, TaskUpdateSchema
from app.services import TasksService
from app.depends import get_tasks_service
from app.dto.pagination.pagination import BaseParamsSchema
from app.core.middleware import AuthHTTPBearer
from starlette.requests import Request

security = AuthHTTPBearer()

router = APIRouter(prefix="/tasks", tags=["Task"], dependencies=[Depends(security)])


@router.get("/{id}", response_model=TaskReadSchema)
async def get_task(
    id: int,
    tasks_service: TasksService = Depends(get_tasks_service),
) -> TaskReadSchema:
    return await tasks_service.get_task_by_id(id)


@router.post("/", response_model=TaskReadSchema)
async def create_task(
    data: TaskCreateSchema = Body(),
    tasks_service: TasksService = Depends(get_tasks_service)
) -> TaskReadSchema:
    return await tasks_service.create_task(data)


@router.patch("/{id}", response_model=TaskReadSchema)
async def update_task(
    id: int,
    data: TaskUpdateSchema = Body(),
    tasks_service: TasksService = Depends(get_tasks_service)
):
    return await tasks_service.update_task(data, id)

@router.get("/", response_model=list[TaskReadSchema])
async def get_all_tasks(
    query_params: BaseParamsSchema =  Query(),
    tasks_service: TasksService = Depends(get_tasks_service)
) -> list[TaskReadSchema]:
    return await tasks_service.get_all_tasks(query_params)



@router.delete("/{id}", response_model=dict)
async def delete_task(
    id: int,
    tasks_service: TasksService = Depends(get_tasks_service)
) -> dict:
    return await tasks_service.delete_task(id)