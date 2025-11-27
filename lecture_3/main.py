from typing import TypedDict


class Student(TypedDict):
    """Type definition for a student dictionary."""

    name: str
    grades: list[int]


def main() -> None:
    """Handles user interaction and menu navigation for the Student Grade Analyzer."""
    students: list[Student] = []
    while True:
        print("\n----- Student Grade Analyzer -----")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        choice = get_menu_choice()

        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            show_report(students)
        elif choice == 4:
            find_top_performer(students)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option selected")


def get_menu_choice() -> int:
    """Gets and validates menu choice from user.

    Returns:
        Validated integer choice from user.
    """
    while True:
        try:
            return int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number")


def add_student(students: list[Student]) -> None:
    """Adds a new student to the students list.

    Args:
        students: List of student dictionaries to add to.
    """
    student_name = input("Enter student name: ").strip()

    if not student_name or student_name.isdigit():
        print("Invalid input, please enter a valid student name")
        return

    # Check if student already exists
    for student in students:
        if student["name"] == student_name:
            print("This student already exists")
            return

    students.append(Student(name=student_name, grades=[]))
    print(f"Student '{student_name}' added successfully")


def add_grades(students: list[Student]) -> None:
    """Adds grades for a specific student.

    Args:
        students: List of student dictionaries to search.
    """
    student_name = input("Enter student name: ").strip()

    # Find the student
    student: Student | None = None
    for s in students:
        if s["name"] == student_name:
            student = s
            break

    if student is None:
        print("Student not found")
        return

    print("Enter grades (0-100). Type 'done' to finish:")

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == "done":
            break

        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
                print(f"Grade {grade} added")
            else:
                print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_report(students: list[Student]) -> None:
    """Generates and displays a report of all students and statistics.

    Args:
        students: List of student dictionaries to generate report from.
    """
    print("\n----- Student Report -----")

    if not students:
        print("No students in records")
        return

    averages: list[float] = []
    students_with_grades = 0

    for student in students:
        try:
            if student["grades"]:
                avg = sum(student["grades"]) / len(student["grades"])
                averages.append(avg)
                students_with_grades += 1
                print(f"{student['name']}'s average grade is {avg:.1f}.")
            else:
                print(f"{student['name']}'s average grade is N/A.")
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")

    if not averages:
        print("No students have grades yet")
        return

    print("---")
    print(f"Max Average: {max(averages):.1f}")
    print(f"Min Average: {min(averages):.1f}")
    print(f"Overall Average: {sum(averages) / len(averages):.1f}")


def find_top_performer(students: list[Student]) -> None:
    """Finds and displays the student with the highest average grade.

    Args:
        students: List of student dictionaries to search.
    """
    if not students:
        print("No students in records")
        return

    # Filter students who have grades
    students_with_grades = [s for s in students if s["grades"]]

    if not students_with_grades:
        print("No students have grades yet")
        return

    # Use max() with lambda function as specified
    try:
        top_student = max(
            students_with_grades,
            key=lambda student: sum(student["grades"]) / len(student["grades"]),
        )
        top_avg = sum(top_student["grades"]) / len(top_student["grades"])
        print(
            f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}."
        )
    except ZeroDivisionError:
        print("Error calculating averages")


if __name__ == "__main__":
    main()
