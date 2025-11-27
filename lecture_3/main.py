from typing import List, Dict, Any, Optional, Union


def main() -> None:
    """Handles user interaction and menu navigation for the Student Grade Analyzer.

    This function runs the main program loop, displaying the menu and processing
    user choices until the user selects the exit option.
    """
    student_list: List[Dict[str, Any]] = []
    while True:
        display_menu()
        user_choice: int = get_menu_choice()
        handle_user_choice(user_choice, student_list)


def display_menu() -> None:
    """Displays the main menu options to the user."""
    print("\n----- Student Grade Analyzer -----")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")


def get_menu_choice() -> int:
    """Gets and validates the user's menu choice.

    Returns:
        int: The validated menu choice entered by the user.
    """
    while True:
        try:
            return int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number")


def handle_user_choice(choice: int, students: List[Dict[str, Any]]) -> None:
    """Processes the user's menu selection.

    Args:
        choice: The menu option selected by the user.
        students: List of student dictionaries containing name and grades.
    """
    options: Dict[int, Any] = {
        1: lambda: add_new_student(students),
        2: lambda: add_student_grades(students),
        3: lambda: generate_full_report(students),
        4: lambda: find_best_student(students),
        5: lambda: exit_program(),
    }

    action = options.get(choice, invalid_choice)
    action()


def add_new_student(student_list: List[Dict[str, Any]]) -> None:
    """Adds a new student to the student list.

    Args:
        student_list: List of student dictionaries to add the new student to.
    """
    name: Optional[str] = get_valid_student_name(student_list)
    if name:
        student_list.append({"name": name, "grades": []})
        print(f"Student '{name}' added successfully")


def get_valid_student_name(students: List[Dict[str, Any]]) -> Optional[str]:
    """Gets a valid and non-duplicate student name from user input.

    Args:
        students: List of existing students to check for duplicates.

    Returns:
        Optional[str]: Valid student name or None if duplicate exists.
    """
    while True:
        name_input: str = input("Enter student name: ").strip()

        if not is_valid_name(name_input):
            print("Please enter a valid name (not empty and not just numbers)")
            continue

        if is_duplicate_name(name_input, students):
            print("This student name already exists")
            return None

        return name_input


def is_valid_name(name: str) -> bool:
    """Validates that a name is not empty and not just numbers.

    Args:
        name: The name string to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    return bool(name and not name.isdigit())


def is_duplicate_name(name: str, student_list: List[Dict[str, Any]]) -> bool:
    """Checks if a student name already exists in the list.

    Args:
        name: The name to check for duplicates.
        student_list: List of existing students.

    Returns:
        bool: True if duplicate exists, False otherwise.
    """
    return any(name == student["name"] for student in student_list)


def add_student_grades(student_list: List[Dict[str, Any]]) -> None:
    """Adds grades for a specific student.

    Args:
        student_list: List of student dictionaries to search for the student.
    """
    name: str = input("Enter student name: ").strip()
    student: Optional[Dict[str, Any]] = find_student_by_name(name, student_list)

    if not student:
        print("Student not found in records")
        return

    add_grades_to_student(student)


def find_student_by_name(
    name: str, students: List[Dict[str, Any]]
) -> Optional[Dict[str, Any]]:
    """Finds a student by name in the student list.

    Args:
        name: The name of the student to find.
        students: List of student dictionaries to search.

    Returns:
        Optional[Dict[str, Any]]: The student dictionary if found, None otherwise.
    """
    for person in students:
        if person["name"] == name:
            return person
    return None


def add_grades_to_student(student: Dict[str, Any]) -> None:
    """Adds multiple grades to a student's record.

    Args:
        student: The student dictionary to add grades to.
    """
    print("Enter grades (0-100). Type 'done' to finish:")

    while True:
        grade_input: str = input("Grade: ")

        if grade_input.lower() == "done":
            break

        grade_value: Optional[int] = validate_grade_input(grade_input)
        if grade_value is not None:
            student["grades"].append(grade_value)
            print(f"Grade {grade_value} added")


def validate_grade_input(input_string: str) -> Optional[int]:
    """Validates and converts grade input to integer.

    Args:
        input_string: The string input representing a grade.

    Returns:
        Optional[int]: Validated grade as integer, or None if invalid.
    """
    try:
        grade: int = int(input_string)
        if 0 <= grade <= 100:
            return grade
        else:
            print("Grade must be between 0 and 100")
    except ValueError:
        print("Please enter a valid number")
    return None


def generate_full_report(student_list: List[Dict[str, Any]]) -> None:
    """Generates a comprehensive report of all students and statistics.

    Args:
        student_list: List of student dictionaries to generate report from.
    """
    print("\n----- Student Report -----")

    if not student_list:
        print("No students in records")
        return

    display_student_grades(student_list)

    if has_graded_students(student_list):
        display_statistics(student_list)


def display_student_grades(students: List[Dict[str, Any]]) -> None:
    """Displays the average grade for each student.

    Args:
        students: List of student dictionaries to display.
    """
    for person in students:
        avg: Union[float, str] = calculate_average_grade(person["grades"])
        print(f"{person['name']}'s average grade: {avg}")


def calculate_average_grade(grades: List[int]) -> Union[float, str]:
    """Calculates the average grade from a list of grades.

    Args:
        grades: List of integer grades.

    Returns:
        Union[float, str]: Average grade as float or 'N/A' if no grades.
    """
    if not grades:
        return "N/A"
    return sum(grades) / len(grades)


def has_graded_students(student_list: List[Dict[str, Any]]) -> bool:
    """Checks if there are any students with grades.

    Args:
        student_list: List of student dictionaries to check.

    Returns:
        bool: True if at least one student has grades, False otherwise.
    """
    return any(student["grades"] for student in student_list)


def display_statistics(student_list: List[Dict[str, Any]]) -> None:
    """Displays statistics including highest, lowest, and class average.

    Args:
        student_list: List of student dictionaries to calculate statistics from.
    """
    averages: List[float] = []
    for person in student_list:
        if person["grades"]:
            avg: float = sum(person["grades"]) / len(person["grades"])
            averages.append(avg)

    if averages:
        print("-------------------------------")
        print(f"Highest Average: {max(averages):.1f}")
        print(f"Lowest Average: {min(averages):.1f}")
        print(f"Class Average: {sum(averages) / len(averages):.1f}")
        print("-------------------------------")


def find_best_student(student_list: List[Dict[str, Any]]) -> None:
    """Finds and displays the student with the highest average grade.

    Args:
        student_list: List of student dictionaries to search.
    """
    if not student_list:
        print("No students in records")
        return

    graded_students: List[Dict[str, Any]] = [s for s in student_list if s["grades"]]

    if not graded_students:
        print("No students have grades yet")
        return

    best: Dict[str, Any] = find_top_performer(graded_students)
    display_top_student(best)


def find_top_performer(students_with_grades: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Finds the student with the highest average grade.

    Args:
        students_with_grades: List of students who have grades.

    Returns:
        Dict[str, Any]: The student dictionary with the highest average.
    """
    return max(students_with_grades, key=lambda s: sum(s["grades"]) / len(s["grades"]))


def display_top_student(student: Dict[str, Any]) -> None:
    """Displays information about the top performing student.

    Args:
        student: The top student dictionary to display.
    """
    average_score: float = sum(student["grades"]) / len(student["grades"])
    print(f"Top student: {student['name']} with average grade {average_score:.1f}")


def exit_program() -> None:
    """Exits the program with a farewell message."""
    print("Goodbye!")
    exit()


def invalid_choice() -> None:
    """Handles invalid menu choices by displaying an error message."""
    print("Invalid option selected")


if __name__ == "__main__":
    main()
