from logger import setup_logger
from student import get_student_from_input, SUBJECTS
from result import compute_result


def read_students_from_file(filepath):
    """Read student records from a CSV-formatted file.

    Args:
        filepath: Path to the file containing one student per line, with
            comma-separated values.

    Returns:
        A list of raw value lists, one per non-empty line in the file.
    """
    students = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw_values = line.split(",")
            students.append(raw_values)
    return students


def main():
    """Entry point: load a students file, grade each student, and print results.

    Invalid records are logged and skipped while processing continues.
    """
    logger = setup_logger()

    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <students_file>")
        return

    filepath = sys.argv[1]

    try:
        raw_students = read_students_from_file(filepath)
    except FileNotFoundError:
        logger.error(f"Data file not found: {filepath}")
        return

    print(f"{'Name':<15} {'Roll':<10} {'Total':<8} {'Percent':<10} {'Grade':<6} {'Status'}")
    print("-" * 65)

    for raw in raw_students:
        try:
            student = get_student_from_input(raw)
            result = compute_result(student)
            status = "PASS" if result["passed"] else "FAIL"
            print(
                f"{student['name']:<15} {student['roll_number']:<10} "
                f"{result['total']:<8.2f} {result['percentage']:<10.2f} "
                f"{result['grade']:<6} {status}"
            )
        except Exception as e:
            logger.error(f"Skipping invalid record {raw} : {e}")


if __name__ == "__main__":
    main()
