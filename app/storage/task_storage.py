from sqlalchemy import Select
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

    def find(self, query: Select[tuple[Task]]) -> list[Task]:
        return list(self._session.scalars(query))
    
    def save(self, task: Task) -> Task:
        self._session.commit()
        return task

    def delete(self, task: Task) -> None:
        self._session.delete(task)
        self._session.commit()
