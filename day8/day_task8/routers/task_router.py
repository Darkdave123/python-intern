from fastapi import APIRouter, Depends, HTTPException
from database import get_connection
from schemas import TaskCreate, TaskUpdate
from auth import get_current_user

router = APIRouter()


@router.post("/")
def create_task(
    task: TaskCreate,
    current_user: str = Depends(get_current_user)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(title, owner_email)
        VALUES (?,?)
        """,
        (
            task.title,
            current_user
        )
    )

    conn.commit()
    conn.close()

    return {"message": "Task created"}


@router.get("/")
def get_tasks(
    current_user: str = Depends(get_current_user)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE owner_email=?
        """,
        (current_user,)
    )

    tasks = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return tasks


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    current_user: str = Depends(get_current_user)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE id=? AND owner_email=?
        """,
        (task_id, current_user)
    )

    existing = cursor.fetchone()

    if not existing:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.execute(
        """
        UPDATE tasks
        SET title=?
        WHERE id=?
        """,
        (
            task.title,
            task_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "Task updated"}


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: str = Depends(get_current_user)
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE id=? AND owner_email=?
        """,
        (task_id, current_user)
    )

    existing = cursor.fetchone()

    if not existing:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Task deleted"}