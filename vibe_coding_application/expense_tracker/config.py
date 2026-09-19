"""Application constants, paths, and default configuration."""

from pathlib import Path

APP_NAME = "Personal Expense Tracker"
APP_VERSION = "1.0.0"
CURRENCY_SYMBOL = "\u20b9"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
EXPORTS_DIR = BASE_DIR / "exports"

EXPENSES_FILE = DATA_DIR / "expenses.json"
CATEGORIES_FILE = DATA_DIR / "categories.json"
BUDGET_FILE = DATA_DIR / "budget.json"
AUTH_FILE = DATA_DIR / "auth.json"
ACTIVITY_LOG = LOGS_DIR / "activity.log"
ERROR_LOG = LOGS_DIR / "error.log"

MAX_LOGIN_ATTEMPTS = 3
PIN_LENGTH = 4
BUDGET_WARNING_THRESHOLD = 0.80
RECORDS_PER_PAGE = 50

PREDEFINED_CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Utilities",
    "Healthcare",
    "Shopping",
    "Education",
    "Other",
]

for directory in [DATA_DIR, LOGS_DIR, EXPORTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
