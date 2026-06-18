from urllib.error import HTTPError


# In-memory database
tasks: dict[int, dict] = {
    1: {"title": "Buy milk", "completed": False},
    2: {"title": "Learn Pydantic", "completed": True},
    3: {"title": "Build API", "completed": False}
}


def get_or_404(collection: dict[int, dict], id: int) -> dict:
    if id in collection:
        return collection[id]

    raise HTTPError(
        url="",
        code=404,
        msg=f"Item with ID {id} not found",
        hdrs=None,
        fp=None
    )


# Test with valid ID
try:
    task: dict = get_or_404(tasks, 2)
    print("Found:", task)

except HTTPError as e:
    print(f"Error {e.code}: {e.msg}")


# Test with invalid ID
try:
    task: dict = get_or_404(tasks, 99)
    print("Found:", task)

except HTTPError as e:
    print(f"Error {e.code}: {e.msg}")