# E-Commerce Product System

A small e-commerce application built with **Object-Oriented Programming (OOP)** in Python. It defines a `Product` class to manage products, handles stock updates, calculates purchase totals, and validates prices.

---

## Program Overview

The program defines a `Product` class where every product stores:

- **Product ID** — a unique identifier
- **Name** — the product's name
- **Price** — unit price in dollars
- **Category** — e.g., Electronics, Books, Accessories
- **Stock quantity** — number of units currently available

A **static method** (`is_valid_price`) validates that prices are greater than zero independently of any product object.

---

## Feature / Functionalities

| Method | Type | Description |
|---|---|---|
| `__init__(product_id, name, price, category, stock_quantity)` | Constructor | Creates a product and validates the price |
| `display_product()` | Instance method | Prints all product details |
| `update_stock(quantity)` | Instance method | Adds (restock) or removes (purchase) units; prevents negative stock |
| `calculate_total_price(quantity)` | Instance method | Returns the total cost for a quantity, checking stock availability |
| `is_valid_price(price)` | Static method | Returns `True` if price > 0, `False` otherwise |

---

## OOP Concepts Used

### Class
`Product` is the **blueprint** that defines what each product looks like and what it can do.

### Objects
5 products are created from the class — `laptop`, `phone`, `book`, `headphones`, and `backpack` — each with its own data.

### `__init__` (Constructor)
Runs automatically on creation. It calls the static `is_valid_price()` method and raises a `ValueError` if the price is invalid, before setting the product attributes.

### Instance Methods
`display_product()`, `update_stock()`, and `calculate_total_price()` operate on a specific product object through `self`.

### Static Method
`is_valid_price(price)` is decorated with `@staticmethod`. It is **not** tied to a specific object or the class — it simply validates a price and returns a boolean:

```python
Product.is_valid_price(100.0)   # True
Product.is_valid_price(0.0)     # False
Product.is_valid_price(-50.0)   # False
```

---

## Validation Rules

- **Price** must be **greater than zero** — enforced at construction time.
- **Stock** can never go below zero.
- **Purchases** with quantity `<= 0` or with insufficient stock are rejected (total returns `0.0`).

---

## How to Run

From the project directory:

```bash
python3 product.py
```

### Expected Output (Highlights)

```
PRODUCT CATALOG

--- Electronics ---
Product ID:     PROD001
Name:           HP Laptop
Price:          $54999.99
Category:       Electronics
Stock:          10 units
...
PRICE VALIDATION (Static Method)
Is $100.00 valid?   True
Is $0.00 valid?     False
Is $-50.00 valid?   False

PURCHASE DEMO
Buying 2 x HP Laptop...
Total cost: $109999.98
HP Laptop: purchased 2 unit(s). New stock: 8
...

RESTOCK DEMO
HP Laptop: restocked 5 unit(s). New stock: 13

UPDATED PRODUCT DETAILS
--- Electronics ---
Product ID:     PROD001
Name:           HP Laptop
Price:          $54999.99
Category:       Electronics
Stock:          13 units
...
```

---

## Demo Flow in `product.py`

1. **Product Catalog** — displays all 5 products.
2. **Price Validation** — shows `is_valid_price()` working on valid and invalid prices.
3. **Purchase Demo** — buys 2 laptops and 1 phone, then tries (and fails) to buy 999 books due to insufficient stock.
4. **Restock Demo** — restocks 5 laptops.
5. **Updated Details** — re-displays all products with the changed stock.

---

## Key Takeaway

> A **class** groups data and behavior into a blueprint; **objects** are real instances built from it; **instance methods** work on object data; and a **static method** provides utility logic that doesn't depend on any object.

---

## Files

- `product.py` — full source code with comments and docstrings
- `README.md` — this documentation file