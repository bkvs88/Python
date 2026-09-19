"""Personal Expense Tracker - A CLI tool for managing personal expenses."""

__version__ = "1.0.0"

from .models.expense import Expense
from .models.budget import Budget
from .models.category import Category, PREDEFINED_CATEGORIES
from .services.expense_service import (
    add_expense, view_expenses, edit_expense,
    delete_expense, search_expenses,
)
from .services.budget_service import (
    set_budget, get_budget_status, check_budget_alert,
)
from .services.category_service import (
    get_categories, add_category, delete_category,
)
from .services.report_service import (
    generate_daily_report, generate_weekly_report, generate_monthly_report,
)
from .services.auth_service import (
    setup_pin, verify_pin, change_pin, is_locked,
)
from .storage.storage_manager import StorageManager
from .exceptions import (
    ExpenseTrackerError, InvalidAmountError, InvalidDateError,
    ExpenseNotFoundError, BudgetExceededError, AuthenticationError,
    CategoryNotFoundError, FileCorruptionError,
)

__all__ = [
    "Expense", "Budget", "Category", "PREDEFINED_CATEGORIES",
    "add_expense", "view_expenses", "edit_expense", "delete_expense", "search_expenses",
    "set_budget", "get_budget_status", "check_budget_alert",
    "get_categories", "add_category", "delete_category",
    "generate_daily_report", "generate_weekly_report", "generate_monthly_report",
    "setup_pin", "verify_pin", "change_pin", "is_locked",
    "StorageManager",
    "ExpenseTrackerError", "InvalidAmountError", "InvalidDateError",
    "ExpenseNotFoundError", "BudgetExceededError", "AuthenticationError",
    "CategoryNotFoundError", "FileCorruptionError",
]
