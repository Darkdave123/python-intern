from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = {}
next_id = 1


@app.post("/tasks")
def create_task(title: str):
    global next_id

    task = {
        "id": next_id,
        "title": title
    }

    tasks[next_id] = task
    next_id += 1

    return task


@app.get("/tasks")
def get_tasks():
    return list(tasks.values())


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted",
        "task": deleted_task
    }