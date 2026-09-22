# Payment Processing System

A payment-processing example built with **Object-Oriented Programming (OOP)** in Python. It uses an **abstract class** to define a payment contract and demonstrates **runtime polymorphism** by calling the same `pay()` method on different payment objects.

---

## Program Overview

The program defines four classes:

- **`Payment`** — an **abstract base class** that defines the blueprint for all payment methods.
- **`CreditCardPayment`** — handles payments through a credit card.
- **`UPIPayment`** — handles payments through UPI.
- **`NetBankingPayment`** — handles payments through net banking.

A helper function `process_payments()` accepts a list of `Payment` objects and calls `pay()` on each — the correct implementation runs automatically based on the object's type.

---

## Feature / Functionalities

| Method | Type | Description |
|---|---|---|
| `__init__(amount)` | Constructor | Stores the amount to be paid |
| `pay()` | Abstract method | Declares the payment contract; no implementation in the base class |
| `__init__(amount, card_number)` | Constructor | Stores card details before calling `pay()` |
| `pay()` | Override | Charges the amount to the credit card |
| `__init__(amount, upi_id)` | Constructor | Stores the UPI ID before calling `pay()` |
| `pay()` | Override | Sends a payment request to the UPI ID |
| `__init__(amount, bank_name)` | Constructor | Stores the bank name before calling `pay()` |
| `pay()` | Override | Redirects to the bank's net banking portal |

---

## OOP Concepts Used

### Abstraction

Abstraction means **hiding implementation details** and only exposing the essential **interface**.

Here, `Payment` is declared **abstract** using the `ABC` module. Its `pay()` method is decorated with `@abstractmethod`, which means:

- It has **no body** — only a contract.
- It **cannot be instantiated** (`Payment(100)` raises an error).
- Every subclass **must** override `pay()`, or it stays abstract itself.

```python
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass
```

The consumer only knows *how to use* a payment (`payment.pay()`), never *how it works* internally — that logic lives in each concrete class.

### Runtime Polymorphism

Polymorphism means **"many forms"** — the same method name behaves differently depending on the object it is called on.

Because each subclass overrides `pay()`, the correct version is chosen **at runtime** based on the object's actual type:

```python
def process_payments(payment_list):
    for payment_method in payment_list:
        payment_method.pay()   # same call, different behaviour per object
```

`payment_method` is typed as a generic `Payment`, but:

- `CreditCardPayment` → charges the card
- `UPIPayment` → sends a UPI request
- `NetBankingPayment` → redirects to the bank portal

This is **runtime (dynamic) polymorphism** — also known as *method overriding*, because the decision of which `pay()` to run happens at runtime, not at compile time.

### Class Diagram

```
            Payment  (ABC - abstract)
          pay()  [no body]
        /     |        \
CreditCardPayment  UPIPayment  NetBankingPayment
   pay()            pay()          pay()
```

All three concrete classes inherit `amount` from `Payment` and provide their own `pay()` implementation.

---

## How to Run

```bash
python3 payment.py
```

### Expected Output

```
Processing payments...
Charging $250.75 to credit card ending in 3456.
Sending payment request of $120.00 to sravan@hdfcbank.
Redirecting to ICICI net banking portal for $89.50.
```

---

## Key Takeaway

> **Abstraction defines *what* a payment does; polymorphism decides *how* it does it. The caller only needs one interface — `pay()` — and the object figures out the rest at runtime.**

---

## Files

- `payment.py` — full source code with docstrings and comments
- `README.md` — this documentation