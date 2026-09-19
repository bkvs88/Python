"""Personal Expense Tracker - CLI entry point."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from expense_tracker.config import APP_NAME, APP_VERSION
from expense_tracker.utils.logger import setup_logging, get_logger
from expense_tracker.exceptions import (
    ExpenseTrackerError, ExpenseNotFoundError, AuthenticationError,
    CategoryNotFoundError,
)
from expense_tracker.services.auth_service import (
    setup_pin, verify_pin, change_pin, is_locked, is_pin_set,
)
from expense_tracker.services.expense_service import (
    add_expense, view_expenses, edit_expense,
    delete_expense, search_expenses, get_expense_by_id, display_expenses,
)
from expense_tracker.services.budget_service import (
    set_budget, check_budget_alert, display_budget_status,
)
from expense_tracker.services.category_service import (
    get_all_category_names, add_category, delete_category, display_categories,
)
from expense_tracker.services.report_service import (
    generate_daily_report, generate_weekly_report, generate_monthly_report,
    format_daily_report, format_weekly_report, format_monthly_report,
)
from expense_tracker.storage import get_storage
from expense_tracker.utils.formatters import format_currency

logger = get_logger("main")


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)


def print_success(message):
    """Print a success message."""
    print(f"\n  [OK] {message}")


def print_error(message):
    """Print an error message."""
    print(f"\n  [ERROR] {message}")


def print_budget_alerts(alerts):
    """Print budget alert messages."""
    for alert in alerts:
        if alert.startswith("ALERT"):
            print(f"\n  >>> {alert} <<<")
        else:
            print(f"\n  ** {alert} **")


def handle_login():
    """Handle the login flow."""
    if not is_pin_set():
        print_header("FIRST TIME SETUP")
        print("No PIN found. Please set up a 4-digit PIN.\n")
        while True:
            pin = input("  Set your 4-digit PIN: ").strip()
            confirm = input("  Confirm your PIN: ").strip()
            if pin != confirm:
                print_error("PINs do not match. Try again.")
                continue
            try:
                setup_pin(pin)
                print_success("PIN set up successfully!")
                return True
            except AuthenticationError as e:
                print_error(str(e))
                continue

    print_header("LOGIN")
    try:
        pin = input("  Enter your 4-digit PIN: ").strip()
        verify_pin(pin)
        print_success("Login successful!")
        return True
    except AuthenticationError as e:
        print_error(str(e))
        return False


def handle_add_expense():
    """Handle adding a new expense."""
    print_header("ADD NEW EXPENSE")

    try:
        categories = get_all_category_names()
    except ExpenseTrackerError as e:
        print_error(str(e))
        return

    print("Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    date_str = input("\n  Date (YYYY-MM-DD) [Enter for today]: ").strip()
    if not date_str:
        date_str = None

    amount = input("  Amount: ").strip()

    cat_choice = input("  Select category (number or name): ").strip()
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        category = categories[int(cat_choice) - 1]
    else:
        category = cat_choice

    description = input("  Description: ").strip()

    try:
        expense = add_expense(amount, category, description, date_str)
        print_success(
            f"Expense added! ID: {expense['id']} | "
            f"Amount: {format_currency(expense['amount'])} | Category: {expense['category']}"
        )

        alerts = check_budget_alert(category)
        if alerts:
            print_budget_alerts(alerts)
    except ExpenseTrackerError as e:
        print_error(str(e))


def handle_view_expenses():
    """Handle viewing expenses."""
    print_header("VIEW EXPENSES")
    print("Filter: [1] All  [2] By Date  [3] By Category  [4] By Date Range")
    choice = input("  > ").strip()

    try:
        if choice == "2":
            date_val = input("  Enter date (YYYY-MM-DD): ").strip()
            expenses = view_expenses("date", date_val)
        elif choice == "3":
            cat = input("  Enter category: ").strip()
            expenses = view_expenses("category", cat)
        elif choice == "4":
            start = input("  Start date (YYYY-MM-DD): ").strip()
            end = input("  End date (YYYY-MM-DD): ").strip()
            expenses = view_expenses("date_range", (start, end))
        else:
            expenses = view_expenses()

        print("\n" + display_expenses(expenses))
    except ExpenseTrackerError as e:
        print_error(str(e))


def handle_edit_expense():
    """Handle editing an expense."""
    print_header("EDIT EXPENSE")
    expense_id = input("  Enter expense ID to edit: ").strip()

    try:
        expense = get_expense_by_id(expense_id)
        print(f"\n  Current: {expense['date']} | {expense['amount']} | {expense['category']} | {expense.get('description', '')}")

        print("\n  Leave blank to keep current value.")
        amount = input(f"  New amount [{expense['amount']}]: ").strip() or None
        category = input(f"  New category [{expense['category']}]: ").strip() or None
        description = input(f"  New description [{expense.get('description', '')}]: ").strip()
        description = description if description else None
        date_str = input(f"  New date [{expense['date']}]: ").strip() or None

        updated = edit_expense(expense_id, amount, category, description, date_str)
        print_success(f"Expense {expense_id} updated successfully!")

        alerts = check_budget_alert(category or updated.get("category"))
        if alerts:
            print_budget_alerts(alerts)
    except ExpenseTrackerError as e:
        print_error(str(e))


def handle_delete_expense():
    """Handle deleting an expense."""
    print_header("DELETE EXPENSE")
    expense_id = input("  Enter expense ID to delete: ").strip()

    try:
        expense = get_expense_by_id(expense_id)
        print(f"\n  Expense: {expense['date']} | {expense['amount']} | {expense['category']} | {expense.get('description', '')}")
        confirm = input("  Are you sure? (yes/no): ").strip().lower()

        if confirm == "yes":
            delete_expense(expense_id)
            print_success(f"Expense {expense_id} deleted.")
        else:
            print("  Deletion cancelled.")
    except ExpenseNotFoundError as e:
        print_error(str(e))


def handle_search_expenses():
    """Handle searching expenses."""
    print_header("SEARCH EXPENSES")
    keyword = input("  Enter search keyword: ").strip()

    try:
        results = search_expenses(keyword)
        print(f"\n  Found {len(results)} result(s):")
        print("\n" + display_expenses(results))
    except ExpenseTrackerError as e:
        print_error(str(e))


def handle_manage_categories():
    """Handle category management."""
    print_header("MANAGE CATEGORIES")
    try:
        print(display_categories())
    except ExpenseTrackerError as e:
        print_error(str(e))
        return
    print("\n  [1] Add Category  [2] Delete Category  [0] Back")
    choice = input("  > ").strip()

    if choice == "1":
        name = input("  Enter new category name: ").strip()
        try:
            add_category(name)
            print_success(f"Category '{name}' added!")
        except ValueError as e:
            print_error(str(e))
    elif choice == "2":
        name = input("  Enter category name to delete: ").strip()
        try:
            delete_category(name)
            print_success(f"Category '{name}' deleted!")
        except (CategoryNotFoundError, ValueError) as e:
            print_error(str(e))


def handle_set_budget():
    """Handle setting budget."""
    print_header("SET MONTHLY BUDGET")

    try:
        overall = input("  Overall monthly budget amount: ").strip()
        if overall:
            overall = float(overall)
        else:
            overall = 0.0

        cat_limits = {}
        while True:
            cat = input("  Add category budget? (category name or blank to skip): ").strip()
            if not cat:
                break
            limit = input(f"  Budget limit for '{cat}': ").strip()
            if limit:
                cat_limits[cat] = float(limit)

        budget = set_budget(overall, cat_limits if cat_limits else None)
        print_success(f"Budget set for {budget['month']}!")
        print("\n" + display_budget_status())
    except (ValueError, ExpenseTrackerError) as e:
        print_error(str(e))


def handle_view_reports():
    """Handle report viewing."""
    print_header("VIEW REPORTS")
    print("  [1] Daily Report")
    print("  [2] Weekly Report")
    print("  [3] Monthly Report")
    print("  [0] Back")
    choice = input("  > ").strip()

    try:
        if choice == "1":
            date_str = input("  Date (YYYY-MM-DD) [Enter for today]: ").strip() or None
            report = generate_daily_report(date_str)
            print("\n" + format_daily_report(report))
        elif choice == "2":
            report = generate_weekly_report()
            print("\n" + format_weekly_report(report))
        elif choice == "3":
            report = generate_monthly_report()
            print("\n" + format_monthly_report(report))
    except ExpenseTrackerError as e:
        print_error(str(e))


def handle_export_csv():
    """Handle CSV export."""
    print_header("EXPORT TO CSV")

    expenses = get_storage().load_expenses()

    if not expenses:
        print("  No expenses to export.")
        return

    try:
        filepath = get_storage().export_to_csv(expenses)
        print_success(f"Exported {len(expenses)} expenses to:\n  {filepath}")
    except Exception as e:
        print_error(f"Export failed: {e}")


def handle_change_pin():
    """Handle PIN change."""
    print_header("CHANGE PIN")
    old_pin = input("  Current PIN: ").strip()
    new_pin = input("  New PIN: ").strip()
    confirm = input("  Confirm new PIN: ").strip()

    if new_pin != confirm:
        print_error("PINs do not match.")
        return

    try:
        change_pin(old_pin, new_pin)
        print_success("PIN changed successfully!")
    except AuthenticationError as e:
        print_error(str(e))


MENU_HANDLERS = {
    "1": handle_add_expense,
    "2": handle_view_expenses,
    "3": handle_edit_expense,
    "4": handle_delete_expense,
    "5": handle_search_expenses,
    "6": handle_manage_categories,
    "7": handle_set_budget,
    "8": handle_view_reports,
    "9": handle_export_csv,
    "10": handle_change_pin,
}


def main_menu():
    """Display and handle the main application menu."""
    while True:
        print_header(f"MAIN MENU - {APP_NAME}")
        print("  1.  Add Expense")
        print("  2.  View Expenses")
        print("  3.  Edit Expense")
        print("  4.  Delete Expense")
        print("  5.  Search Expenses")
        print("  6.  Manage Categories")
        print("  7.  Set Budget")
        print("  8.  View Reports")
        print("  9.  Export to CSV")
        print("  10. Change PIN")
        print("  0.  Logout")
        print("=" * 50)

        try:
            choice = input("\n  Select option: ").strip()
        except EOFError:
            print("\n  Input ended. Logging out.")
            break

        if choice == "0":
            print("\n  Logged out. Goodbye!")
            logger.info("User logged out")
            break

        handler = MENU_HANDLERS.get(choice)
        if handler:
            try:
                handler()
            except EOFError:
                print("\n  Input ended. Logging out.")
                break
            except Exception as e:
                print_error(f"Unexpected error: {e}")
                logger.exception("Unexpected error in menu handler")
        else:
            print_error("Invalid option. Please try again.")


def main():
    """Application entry point."""
    setup_logging()
    logger.info("Application started - %s v%s", APP_NAME, APP_VERSION)

    print(f"\n{'=' * 50}")
    print(f"  {APP_NAME} v{APP_VERSION}")
    print(f"{'=' * 50}")

    if is_locked():
        print_error("Account is locked. Please restart the application to try again.")
        return

    if handle_login():
        logger.info("User authenticated, entering main menu")
        main_menu()
    else:
        logger.warning("Authentication failed, exiting")

    logger.info("Application ended")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Application interrupted. Goodbye!")
        logger.info("Application interrupted by user")
    except Exception as e:
        print(f"\n  Fatal error: {e}")
        logger.exception("Fatal error")
        sys.exit(1)
    finally:
        logger.info("Application shutdown complete")
