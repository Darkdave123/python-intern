import sqlite3


def get_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """)


def db_get_all_tasks(status=None):
    with get_connection() as conn:
        cursor = conn.cursor()

        if status:
            cursor.execute(
                "SELECT * FROM tasks WHERE status = ?",
                (status,)
            )
        else:
            cursor.execute(
                "SELECT * FROM tasks"
            )

        return [dict(row) for row in cursor.fetchall()]


def db_get_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None


def db_create_task(task):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO tasks (title, status)
            VALUES (?, ?)
            """,
            (task.title, "pending")
        )

        task_id = cursor.lastrowid

    return db_get_task(task_id)


def db_update_task(task_id, task):
    existing = db_get_task(task_id)

    if not existing:
        return None

    title = task.title if task.title is not None else existing["title"]
    status = task.status if task.status is not None else existing["status"]

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET title = ?, status = ?
            WHERE id = ?
            """,
            (title, status, task_id)
        )

    return db_get_task(task_id)


def db_delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        return cursor.rowcount > 0
