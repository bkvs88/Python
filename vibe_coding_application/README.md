# Personal Expense Tracker

A menu-driven Python CLI application for recording, categorizing, analyzing, and managing personal expenses.

## Features

- **Expense Management** - Add, view, edit, delete, and search expenses
- **Category System** - 8 predefined categories + custom category support
- **Budget Tracking** - Set monthly budgets with 80% warning and 100% alert thresholds
- **Reports** - Daily, weekly, and monthly expense summaries with visual breakdowns
- **CSV Export** - Export all expenses to CSV format
- **PIN Authentication** - 4-digit PIN protection with account lockout after 3 failed attempts
- **Data Persistence** - JSON-based local storage with automatic backups
- **Logging** - Activity and error logs with rotation

## Quick Start

### Prerequisites

- Python 3.13 or higher
- No external dependencies required

### Run the Application

```bash
cd vibe_coding_application
python main.py
```

### First Run

On first launch, you will be prompted to set up a 4-digit PIN. After setup, use your PIN to log in each time.

## Project Structure

```
vibe_coding_application/
├── main.py                     # CLI entry point
├── expense_tracker/            # Python package
│   ├── __init__.py             # Public API
│   ├── config.py               # Constants and paths
│   ├── exceptions.py           # Custom exception hierarchy
│   ├── models/                 # Data models (Expense, Budget, Category)
│   ├── services/               # Business logic
│   │   ├── auth_service.py     # PIN setup, verify, lockout
│   │   ├── expense_service.py  # Expense CRUD
│   │   ├── budget_service.py   # Budget management
│   │   ├── category_service.py # Category management
│   │   └── report_service.py   # Report generation
│   ├── storage/                # File I/O
│   │   └── storage_manager.py  # JSON read/write, CSV export
│   └── utils/                  # Utilities
│       ├── formatters.py       # Currency, table, date formatting
│       ├── validators.py       # Input validation
│       └── logger.py           # Centralized logging
├── data/                       # Runtime data (auto-created)
├── logs/                       # Log files (auto-created)
├── exports/                    # CSV exports (auto-created)
└── tests/                      # Test suite
```

## Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add a new expense |
| 2 | View expenses (all, by date, by category, by range) |
| 3 | Edit an existing expense |
| 4 | Delete an expense |
| 5 | Search expenses by keyword |
| 6 | Manage categories (add/view/delete) |
| 7 | Set monthly budget limits |
| 8 | View reports (daily/weekly/monthly) |
| 9 | Export expenses to CSV |
| 10 | Change PIN |
| 0 | Logout |

## Running Tests

```bash
cd vibe_coding_application
python -m pytest tests/ -v
```

## Data Files

All data is stored locally in the `data/` directory:

| File | Description |
|------|-------------|
| `expenses.json` | All expense records |
| `categories.json` | Predefined and custom categories |
| `budget.json` | Monthly budget configuration |
| `auth.json` | Hashed PIN and lockout state |

## Design Principles

- **Pure Python** - No external dependencies; uses only the standard library
- **Modular architecture** - Clean separation: models, services, storage, utils
- **Fault tolerant** - Custom exceptions, auto-backup before writes, corruption recovery
- **Cross-platform** - Uses `pathlib` for all file operations
- **Testable** - Isolated test suite with `pytest` fixtures and temporary directories

## Development Prompts

The following prompts were used iteratively to create and test this application:

| # | Prompt |
|---|--------|
| 1 | As a developer, understand the requirement and generate the BRD to create the application for Personal Expense Tracker |
| 2 | Suggest the package and module structure and update the same in BRD |
| 3 | Create the application |
| 4 | Create README.md file |
| 5 | Run the application code |
| 6 | Find an error |
| 7 | Check for exception handlings and add if any missing |
| 8 | Perform the final checks of the application to deploy for production |
