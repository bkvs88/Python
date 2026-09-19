import logging


def setup_logger():
    """Configure and return the logger for the student grading system.

    Writes ERROR-level messages to grading_errors.log and logs INFO-level
    and above to the console.
    """
    logger = logging.getLogger("student_grading")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("grading_errors.log")
    file_handler.setLevel(logging.ERROR)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
