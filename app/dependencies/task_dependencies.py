from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.task_service import TaskService
from app.storage.task_storage import TaskStorage


def get_task_service(db: Annotated[Session, Depends(get_db)]) -> TaskService:
    return TaskService(TaskStorage(db))


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]
