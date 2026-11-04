from dataclasses import replace

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.storage.task_storage import TaskStorage
from app.exceptions import TaskNotFoundError




class TaskService:
    def __init__(self, storage: TaskStorage) -> None:
        self._storage = storage

    def create_task(self, data: TaskCreate) -> Task:
        task = Task(
            id=self._storage.next_id(),
            title=data.title,
            description=data.description,
            completed=False,
        )
        self._storage.save(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self._storage.list_all()

    def get_task(self, task_id: int) -> Task:
        task = self._storage.get(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)
        return task

    def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        changes = data.model_dump(exclude_unset=True)
        updated_task = replace(task, **changes)
        self._storage.save(updated_task)
        return updated_task

    def delete_task(self, task_id: int) -> None:
        if not self._storage.delete(task_id):
            raise TaskNotFoundError(task_id)
