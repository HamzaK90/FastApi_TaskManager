from typing import Annotated

from fastapi import APIRouter, Query, status


from app.dependencies.task_dependencies import TaskServiceDep
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskFilters, TaskResponse, TaskUpdate
from app.schemas.tag import TagsAdd


router = APIRouter(prefix="/tasks", tags=["Tasks"])

TASK_NOT_FOUND = {status.HTTP_404_NOT_FOUND: {"description": "Task not found"}}


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, service: TaskServiceDep) -> Task:
    return service.create_task(data)


@router.get("", response_model=list[TaskResponse])
def list_tasks(filters: Annotated[TaskFilters, Query()], service: TaskServiceDep) -> list[Task]:
    return service.list_tasks(filters)


@router.get("/{task_id}", response_model=TaskResponse, responses=TASK_NOT_FOUND)
def get_task(task_id: int, service: TaskServiceDep) -> Task:
    return service.get_task(task_id)


@router.patch("/{task_id}", response_model=TaskResponse, responses=TASK_NOT_FOUND)
def update_task(task_id: int, data: TaskUpdate, service: TaskServiceDep) -> Task:
    return service.update_task(task_id, data)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, responses=TASK_NOT_FOUND)
def delete_task(task_id: int, service: TaskServiceDep) -> None:
    service.delete_task(task_id)

@router.post("/{task_id}/tags", response_model=TaskResponse, responses=TASK_NOT_FOUND)
def add_tags(task_id: int, data: TagsAdd, service: TaskServiceDep) -> Task:
    return service.add_tags(task_id, data)
