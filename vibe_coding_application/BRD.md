# Business Requirements Document (BRD)

## Personal Expense Tracker Application

**Document Version:** 1.0  
**Date:** 09 September 2026  
**Project Name:** Personal Expense Tracker  
**Target Directory:** `works/vibe_coding_application/`  
**Technology Stack:** Python 3.13

---

## 1. Executive Summary

The Personal Expense Tracker is a menu-driven Python application that enables users to record, categorize, analyze, and manage their daily expenses. The application provides an intuitive CLI interface for adding, viewing, editing, and deleting expenses, along with reporting features to help users understand their spending patterns.

---

## 2. Problem Statement

Individuals often struggle to track their day-to-day expenses manually. Without a structured system, it becomes difficult to:
- Monitor where money is being spent
- Identify unnecessary or excessive spending
- Stay within a monthly budget
- Generate expense summaries for financial planning

This application solves these problems by providing a simple, local, menu-driven tool for personal expense management.

---

## 3. Project Objectives

| # | Objective |
|---|-----------|
| 1 | Provide a simple CLI interface for managing personal expenses |
| 2 | Allow users to categorize expenses for better analysis |
| 3 | Generate daily, weekly, and monthly expense reports |
| 4 | Enable budget tracking with alerts when limits are exceeded |
| 5 | Persist data locally using CSV/JSON file storage |
| 6 | Ensure fault tolerance with proper error handling and logging |

---

## 4. Scope

### In Scope

| Feature | Description |
|---------|-------------|
| Add Expense | Record expense with amount, category, date, and description |
| View Expenses | Display all expenses with optional filtering by date/category |
| Edit Expense | Modify an existing expense record |
| Delete Expense | Remove an expense record |
| Search Expenses | Search by category, date range, or keyword |
| Category Management | Predefined + custom expense categories |
| Budget Setting | Set monthly budget limits per category and overall |
| Reports | Generate summary reports (daily, weekly, monthly) |
| Export | Export expenses to CSV format |
| Data Persistence | Save and load expenses from local file storage |
| Authentication | Simple PIN-based access to protect data |
| Logging | Activity and error logging |

### Out of Scope

- Web-based or mobile UI
- Cloud sync or multi-device access
- Bank account integration
- Multi-user support
- Advanced data visualization / charts
- Recurring expense auto-generation

---

## 5. Functional Requirements

### 5.1 Authentication Module (`auth.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-AUTH-01 | User must set a 4-digit PIN on first run | High |
| FR-AUTH-02 | User must enter PIN to access the application | High |
| FR-AUTH-03 | Lock account after 3 consecutive failed attempts | Medium |
| FR-AUTH-04 | Allow PIN change from within the application | Low |

### 5.2 Expense Management Module (`expense.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-EXP-01 | Add a new expense with: amount, category, date, description | High |
| FR-EXP-02 | Validate amount (positive number, max 2 decimal places) | High |
| FR-EXP-03 | Default date to current date if not provided | High |
| FR-EXP-04 | Edit existing expense by ID | High |
| FR-EXP-05 | Delete expense by ID with confirmation prompt | High |
| FR-EXP-06 | Auto-generate unique ID for each expense record | High |
| FR-EXP-07 | Display expenses in a formatted table | High |
| FR-EXP-08 | Filter expenses by date range, category, or amount range | Medium |
| FR-EXP-09 | Search expenses by keyword in description | Medium |

### 5.3 Category Management Module (`category.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-CAT-01 | Provide predefined categories: Food, Transport, Entertainment, Utilities, Healthcare, Shopping, Education, Other | High |
| FR-CAT-02 | Allow user to add custom categories | Medium |
| FR-CAT-03 | Allow user to view all available categories | Medium |
| FR-CAT-04 | Prevent deletion of a category if expenses exist under it | Low |

### 5.4 Budget Module (`budget.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-BUD-01 | Set an overall monthly budget | High |
| FR-BUD-02 | Set per-category monthly budget limits | Medium |
| FR-BUD-03 | Display remaining budget after each expense addition | Medium |
| FR-BUD-04 | Show warning when spending reaches 80% of budget | Medium |
| FR-BUD-05 | Show alert when budget is exceeded | High |

### 5.5 Reports Module (`reports.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-RPT-01 | Generate daily expense summary (today's spending by category) | High |
| FR-RPT-02 | Generate weekly expense summary (last 7 days) | High |
| FR-RPT-03 | Generate monthly expense summary (current month) | High |
| FR-RPT-04 | Show total spending and category-wise breakdown | High |
| FR-RPT-05 | Show budget vs. actual comparison in reports | Medium |
| FR-RPT-06 | Show highest and lowest expense categories | Low |

### 5.6 Data Storage Module (`storage.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-STO-01 | Save all expense data to a local JSON file | High |
| FR-STO-02 | Load expense data on application startup | High |
| FR-STO-03 | Auto-save after every write operation (add/edit/delete) | High |
| FR-STO-04 | Export expenses to CSV format | Medium |
| FR-STO-05 | Handle file corruption gracefully with backup | Medium |

### 5.7 Authentication & Security Module (`auth.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-SEC-01 | Store hashed PIN (not plain text) | High |
| FR-SEC-02 | Encrypt local data file | Low |

### 5.8 Logging Module (`logger.py`)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-LOG-01 | Log all user actions (add, edit, delete, login) | High |
| FR-LOG-02 | Log all errors and exceptions | High |
| FR-LOG-03 | Separate log files for activity and errors | Medium |
| FR-LOG-04 | Log entries must include timestamp, action, and status | High |

---

## 6. Non-Functional Requirements

| ID | Requirement | Category |
|----|-------------|----------|
| NFR-01 | Application must respond within 1 second for all operations | Performance |
| NFR-02 | Data must persist across application restarts | Reliability |
| NFR-03 | Application must handle invalid inputs gracefully without crashing | Fault Tolerance |
| NFR-04 | All error messages must be user-friendly | Usability |
| NFR-05 | Application must work on Windows, macOS, and Linux | Compatibility |
| NFR-06 | No external library dependencies beyond Python standard library | Portability |
| NFR-07 | Code must follow PEP 8 style guidelines | Code Quality |
| NFR-08 | Application must include a README with usage instructions | Documentation |

---

## 7. Application Menu Structure

```
========================================
     PERSONAL EXPENSE TRACKER
========================================
  1. Login
  2. Exit
========================================

(After Login)

========================================
     MAIN MENU
========================================
  1. Add Expense
  2. View Expenses
  3. Edit Expense
  4. Delete Expense
  5. Search Expenses
  6. Manage Categories
  7. Set Budget
  8. View Reports
  9. Export to CSV
  10. Change PIN
  0. Logout
========================================
```

---

## 8. Data Model

### 8.1 Expense Record

```json
{
  "id": "EXP001",
  "amount": 45.50,
  "category": "Food",
  "date": "2026-09-09",
  "description": "Lunch at cafe",
  "created_at": "2026-09-09T14:30:00",
  "updated_at": "2026-09-09T14:30:00"
}
```

### 8.2 Budget Record

```json
{
  "month": "2026-09",
  "overall_limit": 5000.00,
  "category_limits": {
    "Food": 1500.00,
    "Transport": 800.00,
    "Entertainment": 500.00
  }
}
```

### 8.3 Categories

```json
{
  "predefined": ["Food", "Transport", "Entertainment", "Utilities", "Healthcare", "Shopping", "Education", "Other"],
  "custom": []
}
```

---

## 9. Package and Module Structure

### 9.1 Design Principles

| Principle | Rationale |
|-----------|-----------|
| **Proper Python package** with `__init__.py` | Makes the project importable and follows PEP 420; consistent with `calculator_tools` pattern |
| **Relative imports** within the package | Ensures portability; no working-directory dependency |
| **Flat module layout** (no sub-packages) | Keeps complexity appropriate for the project scope |
| **Entry point outside the package** | `main.py` at project root; package stays clean and reusable |
| **Centralized logging** with parent/child loggers | Consistent with `file_organiser` pattern; each module gets its own child logger |
| **Hierarchical exceptions** with shared base class | Consistent with `calculator_tools` and `file_organiser` patterns |
| **`pathlib` for all file paths** | Cross-platform robustness; consistent with `file_organiser` pattern |
| **Auto-created data directories** | `data/`, `logs/`, `exports/` created at runtime with `Path.mkdir(exist_ok=True)` |

### 9.2 Directory Tree

```
vibe_coding_application/
│
├── BRD.md                              # This document
├── README.md                           # Project documentation
├── main.py                             # Entry point (runs outside the package)
│
├── expense_tracker/                    # ====== PYTHON PACKAGE ======
│   ├── __init__.py                     #   Public API facade + __all__
│   │
│   ├── models/                         #   ---- Data Models ----
│   │   └── __init__.py                 #     Re-exports: Expense, Budget, Category
│   │   ├── expense.py                  #     Expense dataclass / record class
│   │   ├── budget.py                   #     Budget dataclass / record class
│   │   └── category.py                 #     Category dataclass / predefined list
│   │
│   ├── services/                       #   ---- Business Logic ----
│   │   └── __init__.py                 #     Re-exports: service functions
│   │   ├── expense_service.py          #     Add, edit, delete, search, filter expenses
│   │   ├── budget_service.py           #     Set budget, check limits, calculate remaining
│   │   ├── category_service.py         #     Add/view/delete categories
│   │   ├── report_service.py           #     Daily, weekly, monthly report generation
│   │   └── auth_service.py             #     PIN setup, verify, change, lockout logic
│   │
│   ├── storage/                        #   ---- Data Persistence ----
│   │   └── __init__.py                 #     Re-exports: StorageManager
│   │   └── storage_manager.py          #     JSON read/write, CSV export, backup/restore
│   │
│   ├── utils/                          #   ---- Utilities ----
│   │   └── __init__.py                 #     Re-exports: utility functions
│   │   ├── formatters.py               #     Currency formatting, table rendering, date utils
│   │   ├── validators.py               #     Input validation (amount, date, category)
│   │   └── logger.py                   #     Centralized logging config (parent + child loggers)
│   │
│   ├── exceptions.py                   #   ---- Custom Exception Hierarchy ----
│   │
│   └── config.py                       #   ---- App Constants ----
│                                         #     App name, version, default paths, categories
│
├── data/                               # ====== RUNTIME DATA ====== (auto-created)
│   ├── expenses.json                   #     Expense records
│   ├── categories.json                 #     Category definitions (predefined + custom)
│   ├── budget.json                     #     Budget settings
│   └── auth.json                       #     Hashed PIN + lockout state
│
├── logs/                               # ====== LOG OUTPUT ====== (auto-created)
│   ├── activity.log                    #     User actions (DEBUG+)
│   └── error.log                       #     Errors only (WARNING+)
│
├── exports/                            # ====== CSV EXPORTS ====== (auto-created)
│   └── expenses_YYYY-MM.csv            #     Monthly export files
│
└── tests/                              # ====== TEST SUITE ======
    ├── __init__.py                     #     Makes tests a package
    ├── conftest.py                     #     Shared pytest fixtures (tmp dirs, sample data)
    ├── test_expense_service.py         #     Expense CRUD tests
    ├── test_budget_service.py          #     Budget logic tests
    ├── test_category_service.py        #     Category management tests
    ├── test_report_service.py          #     Report generation tests
    ├── test_auth_service.py            #     Authentication tests
    ├── test_storage_manager.py         #     File I/O and backup tests
    ├── test_validators.py              #     Input validation edge cases
    └── test_formatters.py              #     Formatting utility tests
```

### 9.3 Package `__init__.py` — Public API

The package exposes a clean public API through `expense_tracker/__init__.py`. Internal modules are never imported directly by `main.py`.

```python
# expense_tracker/__init__.py
"""Personal Expense Tracker - A CLI tool for managing personal expenses."""

__version__ = "1.0.0"

from .models.expense import Expense
from .models.budget import Budget
from .models.category import Category, PREDEFINED_CATEGORIES
from .services.expense_service import (
    add_expense, view_expenses, edit_expense,
    delete_expense, search_expenses
)
from .services.budget_service import (
    set_budget, get_budget_status, check_budget_alert
)
from .services.category_service import (
    get_categories, add_category, delete_category
)
from .services.report_service import (
    generate_daily_report, generate_weekly_report, generate_monthly_report
)
from .services.auth_service import (
    setup_pin, verify_pin, change_pin, is_locked
)
from .storage.storage_manager import StorageManager
from .exceptions import (
    ExpenseTrackerError, InvalidAmountError, InvalidDateError,
    ExpenseNotFoundError, BudgetExceededError, AuthenticationError,
    CategoryNotFoundError, FileCorruptionError
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
```

### 9.4 Module Responsibilities

| Module | File | Responsibility |
|--------|------|----------------|
| **Models** | `models/expense.py` | `Expense` dataclass: id, amount, category, date, description, timestamps |
| | `models/budget.py` | `Budget` dataclass: month, overall_limit, category_limits dict |
| | `models/category.py` | `Category` dataclass, `PREDEFINED_CATEGORIES` constant list |
| **Services** | `services/expense_service.py` | Business logic for add/edit/delete/search/filter expenses |
| | `services/budget_service.py` | Budget CRUD, remaining calculation, threshold alerts (80%/100%) |
| | `services/category_service.py` | Category CRUD with dependency check (prevent deletion if expenses exist) |
| | `services/report_service.py` | Report generation: daily, weekly, monthly with category breakdown |
| | `services/auth_service.py` | PIN hash/verify, lockout logic (3 attempts), PIN change |
| **Storage** | `storage/storage_manager.py` | JSON read/write, CSV export, auto-backup before writes, corruption recovery |
| **Utils** | `utils/formatters.py` | Currency display, table rendering, date formatting, ID generation |
| | `utils/validators.py` | Amount validation, date parsing, category existence check |
| | `utils/logger.py` | Centralized logging setup: parent logger + child loggers per module |
| **Exceptions** | `exceptions.py` | Base `ExpenseTrackerError` + 7 domain-specific subclasses |
| **Config** | `config.py` | App name, version, default paths, category list, budget thresholds |
| **Entry** | `main.py` (root) | Menu loop, user input dispatch, calls package API |

### 9.5 Import Flow

```
main.py (entry point)
  └── import expense_tracker          # Uses public API from __init__.py
        ├── expense_tracker.models.*   # Data classes
        ├── expense_tracker.services.* # Business logic
        ├── expense_tracker.storage.*  # Persistence
        ├── expense_tracker.utils.*    # Formatting, validation, logging
        └── expense_tracker.exceptions # Error hierarchy
```

**Rule:** `main.py` only imports from `expense_tracker` (the package). It never reaches into sub-modules directly.

### 9.6 Exception Hierarchy

```
expense_tracker/exceptions.py

ExpenseTrackerError (base)
├── InvalidAmountError          # Non-positive, non-numeric, or > 2 decimal places
├── InvalidDateError            # Malformed, future, or unparseable date
├── ExpenseNotFoundError        # ID not found in records
├── DuplicateExpenseError       # Duplicate entry detection
├── BudgetExceededError         # Spending exceeds budget limit
├── AuthenticationError         # Wrong PIN / account locked
├── CategoryNotFoundError       # Category does not exist
└── FileCorruptionError         # Data file is unreadable or malformed
```

### 9.7 Logging Architecture

```
expense_tracker (parent logger)
├── expense_tracker.auth_service      # Logs: login attempts, PIN changes
├── expense_tracker.expense_service   # Logs: add, edit, delete operations
├── expense_tracker.budget_service    # Logs: budget changes, alerts
├── expense_tracker.category_service  # Logs: category add/delete
├── expense_tracker.report_service    # Logs: report generation
└── expense_tracker.storage_manager   # Logs: file read/write, backup, restore

Output:
├── logs/activity.log   (DEBUG+ level — all actions)
└── logs/error.log      (WARNING+ level — errors and warnings)
```

### 9.8 Runtime Directory Auto-Creation

All runtime directories are created automatically on first run using `pathlib`:

```python
# In expense_tracker/config.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent   # vibe_coding_application/
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
EXPORTS_DIR = BASE_DIR / "exports"

for directory in [DATA_DIR, LOGS_DIR, EXPORTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
```

---

## 10. User Interface (CLI Screenshots)

### 10.1 Add Expense Screen

```
========================================
        ADD NEW EXPENSE
========================================
Date (YYYY-MM-DD) [2026-09-09]: 
Amount: 45.50
Category:
  1. Food
  2. Transport
  3. Entertainment
  4. Utilities
  5. Healthcare
  6. Shopping
  7. Education
  8. Other
  9. Custom Category
Select category: 1
Description: Lunch at cafe

✓ Expense added successfully!
  ID: EXP001 | Amount: ₹45.50 | Category: Food
  Monthly Budget Remaining: ₹4,554.50 / ₹5,000.00
========================================
```

### 10.2 View Expenses Screen

```
========================================
        VIEW EXPENSES
========================================
Filter: [1] All  [2] By Date  [3] By Category  [4] By Range
> 1

+--------+------------+-----------+---------------+------------------+
| ID     | Date       | Amount    | Category      | Description      |
+--------+------------+-----------+---------------+------------------+
| EXP001 | 2026-09-09 | ₹45.50   | Food          | Lunch at cafe    |
| EXP002 | 2026-09-09 | ₹120.00  | Transport     | Auto fare        |
| EXP003 | 2026-09-08 | ₹500.00  | Shopping      | New shirt        |
+--------+------------+-----------+---------------+------------------+
Total: ₹665.50 | Records: 3
========================================
```

### 10.3 Monthly Report Screen

```
========================================
     MONTHLY REPORT - September 2026
========================================
Total Expenses: ₹3,245.50
Budget Limit:   ₹5,000.00
Remaining:      ₹1,754.50 (35.09%)

Category Breakdown:
  Food          ₹1,200.00  (36.98%)  ████████░░░░░░░░
  Transport       ₹800.00  (24.65%)  ██████░░░░░░░░░░
  Shopping        ₹645.50  (19.89%)  ████░░░░░░░░░░░░
  Entertainment   ₹400.00  (12.32%)  ███░░░░░░░░░░░░░
  Utilities       ₹200.00  ( 6.16%)  █░░░░░░░░░░░░░░░

Highest: Food (₹1,200.00)
Lowest:  Utilities (₹200.00)
========================================
```

---

## 11. Exception Handling Requirements

| Exception Class | Trigger | Handling |
|----------------|---------|----------|
| `InvalidAmountError` | Non-positive or invalid amount | Display error, re-prompt |
| `InvalidDateError` | Malformed or future date | Display error, use current date |
| `DuplicateExpenseError` | Duplicate entry detection | Warn user, allow override |
| `BudgetExceededError` | Spending exceeds budget limit | Display alert, confirm to proceed |
| `FileCorruptionError` | Corrupted data file | Restore from backup |
| `AuthenticationError` | Wrong PIN entered 3 times | Lock access for session |
| `CategoryNotFoundError` | Invalid category selection | Display available categories |
| `ExpenseNotFoundError` | Invalid expense ID for edit/delete | Display error message |

---

## 12. Testing Requirements

| Test Type | Coverage |
|-----------|----------|
| Unit Tests | All modules (expense, budget, reports, storage, auth) |
| Input Validation | Edge cases for amount, date, category |
| File Operations | Create, read, corrupt, and restore scenarios |
| Boundary Tests | Zero amount, max amount, empty fields |
| Integration Tests | End-to-end add-view-edit-delete flow |

**Framework:** `pytest` (consistent with existing workspace projects)

---

## 13. Acceptance Criteria

| # | Criterion |
|---|-----------|
| 1 | User can add, view, edit, and delete expenses without errors |
| 2 | All expense data persists across application restarts |
| 3 | Budget alerts trigger correctly at 80% and 100% thresholds |
| 4 | Reports accurately reflect expense data for the selected period |
| 5 | Application handles all invalid inputs gracefully with clear messages |
| 6 | Application logs all actions and errors with timestamps |
| 7 | Export to CSV produces a valid, openable CSV file |
| 8 | PIN-based authentication protects access to the application |
| 9 | All tests pass with `pytest` |
| 10 | Application runs on all major operating systems without modification |

---

## 14. Milestones

| Phase | Description | Deliverables |
|-------|-------------|--------------|
| **Phase 1** | Core Setup | Project structure, exceptions, logger, storage, utils |
| **Phase 2** | Authentication | PIN setup, login, lockout, PIN change |
| **Phase 3** | Expense CRUD | Add, view, edit, delete expenses with validation |
| **Phase 4** | Categories & Budget | Category management, budget setting and alerts |
| **Phase 5** | Reports & Export | Daily/weekly/monthly reports, CSV export |
| **Phase 6** | Testing & Polish | Unit tests, edge case handling, README |

---

## 15. Assumptions

1. The application is single-user (local machine only)
2. Data is stored locally (no cloud or network dependency)
3. Python 3.13 standard library is sufficient (no third-party dependencies)
4. User has basic familiarity with CLI/terminal interfaces
5. Date format follows ISO 8601 (YYYY-MM-DD)
6. Currency is configurable (defaults to INR ₹)

---

## 16. Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Data loss from file corruption | High | Auto-backup before every write operation |
| User forgets PIN | Medium | Provide PIN reset via backup file |
| Large dataset performance | Low | Limit display to 50 records per page |
| Cross-platform path issues | Low | Use `os.path` / `pathlib` for all file operations |

---

**End of Document**
