from fastapi import FastAPI

from db import init_db

from routers import auth
from routers import tasks

app = FastAPI()

init_db()

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)