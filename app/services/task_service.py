from app.exceptions import TaskNotFoundError, UserNotFoundError
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.storage.task_storage import TaskStorage
from app.storage.user_storage import UserStorage
from app.schemas.tag import TagsAdd
from app.storage.tag_storage import TagStorage



class TaskService:
    def __init__(self, storage: TaskStorage, user_storage: UserStorage, tag_storage: TagStorage) -> None:
        self._storage = storage
        self._user_storage = user_storage
        self._tag_storage = tag_storage

    def create_task(self, data: TaskCreate) -> Task:
        if self._user_storage.get(data.user_id) is None:
            raise UserNotFoundError(data.user_id)
        task = Task(
            user_id=data.user_id,
            title=data.title,
            description=data.description,
            tags=self._tag_storage.get_or_build(data.tags),
        )
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

    def add_tags(self, task_id: int, data: TagsAdd) -> Task:
        task = self.get_task(task_id)
        for tag in self._tag_storage.get_or_build(data.tags):
            if tag not in task.tags:
                task.tags.append(tag)
        return self._storage.save(task)
