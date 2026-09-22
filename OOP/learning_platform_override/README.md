# Learning Platform — Override

A small learning platform built with **Object-Oriented Programming (OOP)** in Python. It models different platform roles using **inheritance** — a parent `User` class holds common properties, and `Student`, `Mentor`, and `Admin` children add role-specific behaviour. It focuses on **method overriding**: the same method name produces different output depending on the object that calls it.

---

## Program Overview

The program defines four classes:

- **`User`** — the parent (base) class holding data and behaviour common to every role.
- **`Student`** — a child that can submit assignments.
- **`Mentor`** — a child that can assign mentees.
- **`Admin`** — a child that can manage users and the platform.

The parent stores shared properties (`name`, `email`, `user_id`) and provides two methods (`display_profile()` and `access_dashboard()`) that **all three children override** in their own way.

---

## Feature / Functionalities

| Method | Class | Type | Description |
|---|---|---|---|
| `__init__(name, email)` | `User` | Constructor | Validates email and assigns `name`, `email`, `user_id` |
| `display_profile()` | `User` | Instance method | Prints the generic base profile |
| `access_dashboard()` | `User` | Instance method | Returns a generic dashboard message |
| `get_total_users()` | `User` | Class method | Returns the total registered user count |
| `is_valid_email(email)` | `User` | Static method | Checks whether an email is well-formed |
| `__init__(..., course_name)` | `Student` | Constructor | Adds `course_name` on top of `User` |
| `submit_assignment(name)` | `Student` | Instance method | Records a submitted assignment (rejects duplicates) |
| `display_profile()` | `Student` | **Override** | Adds role, course, and assignment count to the profile |
| `access_dashboard()` | `Student` | **Override** | Loads the student dashboard with the enrolled course |
| `__init__(..., expertise)` | `Mentor` | Constructor | Adds `expertise` and a mentee list |
| `assign_student(student)` | `Mentor` | Instance method | Adds a student to the mentor's mentees |
| `display_profile()` | `Mentor` | **Override** | Adds role, expertise, and mentee count |
| `access_dashboard()` | `Mentor` | **Override** | Loads the mentor review dashboard |
| `__init__(..., department, is_super)` | `Admin` | Constructor | Adds `department` and `is_super` flag |
| `suspend_user(user)` | `Admin` | Instance method | Suspends a user account |
| `display_profile()` | `Admin` | **Override** | Adds role, department, and super-admin status |
| `access_dashboard()` | `Admin` | **Override** | Loads the admin analytics dashboard |

---

## Class Relationships

### Inheritance Hierarchy

```
               User                 (Parent / Base class)
       /               |              \
 Student            Mentor           Admin
(Child / Derived)  (Child)          (Child)
```

**Inheritance** creates an IS-A relationship. A `Student` **is a** `User`, a `Mentor` **is a** `User`, and an `Admin` **is a** `User`. Each child:

- Automatically receives everything the parent defines (`name`, `email`, `user_id`, `get_total_users()`).
- Extends it with role-specific properties (`course_name`, `expertise`, `department`).
- Customizes parent methods where its own behaviour differs.

### The Parent Holds the Common Core

```python
class User:
    platform_name = "Euron Super30"
    total_users = 0

    def __init__(self, name, email):
        if not User.is_valid_email(email):
            raise ValueError(f"Invalid email address: {email}")
        self.name = name
        self.email = email
        User.total_users += 1
        self.user_id = f"USR{User.total_users:03d}"
```

The shared `user_id` counter, email validation, and profile structure live in one place, so no child can drift out of sync — this keeps the code **DRY**.

### `super()` — Reusing the Parent Constructor

Every child calls the parent constructor instead of rewriting it:

```python
class Student(User):
    def __init__(self, name, email, course_name):
        super().__init__(name, email)   # parent handles shared fields
        self.course_name = course_name
        self.completed_assignments = []
```

---

## Method Overriding

**Method overriding** is when a child redefines a method inherited from its parent with the same name and parameters, giving it a different implementation. The version that runs depends on the **actual object type at runtime**.

Both `display_profile()` and `access_dashboard()` are overridden by all three children.

### Example — `display_profile()`

```python
# Student version
def display_profile(self):
    super().display_profile()          # print the shared fields first
    print(f"Role:           Student")
    print(f"Course:         {self.course_name}")

# Mentor version
def display_profile(self):
    super().display_profile()          # print the shared fields first
    print(f"Role:           Mentor")
    print(f"Expertise:      {self.expertise}")
```

Every version reuses `super().display_profile()` for the common lines, then appends its role-specific lines.

### Same Call, Different Result

```python
for user in [student1, mentor1, admin1]:
    user.display_profile()
```

The exact same line executes three times but prints three different profiles — this is **runtime polymorphism**:

```
--- Student ---
Platform:       Euron Super30
User ID:        USR001
Name:           Sravan Kumar
Role:           Student
Course:         Data Science

--- Mentor ---
Platform:       Euron Super30
User ID:        USR003
Name:           Deepansh
Role:           Mentor
Expertise:      Data Science & Python

--- Admin ---
Platform:       Euron Super30
User ID:        USR004
Name:           Kesav Singh
Role:           Admin
Department:     Operations
Super Admin:    Yes
```

---

## How to Run

```bash
python3 learning_platform.py
```

### Expected Output

```
=============================================
ROLE-SPECIFIC ACTIONS
=============================================
Sravan Kumar: 'Assignment 1 - Python Basics' submitted successfully.
Deepansh: Sravan Kumar is now your mentee.
Deepansh: Divya Kumar is now your mentee.
Kesav Singh: Account of Divya Kumar (USR002) suspended.

=============================================
METHOD OVERRIDING — display_profile()
=============================================

--- Student ---
Platform:       Euron Super30
User ID:        USR001
Name:           Sravan Kumar
Email:          sravan@super30.com
Role:           Student
Course:         Data Science
Assignments:    1

--- Mentor ---
...
=============================================
PLATFORM SUMMARY
=============================================
Total users registered: 4
```

---

## Key Takeaway

> **Inheritance gives every role the shared core; method overriding lets each role present and behave differently using the same method names — the system stays consistent for the caller while each object decides its own details at runtime.**

---

## Files

- `learning_platform.py` — full source code with docstrings and comments
- `README.md` — this documentation