"""Formatting utilities for currency, tables, dates, and ID generation."""

from datetime import date, timedelta

from ..config import CURRENCY_SYMBOL


def format_currency(amount):
    """Format a number as currency string.

    Args:
        amount: Numeric amount to format.

    Returns:
        str: Formatted currency string (e.g., '₹1,250.50').
    """
    if amount is None:
        return f"{CURRENCY_SYMBOL}0.00"
    return f"{CURRENCY_SYMBOL}{amount:,.2f}"


def format_percentage(value, total):
    """Calculate and format a percentage string.

    Args:
        value: The part value.
        total: The whole value.

    Returns:
        str: Formatted percentage (e.g., '36.98%').
    """
    if not total:
        return "0.00%"
    pct = (value / total) * 100
    return f"{pct:.2f}%"


def format_date(d):
    """Format a date object as YYYY-MM-DD string.

    Args:
        d: A date object.

    Returns:
        str: Formatted date string.
    """
    if isinstance(d, str):
        return d
    return d.isoformat() if d else ""


def format_table(headers, rows, col_widths=None):
    """Render a list of rows as a formatted ASCII table.

    Args:
        headers: List of column header strings.
        rows: List of lists, each inner list is a row.
        col_widths: Optional list of minimum column widths.

    Returns:
        str: The formatted table string.
    """
    if not col_widths:
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))

    def make_row(cells):
        parts = []
        for i, cell in enumerate(cells):
            parts.append(str(cell).ljust(col_widths[i]))
        return "| " + " | ".join(parts) + " |"

    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    lines = [separator, make_row(headers), separator]
    for row in rows:
        lines.append(make_row(row))
    lines.append(separator)
    return "\n".join(lines)


def generate_expense_id(existing_ids):
    """Generate a unique expense ID in the format EXP###.

    Args:
        existing_ids: List of existing expense ID strings.

    Returns:
        str: A new unique expense ID.
    """
    max_num = 0
    for eid in existing_ids:
        if eid.startswith("EXP") and eid[3:].isdigit():
            num = int(eid[3:])
            if num > max_num:
                max_num = num
    return f"EXP{max_num + 1:03d}"


def get_today():
    """Return today's date."""
    return date.today()


def get_week_dates():
    """Return a list of dates for the last 7 days (including today).

    Returns:
        list[date]: List of 7 date objects.
    """
    today = date.today()
    return [today - timedelta(days=i) for i in range(6, -1, -1)]


def get_month_start():
    """Return the first day of the current month.

    Returns:
        date: First day of current month.
    """
    today = date.today()
    return today.replace(day=1)


def get_bar_chart(value, total, width=16):
    """Generate a simple text-based bar chart.

    Args:
        value: The current value.
        total: The total/maximum value.
        width: Number of characters for the bar width.

    Returns:
        str: A text bar chart string.
    """
    if not total:
        return "\u2591" * width
    filled = int((value / total) * width)
    filled = min(filled, width)
    return "\u2588" * filled + "\u2591" * (width - filled)
