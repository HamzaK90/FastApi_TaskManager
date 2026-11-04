class TaskNotFoundError(Exception):
    def __init__(self, task_id: int) -> None:
        super().__init__(f"Task with id {task_id} was not found.")
        self.task_id = task_id
