import sqlite3

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (70,)
    )

    students = cursor.fetchall()

    for student in students:
        print(
            f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}"
        )