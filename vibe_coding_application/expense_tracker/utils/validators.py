"""Input validation utilities for amounts, dates, and categories."""

import re
from datetime import date, datetime

from ..exceptions import InvalidAmountError, InvalidDateError, CategoryNotFoundError
from ..config import PREDEFINED_CATEGORIES


def validate_amount(value):
    """Validate that a value is a positive number with at most 2 decimal places.

    Args:
        value: The value to validate (str, int, or float).

    Returns:
        float: The validated amount.

    Raises:
        InvalidAmountError: If the value is not a valid positive amount.
    """
    try:
        amount = float(value)
    except (TypeError, ValueError):
        raise InvalidAmountError(value)

    if amount <= 0:
        raise InvalidAmountError(value)

    if abs(amount - round(amount, 2)) > 1e-9:
        raise InvalidAmountError(value)

    return round(amount, 2)


def validate_date(date_str=None):
    """Validate and parse a date string in YYYY-MM-DD format.

    Args:
        date_str: Date string to validate. If None or empty, returns today's date.

    Returns:
        date: The parsed date object.

    Raises:
        InvalidDateError: If the date string is malformed or in the future.
    """
    if not date_str or not date_str.strip():
        return date.today()

    date_str = date_str.strip()

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise InvalidDateError(date_str)

    try:
        parsed = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise InvalidDateError(date_str)

    if parsed > date.today():
        raise InvalidDateError(date_str)

    return parsed


def validate_category(category, custom_categories=None):
    """Validate that a category exists in predefined or custom categories.

    Args:
        category: Category name to validate.
        custom_categories: List of user-defined custom categories.

    Returns:
        str: The validated category name.

    Raises:
        CategoryNotFoundError: If the category is not found.
    """
    all_categories = list(PREDEFINED_CATEGORIES)
    if custom_categories:
        all_categories.extend(custom_categories)

    if category not in all_categories:
        raise CategoryNotFoundError(category)

    return category
