from fastapi import FastAPI 


app = FastAPI(
    title="Task Management API",
    description="A RESTful app for managing a to-do tasks.",
    version="1.0.0",
)