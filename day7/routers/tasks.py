from fastapi import APIRouter, HTTPException

from schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from database import (
    db_get_all_tasks,
    db_get_task,
    db_create_task,
    db_update_task,
    db_delete_task
)

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
def get_tasks(status: str = None):
    return db_get_all_tasks(status)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):

    task = db_get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    return db_create_task(task)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):

    updated = db_update_task(task_id, task)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@router.delete("/{task_id}")
def delete_task(task_id: int):

    success = db_delete_task(task_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted"}

