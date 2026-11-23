class TaskNotFoundError(Exception):
    def __init__(self, task_id: int) -> None:
        super().__init__(f"Task with id {task_id} was not found.")
        self.task_id = task_id

class UserNotFoundError(Exception):
    def __init__(self, user_id: int) -> None:
        super().__init__(f"User with id {user_id} was not found.")
        self.user_id = user_id


class EmailAlreadyExistsError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__(f"A user with email {email} already exists.")
        self.email = email
        