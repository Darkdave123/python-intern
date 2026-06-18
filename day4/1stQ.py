from pydantic import BaseModel, ValidationError


class TaskModel(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False


def main() -> None:
    print("=== Valid Task ===")

    try:
        task: TaskModel = TaskModel(
            title="Buy milk",
            priority="high",
            completed=True
        )

        print(task)
        print(task.model_dump())

    except ValidationError as e:
        print("Validation Error:")
        print(e)

    print("\n=== Invalid Task ===")

    try:
        invalid_task: TaskModel = TaskModel(
            title=123,
            priority=["high"],
            completed="yes"
        )

        print(invalid_task)

    except ValidationError as e:
        print("Validation Error:")
        print(e)


main()