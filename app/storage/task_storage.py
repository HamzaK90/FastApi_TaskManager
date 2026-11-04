from app.models.task import Task


class TaskStorage:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def next_id(self) -> int:
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def save(self, task: Task) -> None:
        self._tasks[task.id] = task

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None
