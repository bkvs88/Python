# Employee Management System

A simple Employee Management System built with **Object-Oriented Programming (OOP)** in Python. It models individual employees as objects, each carrying their ID, name, department, salary, and designation, and provides methods to display information, update salary, and calculate annual salary.

---

## Program Overview

The program defines a single **`Employee`** class that encapsulates all employee data and behaviour:

| Property | Description |
|---|---|
| `employee_id` | Unique identifier (e.g., `EMP001`) |
| `name` | Full name of the employee |
| `department` | Department the employee works in |
| `salary` | Monthly salary in dollars |
| `designation` | Job title (e.g., Software Engineer) |

Five employee objects are created and every method is demonstrated on them.

---

## Feature / Functionalities

| Method | Type | Description |
|---|---|---|
| `__init__(employee_id, name, department, salary, designation)` | Constructor | Creates an employee and increments `total_employees` |
| `display_info()` | Instance method | Prints the complete employee record |
| `update_salary(new_salary)` | Instance method | Changes the monthly salary and confirms the change |
| `calculate_annual_salary()` | Instance method | Returns `12 × monthly salary` as a float |
| `get_total_employees()` | Class method | Returns the total number of employees created |

---

## OOP Concepts Used

### Encapsulation

All employee data lives **inside** the object. The caller works through methods (`display_info()`, `update_salary()`, `calculate_annual_salary()`) instead of reaching into raw fields:

```python
emp1.update_salary(8500.50)   # safe, validated route to change state
emp1.calculate_annual_salary()
```

### Abstraction

The user of the class sees a simple interface — create an employee, display it, raise the salary, compute the annual figure. The internal state (how the monthly-to-annual conversion happens, how the counter increments) is hidden behind those method calls.

### Class Variable & Class Method

| Concept | Name | Purpose |
|---|---|---|
| Class variable | `total_employees` | Shared counter incremented on every employee creation |
| Class method | `get_total_employees()` | Accesses the counter via `cls` and returns the total count |

```python
Employee.total_employees  # 5 after creating five employees
```

### Objects & Instances

Each `Employee` is an independent object:

```python
emp1 = Employee("EMP001", "Sravan Kumar", "Engineering", 7500.50, "Software Engineer")
emp2 = Employee("EMP002", "Divya Kumar", "Human Resources", 5200.00, "HR Executive")
```

Updating `emp1`'s salary has **no effect** on `emp2` — each object holds its own state.

---

## Code Execution

### File Structure

```
employee_management_oops/
├── employee.py   — full source code with docstrings and comments
└── README.md     — this documentation
```

### How to Run

```bash
python3 employee.py
```

---

## Output

```
=============================================
EMPLOYEE RECORDS
=============================================

--- EMP001: Sravan Kumar ---
Employee ID:    EMP001
Name:           Sravan Kumar
Department:     Engineering
Designation:    Software Engineer
Monthly Salary: $7,500.50

--- EMP002: Divya Kumar ---
Employee ID:    EMP002
Name:           Divya Kumar
Department:     Human Resources
Designation:    HR Executive
Monthly Salary: $5,200.00

--- EMP003: Deepansh ---
Employee ID:    EMP003
Name:           Deepansh
Department:     Finance
Designation:    Financial Analyst
Monthly Salary: $6,100.75

--- EMP004: Kesav Singh ---
Employee ID:    EMP004
Name:           Kesav Singh
Department:     Data Science
Designation:    Data Scientist
Monthly Salary: $8,200.00

--- EMP005: Aditi Mehta ---
Employee ID:    EMP005
Name:           Aditi Mehta
Department:     Marketing
Designation:    Marketing Manager
Monthly Salary: $4,800.25

=============================================
ANNUAL SALARY (calculate_annual_salary)
=============================================
Sravan Kumar: $90,006.00/year
Divya Kumar: $62,400.00/year
Deepansh: $73,209.00/year
Kesav Singh: $98,400.00/year
Aditi Mehta: $57,603.00/year

=============================================
SALARY UPDATES (update_salary)
=============================================
Sravan Kumar: salary updated from $7,500.50 to $8,500.50 per month.
Kesav Singh: salary updated from $8,200.00 to $9,000.00 per month.

=============================================
UPDATED ANNUAL SALARIES
=============================================
Sravan Kumar: $102,006.00/year
Kesav Singh: $108,000.00/year

=============================================
EMPLOYEE SUMMARY
=============================================
Total employees created: 5
```

---

## Key Takeaway

> **An `Employee` object bundles its data and behaviour together — the system stays simple to use, and each employee's state (like salary) changes independently without breaking the others.**

---

## Files

- `employee.py` — full source code with docstrings and comments
- `README.md` — this documentation