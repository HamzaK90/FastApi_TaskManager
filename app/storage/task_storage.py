from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task


class TaskStorage:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, task: Task) -> Task:
        self._session.add(task)
        self._session.commit()
        return task

    def get(self, task_id: int) -> Task | None:
        return self._session.get(Task, task_id)

    def list_all(self) -> list[Task]:
        return list(self._session.scalars(select(Task).order_by(Task.id)))

    def save(self, task: Task) -> Task:
        self._session.commit()
        return task

    def delete(self, task: Task) -> None:
        self._session.delete(task)
        self._session.commit()
