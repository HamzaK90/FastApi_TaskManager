from typing import Annotated

from fastapi import Depends

from app.services.task_service import TaskService
from app.storage.task_storage import TaskStorage


task_storage = TaskStorage()


def get_task_service() -> TaskService:
    return TaskService(task_storage)


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]
