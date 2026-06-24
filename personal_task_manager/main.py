from fastapi import FastAPI

import database

from routers.auth_router import router as auth_router
from routers.task_router import router as task_router

app = FastAPI()


@app.on_event("startup")
def startup():
    database.init_db()


app.include_router(auth_router)
app.include_router(task_router)