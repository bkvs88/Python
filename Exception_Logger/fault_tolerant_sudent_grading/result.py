from student import SUBJECTS


def calculate_total(marks):
    """Calculate the sum of all subject marks.

    Args:
        marks: Iterable of numeric marks for a student.

    Returns:
        The total marks as a float.

    Raises:
        ValueError: If no marks are provided.
    """
    if not marks:
        raise ValueError("No marks provided for calculation")
    return sum(float(m) for m in marks)


def calculate_percentage(total):
    """Calculate the percentage from the total marks.

    Args:
        total: The total marks obtained.

    Returns:
        The percentage out of 100.

    Raises:
        ValueError: If the subject list is empty.
        ZeroDivisionError: If there are no subjects to divide by.
    """
    if not SUBJECTS:
        raise ValueError("Subject list is empty")
    subjects_count = len(SUBJECTS)
    if subjects_count == 0:
        raise ZeroDivisionError("Cannot divide by zero subject count")
    return total / subjects_count


def assign_grade(percentage):
    """Map a percentage to a letter grade.

    Args:
        percentage: The student's percentage (0-100).

    Returns:
        A letter grade: A+, A, B, C, D, or F.
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def determine_pass_fail(marks):
    """Determine whether a student passes all subjects.

    Students pass only if each subject mark is 40 or above.

    Args:
        marks: Iterable of marks for the student's subjects.

    Returns:
        True if all subjects are passed, False otherwise.
    """
    for subject, mark in zip(SUBJECTS, marks):
        if mark < 40:
            return False
    return True


def compute_result(student):
    """Compute total, percentage, grade, and pass/fail status for a student.

    Args:
        student: A student record dict with a 'marks' list.

    Returns:
        A dict with keys 'total', 'percentage', 'grade', and 'passed'.
    """
    marks = student["marks"]
    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = assign_grade(percentage)
    passed = determine_pass_fail(marks)

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "passed": passed,
    }
