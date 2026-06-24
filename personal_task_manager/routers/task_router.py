from fastapi import APIRouter, Depends

import database
import auth
import schemas

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_task(
    task: schemas.TaskCreate,
    email: str = Depends(auth.get_current_user)
):

    conn = database.get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO tasks(
        title,
        description,
        priority,
        status,
        due_date,
        owner_email
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        task.title,
        task.description,
        task.priority,
        task.status,
        task.due_date,
        email
    ))

    conn.commit()
    conn.close()

    return {"message": "Task created"}


@router.get("/")
def get_tasks(
    email: str = Depends(auth.get_current_user)
):

    conn = database.get_connection()

    rows = conn.execute(
        "SELECT * FROM tasks WHERE owner_email=?",
        (email,)
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    email: str = Depends(auth.get_current_user)
):

    conn = database.get_connection()

    conn.execute(
        "DELETE FROM tasks WHERE id=? AND owner_email=?",
        (task_id, email)
    )

    conn.commit()
    conn.close()

    return {"message": "Deleted"}