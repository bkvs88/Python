class InvalidMarksError(Exception):
    """Raised when marks are non-numeric or outside the valid 0-100 range."""

    def __init__(self, message="Marks must be a number between 0 and 100"):
        self.message = message
        super().__init__(self.message)


class MissingStudentInfoError(Exception):
    """Raised when student name, roll number, or marks are missing or malformed."""

    def __init__(self, message="Student name and roll number are required"):
        self.message = message
        super().__init__(self.message)
