from fastapi import APIRouter, status

from app.dependencies.user_dependencies import UserServiceDep
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskResponse
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

USER_NOT_FOUND = {status.HTTP_404_NOT_FOUND: {"description": "User not found"}}


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_409_CONFLICT: {"description": "Email already exists"}},
)
def create_user(data: UserCreate, service: UserServiceDep) -> User:
    return service.create_user(data)


@router.get("/{user_id}", response_model=UserResponse, responses=USER_NOT_FOUND)
def get_user(user_id: int, service: UserServiceDep) -> User:
    return service.get_user(user_id)


@router.get("/{user_id}/tasks", response_model=list[TaskResponse], responses=USER_NOT_FOUND)
def list_user_tasks(user_id: int, service: UserServiceDep) -> list[Task]:
    return service.list_user_tasks(user_id)
