from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions import EmailAlreadyExistsError, TaskNotFoundError, UserNotFoundError
from app.routers.users import router as users_router
from app.routers.routes import router as tasks_router

app = FastAPI(
    title="Task Management API",
    description="A RESTful API for managing to-do tasks.",
    version="1.0.0",
)

app.include_router(tasks_router)
app.include_router(users_router)


@app.exception_handler(TaskNotFoundError)
def handle_task_not_found(request: Request, exc: TaskNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)})

@app.exception_handler(UserNotFoundError)
def handle_user_not_found(request: Request, exc: UserNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)})


@app.exception_handler(EmailAlreadyExistsError)
def handle_email_exists(request: Request, exc: EmailAlreadyExistsError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})
