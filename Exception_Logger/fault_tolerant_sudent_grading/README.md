# Fault Tolerant Student Grading

A Python program that reads student details and marks for 5 subjects, then
calculates total marks, percentage, grade, and pass/fail status for each
student. The program is designed to be **fault tolerant**: invalid records are
logged and skipped instead of crashing the entire run.

## Features

- Reads student records from a CSV file (one student per line, comma-separated)
- Calculates total, percentage, grade, and pass/fail status
- Handles incorrect marks, non-numeric input, marks outside 0–100, missing
  student information, and division/calculation errors
- Uses custom exceptions for clearer error reporting
- Logs errors (instead of stopping) and continues processing remaining students
- Written without OOP — everything is implemented with plain functions and
  dict-based student records

## Project Structure

```
fault_tolerant_student_grading/
├── exceptions.py    # Custom exception definitions
├── logger.py        # Logging configuration
├── student.py       # Student input handling and validation
├── result.py        # Result calculations (total, percentage, grade, pass/fail)
├── main.py          # Entry point that ties the modules together
└── students.csv     # Example input data
```

## Usage

```
python3 main.py <students_file>
```

Example:

```
python3 main.py students.csv
```

### Input format

Each line in the input file must contain, in order:

```
Name, RollNumber, Maths, Physics, Chemistry, English, Computer
```

Example line:

```
Aarav,101,85,90,78,92,88
```

### Sample output

```
Name            Roll       Total    Percent    Grade  Status
-----------------------------------------------------------------
Aarav           101        433.00   86.60      A      PASS
Priya           102        295.00   59.00      D      PASS
Vikram          105        489.00   97.80      A+     PASS
Kavya           106        150.00   30.00      F      FAIL
```

Invalid records are logged to the console and to `grading_errors.log` while the
rest of the students continue to be processed.

## Modules

### `exceptions.py`

Defines the custom exceptions used across the package:

| Exception | Description |
| --- | --- |
| `InvalidMarksError` | Raised when a mark is empty, non-numeric, or outside the valid range 0–100. |
| `MissingStudentInfoError` | Raised when a record has too few fields, or the student name or roll number is missing. |

Custom exceptions are the one place classes are required — Python needs a class
to define a custom exception type.

### `logger.py`

Configures and returns the shared logger used by the package.

- Logs `ERROR` level messages to `grading_errors.log`
- Logs `INFO` level and above to the console
- Timestamps every entry using the format `YYYY-MM-DD HH:MM:SS,mmm - LEVEL - message`

### `student.py`

Handles all student input reading and validation.

| Function | Description |
| --- | --- |
| `create_student(name, roll_number, marks)` | Builds a student record dict with keys `name`, `roll_number`, `marks`. |
| `parse_marks(raw_marks)` | Validates a raw marks string and returns a float; raises `InvalidMarksError` for empty, non-numeric, or out-of-range values. |
| `get_student_from_input(raw_values)` | Parses a raw record (name, roll number, 5 marks) into a validated student dict; raises `MissingStudentInfoError` or `InvalidMarksError`. |

Students are represented as plain dicts:

```python
{"name": "Alice", "roll_number": "101", "marks": [85.0, 90.0, 78.0, 92.0, 88.0]}
```

### `result.py`

Performs all result calculations.

| Function | Description |
| --- | --- |
| `calculate_total(marks)` | Sums all subject marks; raises `ValueError` if no marks are provided. |
| `calculate_percentage(total)` | Divides total by the number of subjects; guards against empty/zero subject lists. |
| `assign_grade(percentage)` | Maps a percentage to A+, A, B, C, D, or F. |
| `determine_pass_fail(marks)` | Returns `True` only if every subject is 40 or above. |
| `compute_result(student)` | Combines the above into a result dict with keys `total`, `percentage`, `grade`, `passed`. |

### `main.py`

Entry point of the package.

| Function | Description |
| --- | --- |
| `read_students_from_file(filepath)` | Reads the input file and returns a list of raw value lists. |
| `main()` | Loads the file, grades each student, prints a results table, and logs+skips invalid records. |

## Exceptions used

The program raises and handles the following exceptions:

| Exception | Where it is raised | Why |
| --- | --- | --- |
| `InvalidMarksError` | `student.py` | Empty marks, non-numeric marks, or marks outside 0–100. |
| `MissingStudentInfoError` | `student.py` | Missing name/roll number, or fewer than 7 fields in a record. |
| `ValueError` (built-in) | `result.py` | No marks provided for total, or empty subject list for percentage. |
| `ZeroDivisionError` (built-in) | `result.py` | Guarded division when the subject count is zero. |
| `FileNotFoundError` (built-in) | `main.py` | The input data file does not exist. |
| `Exception` (catch-all) | `main.py` | Any other unexpected error per record — logged and skipped. |

## Logging behaviour

- Every invalid record is written to the log file `grading_errors.log` with an
  `ERROR` level and a timestamp.
- Errors are also echoed to the console for immediate visibility.
- Processing never stops on an error — each invalid record is skipped and the
  next student is processed.

Example log line:

```
2026-09-08 23:11:34,385 - ERROR - Skipping invalid record ['Carol', '103', '-5', '80', '90', '85', '95'] : Marks -5.0 is outside the valid range 0-100
```

## Grading rules

| Percentage | Grade |
| --- | --- |
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

A student **passes** only if every subject is 40 or above; otherwise the status
is **FAIL**.