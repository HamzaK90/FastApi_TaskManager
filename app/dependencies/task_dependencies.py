from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.task_service import TaskService
from app.storage.task_storage import TaskStorage
from app.storage.user_storage import UserStorage


def get_task_service(db: Annotated[Session, Depends(get_db)]) -> TaskService:
    return TaskService(TaskStorage(db), UserStorage(db))


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]
