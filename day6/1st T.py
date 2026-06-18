import sqlite3

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        marks INTEGER
    )
    """)

    # List of tuples
    students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("David", 88),
        ("Eva", 95)
    ]

    # Insert students using a loop
    for student in students:
        cursor.execute(
            "INSERT INTO students (name, marks) VALUES (?, ?)",
            student
        )

    print("5 students inserted successfully!")