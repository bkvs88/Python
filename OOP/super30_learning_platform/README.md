# Super30 Learning Platform

The **main assignment** combining every OOP concept covered so far — built as a mini EdTech platform where students and mentors register, students submit assignments, and mentors track their assigned students.

---

## Program Overview

The platform models three classes using **inheritance**:

```
         User                    (Parent / Base class)
        /    \
     Student  Mentor             (Child / Derived classes)
```

- **`User`** — base class holding shared data (`name`, `email`, `user_id`) for everyone on the platform.
- **`Student`** — inherits from `User`, adds `course_name` and a list of `completed_assignments`.
- **`Mentor`** — inherits from `User`, adds `expertise` and `students_assigned`.

---

## Feature / Functionalities

| Method | Class | Type | Description |
|---|---|---|---|
| `__init__(name, email)` | User | Constructor | Validates email, auto-generates `user_id`, increments `total_users` |
| `display_profile()` | User | Instance method | Prints shared user details |
| `get_total_users()` | User | Class method | Returns total registered users |
| `is_valid_email(email)` | User | Static method | Checks the email is well-formed |
| `submit_assignment(name)` | Student | Instance method | Records an assignment submission (duplicates rejected) |
| `assign_course(new_course)` | Student | Instance method | Changes the student's course and resets progress |
| `get_progress()` | Student | Instance method | Returns % of assignments completed |
| `display_profile()` | Student | Instance method | Overrides parent — adds role, course, assignments, progress |
| `assign_student(student)` | Mentor | Instance method | Assigns a student under the mentor (duplicates rejected) |
| `display_profile()` | Mentor | Instance method | Overrides parent — adds role, expertise, student count |
| `get_mentor_summary()` | Mentor | Class method | Returns total students assigned across all mentors |

---

## OOP Concepts Demonstrated (Checklist)

| Requirement | Where it appears |
|---|---|
| **Class variable** | `User.total_users` (`user_id` auto-generation), `User.platform_name`, `Mentor.all_mentees` |
| **Class method** | `User.get_total_users()`, `Mentor.get_mentor_summary()` |
| **Static method** | `User.is_valid_email()` |
| **Inheritance** | `class Student(User):`, `class Mentor(User):` |
| **Multiple objects** | `mentor1`, `student1`, `student2`, `student3` |
| **Constructors** | `__init__()` in User, Student, and Mentor |
| **Instance methods** | `submit_assignment()`, `assign_student()`, `get_progress()`, etc. |
| **Method overriding** | `display_profile()` overridden in both child classes |

---

## How Key Concepts Work Here

### Inheritance & `super()`
`Student` and `Mentor` reuse the `User` constructor to get `name`, `email`, and `user_id`:

```python
super().__init__(name, email)          # shared setup from User
```

### Class Variable — `User.total_users`
Incremented in the constructor every time **any** user (student or mentor) is created. Since both child classes inherit it, the count covers the whole platform.

### Class Method — `get_total_users()`
Reads the class variable through `cls`, so it always reflects the total:

```python
User.get_total_users()      # Total users registered: 4
```

### Static Method — `is_valid_email()`
Called both internally (in the constructor, raising `ValueError` for bad emails) and externally:

```python
User.is_valid_email("valid@mail.com")     # True
User.is_valid_email("invalid-mail.com")   # False
```

### Method Overriding
`Student.display_profile()` and `Mentor.display_profile()` call `super().display_profile()` first, then print role-specific lines (course/progress for students; expertise/students for mentors).

---

## Example Scenario (Demo Output)

```
=============================================
STUDENT REGISTRATION
=============================================
Aditi Mehta: Student 'Sravan Kumar' (USR002) has been assigned to you.
Aditi Mehta: Student 'Kumaar Reddy' (USR003) has been assigned to you.
Aditi Mehta: Student 'Kesav Singh' (USR004) has been assigned to you.
Aditi Mehta: Student 'Sravan Kumar' is already assigned under you.
...
=============================================
PLATFORM SUMMARY
=============================================
Total users registered: 4
Total students assigned to mentors: 3
```

---

## How to Run

```bash
python3 super30_platform.py
```

---

## Files

- `super30_platform.py` — full source code with comments and docstrings
- `README.md` — this documentation