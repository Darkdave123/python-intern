def calculate_average(
    math: int,
    physics: int,
    java: int,
    dbms: int,
    oops: int
) -> float:
    return (math + physics + java + dbms + oops) / 5


def get_grade(average: float) -> str:
    if average >= 90:
        return "Grade A"
    elif average >= 80:
        return "Grade B"
    elif average >= 70:
        return "Grade C"
    elif average >= 60:
        return "Grade D"
    else:
        return "Grade F"


def main() -> None:
    name: str = input("Enter name of student: ")

    math: int = int(input("Enter marks in Math: "))
    physics: int = int(input("Enter marks in Physics: "))
    java: int = int(input("Enter marks in JAVA: "))
    dbms: int = int(input("Enter marks in DBMS: "))
    oops: int = int(input("Enter marks in OOPS: "))

    average: float = calculate_average(
        math, physics, java, dbms, oops
    )

    grade: str = get_grade(average)

    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(grade)


main()