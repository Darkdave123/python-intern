from fastapi import FastAPI

from routers.tasks import router
from database import init_db

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


app.include_router(
    router,
    prefix="/tasks",
    tags=["Tasks"]
)

