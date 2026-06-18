import sqlite3

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()

    # Delete student by name
    cursor.execute(
        "DELETE FROM students WHERE name = ?",
        ("Alice",)
    )

    # Retrieve remaining students
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("Remaining Students:")

    for student in students:
        print(
            f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}"
        )