from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

from database import init_db
from routers import auth_router, task_router

app = FastAPI()

init_db()


@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"{process_time:.4f}s"
    )

    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth_router.router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    task_router.router,
    prefix="/tasks",
    tags=["Tasks"]
)