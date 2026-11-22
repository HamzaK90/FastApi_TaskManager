from app.exceptions import EmailAlreadyExistsError, UserNotFoundError
from app.models.task import Task
from app.models.user import User
from app.schemas.user import UserCreate
from app.storage.user_storage import UserStorage


class UserService:
    def __init__(self, storage: UserStorage) -> None:
        self._storage = storage

    def create_user(self, data: UserCreate) -> User:
        if self._storage.get_by_email(data.email) is not None:
            raise EmailAlreadyExistsError(data.email)
        user = User(name=data.name, email=data.email)
        return self._storage.add(user)

    def get_user(self, user_id: int) -> User:
        user = self._storage.get(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return user

    def list_user_tasks(self, user_id: int) -> list[Task]:
        return self.get_user(user_id).tasks
