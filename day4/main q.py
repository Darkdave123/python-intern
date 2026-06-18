from pydantic import BaseModel, ValidationError


# In-Memory Database
tasks: dict[int, dict] = {}
next_id: int = 1


# Custom Exception
class TaskNotFoundError(Exception):
    pass


# Pydantic Model
class Task(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False


# Get All Tasks
def get_all_tasks() -> list[dict]:
    return list(tasks.values())


# Get One Task
def get_task(id: int) -> dict:
    if id not in tasks:
        raise TaskNotFoundError(f"Task with ID {id} not found.")

    return tasks[id]


# Create Task
def create_task(data: dict) -> dict:
    global next_id

    task: Task = Task(**data)

    task_data: dict = task.model_dump()

    task_data["id"] = next_id

    tasks[next_id] = task_data

    next_id += 1

    return task_data


# Update Task
def update_task(id: int, data: dict) -> dict:
    if id not in tasks:
        raise TaskNotFoundError(f"Task with ID {id} not found.")

    updated_task: Task = Task(**data)

    task_data: dict = updated_task.model_dump()

    task_data["id"] = id

    tasks[id] = task_data

    return task_data


# Delete Task
def delete_task(id: int) -> bool:
    if id not in tasks:
        raise TaskNotFoundError(f"Task with ID {id} not found.")

    del tasks[id]

    return True


# CLI Menu
while True:
    print("\n===== TASK MANAGER =====")
    print("1. Create Task")
    print("2. View All Tasks")
    print("3. View Task By ID")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice: str = input("Enter choice: ")

    try:

        if choice == "1":
            title: str = input("Enter title: ")
            priority: str = input("Enter priority: ")

            task: dict = create_task({
                "title": title,
                "priority": priority
            })

            print("Created:", task)

        elif choice == "2":
            all_tasks: list[dict] = get_all_tasks()

            if not all_tasks:
                print("No tasks found.")
            else:
                for task in all_tasks:
                    print(task)

        elif choice == "3":
            task_id: int = int(input("Enter task ID: "))

            task: dict = get_task(task_id)

            print(task)

        elif choice == "4":
            task_id: int = int(input("Enter task ID: "))

            title: str = input("Enter new title: ")
            priority: str = input("Enter new priority: ")

            updated: dict = update_task(
                task_id,
                {
                    "title": title,
                    "priority": priority
                }
            )

            print("Updated:", updated)

        elif choice == "5":
            task_id: int = int(input("Enter task ID: "))

            delete_task(task_id)

            print("Task deleted.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    except TaskNotFoundError as e:
        print("Error:", e)

    except ValidationError as e:
        print("\nValidation Error:")
        print(e)

    except ValueError:
        print("Please enter a valid number.")