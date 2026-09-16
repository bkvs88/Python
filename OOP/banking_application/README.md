# Banking Application

A simplified banking application built with **Object-Oriented Programming (OOP)** in Python. It models a real-world bank account using a `BankAccount` class with deposit, withdraw, and balance-checking functionality, plus safeguards to prevent overdrawing.

---

## Program Overview

The program defines a `BankAccount` class that represents a single bank account. Each account stores:

- **Account holder name** — who owns the account
- **Account number** — a unique, auto-generated identifier
- **Balance** — the current amount of money in the account

A class variable stores the **bank name** (shared by all accounts), and a class method allows renaming the bank for every account at once.

---

## Features / Functionalities

| Method | Type | Description |
|---|---|---|
| `__init__(account_holder, initial_balance=0)` | Constructor | Creates a new account, auto-generates an account number, and increments the total account counter |
| `deposit(amount)` | Instance method | Adds money to the account balance |
| `withdraw(amount)` | Instance method | Deducts money, with validation to prevent overdrawing |
| `check_balance()` | Instance method | Returns the current balance |
| `display_account_details()` | Instance method | Prints the bank name, holder, account number, and balance |
| `change_bank_name(new_name)` | Class method | Changes the bank name for **every** account |
| `get_total_accounts()` | Class method | Returns the total number of accounts created |

---

## OOP Concepts Used

### Classes and Objects
`BankAccount` is the **class** (blueprint). Each account created from it — e.g. `acc1`, `acc2` — is an **object** (instance) with its own data.

### `__init__` (Constructor)
Runs automatically when an account is created. It sets the account holder, balance, generates a unique account number, and increments the account counter.

### Instance Methods
Methods like `deposit()`, `withdraw()`, and `check_balance()` operate on a specific account object through `self`.

### Class Variables
- `bank_name` — shared by all accounts; renaming it affects every account.
- `total_accounts` — tracks how many accounts have been created.

### Class Methods
- `change_bank_name()` uses `@classmethod` and `cls` to update the shared bank name.
- `get_total_accounts()` reads the class variable without needing a specific object.

---

## Validation (Important)

- **Deposit** amount must be **positive**.
- **Withdrawal** amount must be **positive**.
- A user **cannot withdraw more money than is available** — the request is rejected with an "insufficient funds" message, and the balance is never overdrawn.

---

## How to Run

From the project directory:

```bash
python3 bank_account.py
```

### Expected Output

```
--- Account 1 ---
Bank:           National Bank
Account holder: Sravan
Account number: ACC0001
Balance:        $1000
Deposited $500. New balance: $1500
Insufficient funds. Cannot withdraw more than available balance.
Withdrew $300. New balance: $1200
Current balance: $1200

--- Account 2 ---
Bank:           National Bank
Account holder: Kumaar
Account number: ACC0002
Balance:        $0

--- Change bank name ---
Bank:           Global Trust Bank
Account holder: Sravan
Account number: ACC0001
Balance:        $1200
Current balance: $0

Total bank accounts created: 2
```

---

## Files

- `bank_account.py` — the full source code with comments and docstrings
- `README.md` — this documentation file