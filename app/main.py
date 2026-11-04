from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions import TaskNotFoundError
from app.routers.routes import router as tasks_router

app = FastAPI(
    title="Task Management API",
    description="A RESTful API for managing to-do tasks.",
    version="1.0.0",
)

app.include_router(tasks_router)


@app.exception_handler(TaskNotFoundError)
def handle_task_not_found(request: Request, exc: TaskNotFoundError) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)})
