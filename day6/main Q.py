import sqlite3


def create_table():
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            marks INTEGER
        )
        """)


def insert_student(name, marks):
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, marks) VALUES (?, ?)",
            (name, marks)
        )


def get_all_students():
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )


def get_student_by_id(student_id):
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
        else:
            print("Student not found.")


def update_marks(student_id, new_marks):
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE students SET marks = ? WHERE id = ?",
            (new_marks, student_id)
        )

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Marks updated successfully.")


def delete_student(student_id):
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student deleted successfully.")


def get_students_above(threshold):
    with sqlite3.connect("school1.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE marks > ?",
            (threshold,)
        )

        students = cursor.fetchall()

        if not students:
            print("No matching students found.")
            return

        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )


create_table()

while True:
    print("\n--- Student Database System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Get Student By ID")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Students Above Threshold")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        insert_student(name, marks)

    elif choice == "2":
        get_all_students()

    elif choice == "3":
        student_id = int(input("Enter ID: "))
        get_student_by_id(student_id)

    elif choice == "4":
        student_id = int(input("Enter ID: "))
        new_marks = int(input("Enter new marks: "))
        update_marks(student_id, new_marks)

    elif choice == "5":
        student_id = int(input("Enter ID: "))
        delete_student(student_id)

    elif choice == "6":
        threshold = int(input("Enter threshold: "))
        get_students_above(threshold)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")