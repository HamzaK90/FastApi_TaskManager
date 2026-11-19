from app.exceptions import TaskNotFoundError
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.storage.task_storage import TaskStorage


class TaskService:
    def __init__(self, storage: TaskStorage) -> None:
        self._storage = storage

    def create_task(self, data: TaskCreate) -> Task:
        task = Task(title=data.title, description=data.description)
        return self._storage.add(task)

    def list_tasks(self) -> list[Task]:
        return self._storage.list_all()

    def get_task(self, task_id: int) -> Task:
        task = self._storage.get(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)
        return task

    def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(task, field, value)
        return self._storage.save(task)

    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        self._storage.delete(task)
