from fastapi import FastAPI
import sqlite3

app = FastAPI()


def init_db():
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
        """)


@app.on_event("startup")
def startup():
    init_db()


@app.post("/tasks")
def create_task(title: str):

    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )

        task_id = cursor.lastrowid

    return {
        "id": task_id,
        "title": title
    }


@app.get("/tasks")
def get_tasks():

    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")

        return cursor.fetchall()