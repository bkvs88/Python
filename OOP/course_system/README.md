# Online Learning Platform

A simple EdTech platform built with **Object-Oriented Programming (OOP)** in Python. It uses inheritance to model regular and premium courses, with a class variable to track the total number of courses created.

---

## Program Overview

The program defines two classes:

- **`Course`** — the base (parent) class holding common course data and methods.
- **`PremiumCourse`** — a child class that inherits everything from `Course` and adds premium-specific features.

A **class variable** (`total_courses`) is shared across all courses and increments automatically each time a new course is created.

---

## Feature / Functionalities

| Method | Type | Description |
|---|---|---|
| `__init__(name, instructor, duration, price)` | Constructor | Creates a course and increments `total_courses` |
| `show_course_details()` | Instance method | Prints course name, instructor, duration, and price |
| `calculate_discount(discount_percent)` | Instance method | Returns the discounted price as a formatted string |
| `get_course_count()` | Class method | Returns the total number of courses created |

### PremiumCourse (adds to the above)

| Attribute | Description |
|---|---|
| `mentor_support` | `True` if 1-on-1 mentor support is included |
| `live_sessions` | `True` if live sessions are included |
| `show_course_details()` | **Overrides** the parent method to include premium attributes |

---

## OOP Concepts Used

### Inheritance

```
        Course                (Parent / Base class)
          |
    PremiumCourse             (Child / Derived class)
```

`PremiumCourse` inherits `name`, `instructor`, `duration`, `price`, `show_course_details()`, and `calculate_discount()` from `Course` — then adds `mentor_support` and `live_sessions`.

### `super()` — Calling the Parent Constructor

`PremiumCourse.__init__()` uses `super().__init__(...)` to reuse the parent constructor instead of repeating the shared logic:

```python
super().__init__(name, instructor, duration, price)
self.mentor_support = mentor_support
self.live_sessions = live_sessions
```

### Method Overriding

`PremiumCourse` **overrides** `show_course_details()` to add premium features while still calling the parent version first via `super().show_course_details()`.

### Inherited Method — `calculate_discount()`

`calculate_discount()` is defined only in `Course` — yet `PremiumCourse` objects can call it directly, thanks to inheritance:

```python
premium_ds.calculate_discount(30)
# 30% off -> $1049.30
```

### Class Variable & Class Method

| Concept | Name | Purpose |
|---|---|---|
| Class variable | `total_courses` | Shared counter incremented on every course creation |
| Class method | `get_course_count()` | Accesses the class variable via `cls` and returns the total count |

---

## How to Run

```bash
python3 course.py
```

### Expected Output

```
=============================================
COURSE CATALOG
=============================================

--- Course ---
Course:         Core Python Basics
Instructor:     Sravan Kumar
Duration:       12 hours
Price:          $499

--- Course ---
Course:         Full Stack Web Dev
Instructor:     Aditi Mehta
Duration:       40 hours
Price:          $999

--- PremiumCourse ---
Course:         Data Science Pro
Instructor:     Kesav Singh
Duration:       60 hours
Price:          $1499
Mentor Support: Yes
Live Sessions:  Yes

...
=============================================
DISCOUNT OFFERS
=============================================
Core Python: 20% off -> $399.20
Data Science Pro: 30% off -> $1049.30
Advanced Python: 10% off -> $719.10

=============================================
COURSE COUNT (Class Method)
=============================================
Total courses created: 5
```

---

## Key Takeaway

> **Inheritance lets you build specialized classes on top of generic ones — `PremiumCourse` doesn't rewrite `Course`, it extends it, keeping code DRY and modeling a natural IS-A relationship.**

---

## Files

- `course.py` — full source code with comments and docstrings
- `README.md` — this documentation