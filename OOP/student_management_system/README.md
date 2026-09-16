# Object-Oriented Programming (OOP) Concepts

This project demonstrates core OOP concepts in Python through a **Student Management System**.

---

## Core Concepts

### 1. Class

A **class** is a blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods) that objects of that type will have.

```python
class Student:
    # Class definition
```

Here, `Student` is a class that represents the idea of a student. It doesn't hold any specific data yet — it just defines what a student *looks like*.

---

### 2. Object

An **object** is a specific instance created from a class. While the class is the blueprint, the object is the actual thing built from it.

```python
student1 = Student("Sravan", "sravan@mail.com", "STU001", "Computer Science", [85, 90, 78])
student2 = Student("Kumar", "kumar@mail.com", "STU002", "Data Science", [92, 88, 95])
```

`student1` and `student2` are two different objects of the `Student` class. Each has its own unique data (name, email, marks, etc.) but shares the same structure and methods.

---

### 3. `__init__` Method (Constructor)

The `__init__` method is a **special method** (constructor) that runs automatically when a new object is created. It initializes the object's attributes.

```python
def __init__(self, name, email, student_id, course, marks=None):
    self.name = name
    self.email = email
    self.student_id = student_id
    self.course = course
    self.marks = marks if marks is not None else []
    Student.total_students += 1
```

- **`self`** refers to the object being created.
- Each attribute (`self.name`, `self.email`, etc.) stores data specific to that object.
- The default parameter `marks=None` allows creating a student without marks (defaults to an empty list).

---

### 4. Instance Methods

**Instance methods** are functions defined inside a class that operate on a specific object. They always take `self` as their first parameter, which gives them access to the object's data.

```python
def display_details(self):
    print(f"Name: {self.name}, Email: {self.email}")

def calculate_average(self):
    return sum(self.marks) / len(self.marks)
```

These methods are called on an object:

```python
student1.display_details()
student1.calculate_average()
```

Each call operates on the data of the specific object it is called on.

---

### 5. Class Variable

A **class variable** is shared across **all instances** of a class. It belongs to the class itself, not to any single object.

```python
class Student:
    total_students = 0  # Class variable
```

Every time a new `Student` object is created, the class variable is incremented:

```python
Student.total_students += 1
```

All objects share the same value:

```python
print(Student.total_students)  # e.g., 3 (if 3 students exist)
```

---

### 6. Class Method

A **class method** is a method that operates on the **class itself** rather than on a specific object. It takes `cls` (class) instead of `self` as its first parameter and is decorated with `@classmethod`.

```python
@classmethod
def get_total_students(cls):
    return f"Total students registered: {cls.total_students}"
```

Class methods are called on the class, not on an object:

```python
print(Student.get_total_students())  # Works without creating any object
```

They are useful for accessing or modifying class-level data.

---

## Summary Table

| Concept | Description | Example in this project |
|---|---|---|
| **Class** | Blueprint for creating objects | `class Student` |
| **Object** | Instance of a class | `student1`, `student2`, `student3` |
| **`__init__`** | Constructor to initialize attributes | `def __init__(self, name, ...)` |
| **Instance Method** | Method that operates on an object | `display_details()`, `calculate_average()` |
| **Class Variable** | Shared variable across all instances | `total_students = 0` |
| **Class Method** | Method that operates on the class | `get_total_students()` |

---

## How They Work Together in This Project

The `Student` class in the notebook brings all these concepts together:

1. A **class** `Student` is defined with attributes and methods.
2. **Objects** (`student1`, `student2`, `student3`) are created from the class.
3. The **`__init__`** method sets up each student's name, email, ID, course, and marks when the object is created.
4. **Instance methods** like `display_details()`, `update_marks()`, and `calculate_average()` let you interact with each student's data.
5. A **class variable** `total_students` keeps a running count of how many students have been registered.
6. A **class method** `get_total_students()` accesses the class variable to display the total count — without needing a specific student object.
