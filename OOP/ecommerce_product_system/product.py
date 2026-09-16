"""
E-Commerce Product System — Demonstrates Classes, Static Methods, and OOP in Python.

This module defines a Product class for a small e-commerce application,
with methods for displaying products, updating stock, calculating totals,
and a static method for price validation.
"""


class Product:
    """
    Represents a product in an e-commerce application.

    Attributes:
        product_id    : Unique identifier for the product.
        name          : Name of the product.
        price         : Unit price in dollars.
        category      : Product category (e.g., Electronics, Books).
        stock_quantity: Number of units currently in stock.
    """

    def __init__(self, product_id, name, price, category, stock_quantity):
        """
        Constructor for Product.

        Args:
            product_id (str): Unique product identifier.
            name (str): Product name.
            price (float): Unit price in dollars.
            category (str): Product category.
            stock_quantity (int): Number of units in stock.

        Raises:
            ValueError: If price is not valid (must be greater than zero).
        """
        # Validate price before setting it
        if not Product.is_valid_price(price):
            raise ValueError(f"Invalid price: ${price}. Price must be greater than zero.")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def display_product(self):
        """Print product details to the console."""
        print(f"Product ID:     {self.product_id}")
        print(f"Name:           {self.name}")
        print(f"Price:          ${self.price:.2f}")
        print(f"Category:       {self.category}")
        print(f"Stock:          {self.stock_quantity} units")

    def update_stock(self, quantity):
        """
        Update the stock quantity after a purchase or restock.

        Args:
            quantity (int): Number of units to add (positive) or remove (negative).

        Returns:
            str: Confirmation message or error message.

        Validation:
            - Cannot reduce stock below zero.
        """
        new_stock = self.stock_quantity + quantity

        # Prevent negative stock
        if new_stock < 0:
            return f"Insufficient stock for {self.name}. Only {self.stock_quantity} available."

        self.stock_quantity = new_stock
        action = "restocked" if quantity > 0 else "purchased"
        return f"{self.name}: {action} {abs(quantity)} unit(s). New stock: {self.stock_quantity}"

    def calculate_total_price(self, quantity):
        """
        Calculate the total price for purchasing multiple units of this product.

        Args:
            quantity (int): Number of units to buy.

        Returns:
            float: Total price, or 0.0 if stock is insufficient.

        Validation:
            - Quantity must be positive.
            - Stock must be sufficient to fulfill the order.
        """
        # Validation: quantity must be positive
        if quantity <= 0:
            return 0.0

        # Validation: check stock availability
        if quantity > self.stock_quantity:
            print(f"Not enough stock for {self.name}. Requested: {quantity}, Available: {self.stock_quantity}")
            return 0.0

        total = self.price * quantity
        return total

    @staticmethod
    def is_valid_price(price):
        """
        Check if a given price is valid.

        Args:
            price (float): The price to validate.

        Returns:
            bool: True if price is greater than zero, False otherwise.
        """
        return price > 0


if __name__ == "__main__":
    # --- Create 5 Product objects ---
    laptop   = Product("PROD001", "HP Laptop",        54999.99, "Electronics",  10)
    phone    = Product("PROD002", "Samsung Galaxy",    32999.50, "Electronics",  25)
    book     = Product("PROD003", "Python Mastery",      499.00, "Books",        100)
    headphones= Product("PROD004", "Sony Headphones",   7999.99, "Electronics",  30)
    backpack = Product("PROD005", "Wildcraft Backpack",  2499.00, "Accessories",  50)

    all_products = [laptop, phone, book, headphones, backpack]

    # --- Display all products ---
    print("=" * 45)
    print("PRODUCT CATALOG")
    print("=" * 45)

    for product in all_products:
        print(f"\n--- {product.category} ---")
        product.display_product()

    # --- Demonstrate price validation (static method) ---
    print("\n" + "=" * 45)
    print("PRICE VALIDATION (Static Method)")
    print("=" * 45)
    print(f"Is $100.00 valid?   {Product.is_valid_price(100.00)}")
    print(f"Is $0.00 valid?     {Product.is_valid_price(0.00)}")
    print(f"Is $-50.00 valid?   {Product.is_valid_price(-50.00)}")

    # --- Demonstrate buying and updating stock ---
    print("\n" + "=" * 45)
    print("PURCHASE DEMO")
    print("=" * 45)

    # Buy 2 laptops
    print(f"\nBuying 2 x {laptop.name}...")
    total = laptop.calculate_total_price(2)
    if total > 0:
        print(f"Total cost: ${total:.2f}")
        print(laptop.update_stock(-2))

    # Buy 1 phone
    print(f"\nBuying 1 x {phone.name}...")
    total = phone.calculate_total_price(1)
    if total > 0:
        print(f"Total cost: ${total:.2f}")
        print(phone.update_stock(-1))

    # Try to buy more books than available (should fail)
    print(f"\nTrying to buy 999 x {book.name}...")
    total = book.calculate_total_price(999)
    if total > 0:
        print(f"Total cost: ${total:.2f}")
        print(book.update_stock(-999))

    # --- Demonstrate restocking ---
    print("\n" + "=" * 45)
    print("RESTOCK DEMO")
    print("=" * 45)
    print(laptop.update_stock(5))   # Restock 5 more laptops

    # --- Updated product details ---
    print("\n" + "=" * 45)
    print("UPDATED PRODUCT DETAILS")
    print("=" * 45)
    for product in all_products:
        print(f"\n--- {product.category} ---")
        product.display_product()