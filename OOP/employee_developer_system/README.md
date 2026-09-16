# Inheritance in Python — Explained with Employee & Developer

This project demonstrates **inheritance** — one of the four pillars of OOP — using a realistic **Employee → Developer** example.

---

## What is Inheritance?

**Inheritance** is an OOP concept where a **child class (subclass)** acquires the attributes and methods of a **parent class (superclass)**.

Think of it like a family tree:
- The **parent class** holds the generic characteristics (what *every* member has).
- The **child class** inherits everything from the parent and then adds its own extra characteristics.

This lets you **reuse** existing code instead of rewriting it, and it creates a natural **"is-a" relationship** between classes.

---

## The "is-a" Relationship

```
    Employee            (Parent / Base / Superclass)
        |
    Developer           (Child / Derived / Subclass)
```

- A **Developer IS-A** Employee. It has everything an Employee has: `employee_id`, `name`, `salary`, `department`, and `display_details()`.
- But a Developer also has **extra** things an Employee doesn't: `language` and `experience`.

---

## Core Components of Inheritance

| Component | Description | Example from this code |
|---|---|---|
| **Parent / Base Class** | The class that provides attributes & methods to be reused | `class Employee:` (`developer.py:9`) |
| **Child / Derived Class** | The class that inherits from the parent | `class Developer(Employee):` (`developer.py:47`) |
| **`super()`** | Calls the parent class constructor/methods from the child | `super().__init__(...)` (`developer.py:72`) |
| **Attributes** | Data passed down or added | `employee_id`, `name`, ..., plus `language`, `experience` |
| **Methods** | Behaviors inherited or created | `display_details()` and `get_annual_salary()` |
| **Method Overriding** | Child redefines a parent method to customize it | `Developer.display_details()` (`developer.py:78`) |
| **Object Creation** | Instances created from the classes | `emp1`, `dev1`, etc. |

---

## How It Works in This Code

### 1. Parent Class — `Employee`

Contains the generic employee data and methods:

```python
class Employee:
    def __init__(self, employee_id, name, salary, department):
        ...
    def display_details(self):
        ...
    def get_annual_salary(self):
        ...
```

### 2. Child Class — `Developer(Employee)`

Declares `(Employee)` after its name to **inherit** from it:

```python
class Developer(Employee):
    def __init__(self, employee_id, name, salary, department, language, experience):
        super().__init__(employee_id, name, salary, department)   # reuse parent's init
        self.language = language                                   # new attribute
        self.experience = experience                               # new attribute
```

- `super().__init__(...)` **calls the parent's constructor** so the developer gets all four Employee attributes without rewriting them.
- Then the child adds its **own** attributes: `language` and `experience`.

### 3. Method Overriding

`Developer.display_details()` **overrides** the parent's method — it starts by calling the parent version via `super().display_details()`, then adds developer-specific lines:

```python
super().display_details()          # prints inherited fields
print(f"Language:   {self.language}")
print(f"Experience: {self.experience} years")
```

### 4. Objects Created

```python
emp1 = Employee("EMP001", "Aditi Mehta", 60000, "Human Resources")   # parent object
dev1 = Developer("EMP003", "Sravan Kumar", 90000, "Engineering", "Python", 5)  # child object
```

---

## Proof That the Child Accesses Parent Functionality

`get_annual_salary()` is **only defined in the parent** class — yet it can be called on a `Developer` object:

```python
dev1.get_annual_salary()
# Sravan Kumar's annual salary: $90,000
```

This works because `Developer` **inherits** every method from `Employee`. The child did not re‑write it; it simply reuses it.

---

## Concept → Code Mapping

| Inheritance Concept | Where it appears |
|---|---|
| Parent class | `class Employee:` |
| Child class | `class Developer(Employee):` |
| Inheriting parent constructor | `super().__init__(employee_id, name, salary, department)` |
| Inheriting a parent method | `dev1.get_annual_salary()` |
| Overriding a parent method | `def display_details(self):` inside `Developer` |
| New child attributes | `self.language`, `self.experience` |
| Object creation | `emp1`, `emp2`, `dev1`, `dev2`, `dev3` |

---

## How to Run

```bash
python3 developer.py
```

---

## Key Takeaway

> **Inheritance allows a child class to reuse the parent's data and behavior, while adding its own specialization — "Don't repeat yourself, extend instead."**

---

## Files

- `developer.py` — full source with comments and docstrings
- `README.md` — this documentation