from exceptions import InvalidMarksError, MissingStudentInfoError

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]


def create_student(name, roll_number, marks):
    """Build a student record dict from a name, roll number, and marks list.

    Args:
        name: The student's name.
        roll_number: The student's roll number.
        marks: List of marks for the student's subjects.

    Returns:
        A dict with keys 'name', 'roll_number', and 'marks'.
    """
    return {"name": name, "roll_number": roll_number, "marks": marks}


def parse_marks(raw_marks):
    """Validate and convert a raw marks string to a float between 0 and 100.

    Args:
        raw_marks: String value to validate and parse.

    Returns:
        The marks as a float.

    Raises:
        InvalidMarksError: If the value is empty, non-numeric, or out of range.
    """
    if not raw_marks.strip():
        raise InvalidMarksError("Marks field is empty")

    try:
        marks = float(raw_marks)
    except ValueError:
        raise InvalidMarksError(f"'{raw_marks}' is not a valid number")

    if marks < 0 or marks > 100:
        raise InvalidMarksError(f"Marks {marks} is outside the valid range 0-100")

    return marks


def get_student_from_input(raw_values):
    """Build a validated student record dict from a list of raw string values.

    Args:
        raw_values: List containing name, roll number, and 5 subject marks
            as strings.

    Returns:
        A dict with keys 'name', 'roll_number', and 'marks' (parsed floats).

    Raises:
        MissingStudentInfoError: If the record has too few fields, or the name
            or roll number is missing.
        InvalidMarksError: If any of the marks is invalid.
    """
    if len(raw_values) < 2 + 5:
        raise MissingStudentInfoError(
            "Expected name, roll number, and 5 subject marks"
        )

    name = raw_values[0].strip()
    roll_number = raw_values[1].strip()

    if not name:
        raise MissingStudentInfoError("Student name is missing")

    if not roll_number:
        raise MissingStudentInfoError("Student roll number is missing")

    marks = [parse_marks(m) for m in raw_values[2:7]]

    return create_student(name, roll_number, marks)
