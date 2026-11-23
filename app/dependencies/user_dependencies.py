from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.user_service import UserService
from app.storage.user_storage import UserStorage


def get_user_service(db: Annotated[Session, Depends(get_db)]) -> UserService:
    return UserService(UserStorage(db))


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
