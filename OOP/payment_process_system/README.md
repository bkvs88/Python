
```markdown
# 💳 Payment Processing System

A payment-processing example built with **Object-Oriented Programming (OOP)** in Python. It uses an **abstract class** to define a payment contract and demonstrates **runtime polymorphism** by executing the same `.pay()` method across different payment objects.

---

## 📑 Table of Contents
- [Program Overview](#program-overview)
- [Understanding `from abc import ABC, abstractmethod`](#understanding-from-abc-import-abc-abstractmethod)
- [1. Abstraction in Python](#1-abstraction-in-python)
- [2. Polymorphism in Python](#2-polymorphism-in-python)
- [How Abstraction and Polymorphism Work Together](#how-abstraction-and-polymorphism-work-together)
- [Class Architecture](#class-architecture)
- [How to Run](#how-to-run)
- [Key Takeaways](#key-takeaways)

---

## Program Overview

The program defines four main classes:
- **`Payment`**: An *abstract base class* that defines the blueprint/contract for all payment methods.
- **`CreditCardPayment`**: Handles payments processed through a credit card.
- **`UPIPayment`**: Handles payments processed through a UPI ID.
- **`NetBankingPayment`**: Handles payments processed through net banking portals.

A helper function, `process_payments()`, accepts a list of `Payment` objects and calls `.pay()` on each — the correct implementation runs automatically based on the object's type at runtime.

---

## Understanding `from abc import ABC, abstractmethod`

Python does not natively enforce abstract classes or interfaces through standard syntax like some other languages (e.g., Java or C++). Instead, it uses the built-in standard library module called **`abc`** (**A**bstract **B**ase **C**lasses).

### 1. What is `ABC`?
`ABC` is a helper class provided by the `abc` module. By inheriting from `ABC`, a Python class becomes an **Abstract Base Class**.

* **Enforces standard contracts:** It serves as a parent blueprint for concrete subclasses.
* **Prevents instantiation:** You cannot instantiate an abstract class directly. Calling `Payment(100)` will raise a `TypeError`.

### 2. What is `@abstractmethod`?
`@abstractmethod` is a decorator used inside an abstract class to define methods that **must** be implemented by any child class.

* **No body required:** The method usually contains only `pass` or a docstring in the base class.
* **Mandatory overriding:** If a child class fails to override any `@abstractmethod`, Python prevents that subclass from being instantiated as well.

### Code Example

```python
from abc import ABC, abstractmethod

# 1. Base Abstract Class
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        """Abstract method - must be implemented by subclasses"""
        pass

# 2. Subclass overriding the abstract method
class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print(f"Paid ${self.amount} using Credit Card ending in {self.card_number[-4:]}")

# Example Usage
# p = Payment(100)           # ❌ Raises TypeError: Can't instantiate abstract class Payment
cc = CreditCardPayment(100, "1234567890123456") 
cc.pay()                     # ✅ Output: Paid $100 using Credit Card ending in 3456

```

---

## 1. Abstraction in Python

**Abstraction** is the process of hiding implementation details from the user and exposing only the essential features or interfaces. It focuses on **what** an object does rather than **how** it does it.

In Python, abstraction is primarily enforced using the standard library module `abc` (**A**bstract **B**ase **C**lasses).

### Key Concepts:

* **Abstract Base Class (`ABC`)**: A parent class that serves as a structural blueprint for subclasses. It cannot be instantiated directly.
* **Abstract Method (`@abstractmethod`)**: A method declared in an abstract class that has no implementation (body). Every non-abstract child class **must** override this method.

### Example:

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Calculates area - must be implemented by concrete subclasses."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

# Usage:
# shape = Shape()      # ❌ TypeError: Can't instantiate abstract class Shape
circle = Circle(5)
print(circle.area())   # ✅ Output: 78.53975

```

---

## 2. Polymorphism in Python

**Polymorphism** comes from Greek, meaning "many forms." In programming, it allows objects of different classes to be treated as instances of a common parent class, where the same method call produces different behaviors based on the object executing it.

### Types of Polymorphism in Python:

#### A. Method Overriding (Runtime Polymorphism)

Subclasses provide a specific implementation of a method that is already defined in their parent class. The decision of which method to run is made dynamically at runtime.

```python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

# Function demonstrating polymorphism
def play_sound(animal):
    print(animal.make_sound())

play_sound(Dog())  # Output: Woof!
play_sound(Cat())  # Output: Meow!

```

#### B. Duck Typing

Python relies heavily on "Duck Typing"—a dynamic typing concept: *"If it walks like a duck and quacks like a duck, it's a duck."*

Python does not require explicit interface contracts or inheritance for polymorphism to work. As long as an object has the expected method name, Python will call it.

```python
class DatabaseLogger:
    def log(self, message):
        print(f"Logging to DB: {message}")

class FileLogger:
    def log(self, message):
        print(f"Logging to File: {message}")

def record_event(logger, event_name):
    logger.log(event_name)  # Doesn't matter which class, as long as log() exists

record_event(DatabaseLogger(), "User Signup")
record_event(FileLogger(), "User Signup")

```

---

## How Abstraction and Polymorphism Work Together

* **Abstraction defines the contract:** It enforces *what* methods subclasses must have (e.g., specifying that all payment methods must have a `.pay()` method).
* **Polymorphism executes the behavior:** It allows a unified process to run those methods without needing to check individual types at runtime.

```python
from abc import ABC, abstractmethod

# 1. Abstraction: Define the contract
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        return f"Charged ${amount} to Credit Card."

class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        return f"Sent ${amount} via PayPal."

# 2. Polymorphism: Treat all payments uniformly
def checkout(processor: PaymentProcessor, amount: float):
    print(processor.process_payment(amount))

checkout(CreditCard(), 100.0)  # Output: Charged $100.0 to Credit Card.
checkout(PayPal(), 50.0)       # Output: Sent $50.0 via PayPal.

```

---

## Class Architecture

```text
               +-----------------------+
               |     Payment (ABC)     |  <-- Abstract Base Class
               +-----------------------+
               | - amount: float       |
               | + pay() [abstract]    |
               +-----------------------+
                           |
       +-------------------+-------------------+
       |                   |                   |
+---------------+   +---------------+   +-------------------+
|CreditCard     |   | UPIPayment    |   | NetBankingPayment |
+---------------+   +---------------+   +-------------------+
| - card_number |   | - upi_id      |   | - bank_name       |
| + pay()       |   | + pay()       |   | + pay()           |
+---------------+   +---------------+   +-------------------+

```

---

## How to Run

1. Run the script directly using Python 3:
```bash
python3 payment.py

```


2. Expected Output:
```text
Processing payments...
Charging $250.75 to credit card ending in 3456.
Sending payment request of $120.00 to sravan@hdfcbank.
Redirecting to ICICI net banking portal for $89.50.

```



---

## Key Takeaways

* **Abstraction** defines *what* a payment does; **polymorphism** decides *how* it does it.
* The caller only needs one consistent interface — `pay()` — while each individual object figures out the underlying details at runtime.

```


## Files

- `payment.py` — full source code with docstrings and comments
- `README.md` — this documentation
