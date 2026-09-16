# Mini Vehicle Rental Application

A vehicle rental system built with **Object-Oriented Programming (OOP)** in Python. It uses inheritance to model vehicles, with a `Vehicle` parent class extended by `Car` and `Bike` child classes, plus a static method to validate rental durations.

---

## Program Overview

The program defines three classes in an inheritance hierarchy:

```
         Vehicle                (Parent / Base class)
        /        \
      Car          Bike         (Child / Derived classes)
```

- **`Vehicle`** — holds shared data and methods for all rental vehicles.
- **`Car`** — inherits from `Vehicle` and adds **number of seats**.
- **`Bike`** — inherits from `Vehicle` and adds **engine capacity**.

Every vehicle can calculate its rental cost, and the system validates rental durations before accepting them.

---

## Feature / Functionalities

| Method | Type | Class | Description |
|---|---|---|---|
| `__init__(...)` | Constructor | Vehicle | Sets vehicle number, brand, model, and rental price/day |
| `show_vehicle_details()` | Instance method | Vehicle | Prints shared vehicle details |
| `calculate_rent(days)` | Instance method | Vehicle | Returns `price_per_day * days` (0.0 for invalid durations) |
| `is_valid_rental_days(days)` | Static method | Vehicle | Returns `True` only if `days > 0` |

### Car — additional attribute
- **`seats`** — number of seats in the car.

### Bike — additional attribute
- **`engine_capacity`** — engine capacity in cc.

Both `Car` and `Bike` **override** `show_vehicle_details()` to include their specific attribute while reusing the parent version via `super()`.

---

## OOP Concepts Used

### Inheritance
`Car(Vehicle)` and `Bike(Vehicle)` inherit `vehicle_number`, `brand`, `model`, `rental_price_per_day`, `calculate_rent()`, and `is_valid_rental_days()` — without rewriting any of it.

### `super()` — Reusing Parent Code
```python
super().__init__(vehicle_number, brand, model, rental_price_per_day)  # Car/Bike constructors
super().show_vehicle_details()                                        # Overridden details methods
```

### Method Overriding
`Car.show_vehicle_details()` and `Bike.show_vehicle_details()` call the parent version first, then print their own extra line (seats / engine capacity).

### Static Method — `is_valid_rental_days(days)`
A utility that behaves independently of any object:

```python
Vehicle.is_valid_rental_days(5)   # True
Vehicle.is_valid_rental_days(0)   # False
Vehicle.is_valid_rental_days(-3)  # False
```

`calculate_rent()` calls this static method internally:

```python
if not Vehicle.is_valid_rental_days(days):
    return 0.0                     # invalid duration is rejected
```

---

## Validation Rules

- **Rental days must be greater than zero.**
- An invalid duration returns `0.0` from `calculate_rent()` and prints an error message.

---

## How to Run

```bash
python3 vehicle_rental.py
```

### Expected Output

```
=============================================
VEHICLE FLEET
=============================================

--- Car ---
Vehicle No:     KA-01-1234
Brand:          Toyota
Model:          Corolla
Rental Price:   $3500/day
Seats:          5

--- Car ---
Vehicle No:     KA-02-5678
Brand:          Hyundai
Model:          Creta
Rental Price:   $4200/day
Seats:          5

--- Bike ---
Vehicle No:     KA-03-9012
Brand:          Royal Enfield
Model:          Classic 350
Rental Price:   $1200/day
Engine Capacity: 350 cc

--- Bike ---
Vehicle No:     KA-04-3456
Brand:          Honda
Model:          Activa 6G
Rental Price:   $800/day
Engine Capacity: 110 cc

=============================================
RENTAL DURATION VALIDATION (Static Method)
=============================================
Valid for 0 days?  False
Valid for -3 days?  False
Valid for 5 days?  True

=============================================
RENT CALCULATION
=============================================
Toyota Corolla for 3 days:    $10500
Hyundai Creta for 5 days:    $21000
Royal Enfield Classic 350 for 2 days:    $2400
Honda Activa 6G for 7 days:    $5600

=============================================
INVALID DURATION DEMO
=============================================
Invalid rental duration: 0 days. Must be greater than zero.
Royal Enfield Classic 350 for 0 days:   $0.0
```

---

## Demo Flow in `vehicle_rental.py`

1. **Vehicle Fleet** — displays details of 2 cars and 2 bikes (shows inherited + child attributes).
2. **Duration Validation** — demonstrates the static method returning `True`/`False`.
3. **Rent Calculation** — `calculate_rent()` on each vehicle for valid durations.
4. **Invalid Duration Demo** — shows that renting for 0 days is rejected with `$0.0`.

---

## Key Takeaway

> **Inheritance lets a child class reuse the parent's data and logic while specializing with its own attributes — `Car` and `Bike` share everything with `Vehicle`, and only add what makes them different. Static methods provide validations that don't depend on any object.**

---

## Files

- `vehicle_rental.py` — full source code with comments and docstrings
- `README.md` — this documentation