"""
Payment Processing System — Demonstrates Abstract Classes & Runtime Polymorphism.

An abstract Payment base class defines the pay() contract, and three concrete
implementations (CreditCard, UPI, NetBanking) provide their own behaviour.
The same pay() method is invoked on different objects to demonstrate runtime
polymorphism via method overriding.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    """
    Abstract base class representing a payment method.

    Attributes:
        amount (float): The amount to be paid.
    """

    def __init__(self, amount):
        """
        Constructor for Payment.

        Args:
            amount (float): The amount to be paid.
        """
        self.amount = amount

    @abstractmethod
    def pay(self):
        """
        Process the payment.

        This method must be implemented by every concrete payment type.
        """
        pass


class CreditCardPayment(Payment):
    """
    Concrete payment using a credit card.

    Attributes:
        card_number (str): The credit card number.
    """

    def __init__(self, amount, card_number):
        """
        Constructor for CreditCardPayment.

        Args:
            amount (float): The amount to be paid.
            card_number (str): The masked credit card number.
        """
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        """Charge the amount to the credit card."""
        print(f"Charging ${self.amount:.2f} to credit card ending in "
              f"{self.card_number[-4:]}.")


class UPIPayment(Payment):
    """
    Concrete payment using UPI.

    Attributes:
        upi_id (str): The UPI ID of the user.
    """

    def __init__(self, amount, upi_id):
        """
        Constructor for UPIPayment.

        Args:
            amount (float): The amount to be paid.
            upi_id (str): The UPI ID, e.g., user@bank.
        """
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        """Request the amount through the user's UPI ID."""
        print(f"Sending payment request of ${self.amount:.2f} to {self.upi_id}.")


class NetBankingPayment(Payment):
    """
    Concrete payment using net banking.

    Attributes:
        bank_name (str): The user's bank.
    """

    def __init__(self, amount, bank_name):
        """
        Constructor for NetBankingPayment.

        Args:
            amount (float): The amount to be paid.
            bank_name (str): The user's bank, e.g., HDFC.
        """
        super().__init__(amount)
        self.bank_name = bank_name

    def pay(self):
        """Redirect the user to their bank's net banking portal."""
        print(f"Redirecting to {self.bank_name} net banking portal for "
              f"${self.amount:.2f}.")


def process_payments(payment_list):
    """
    Demonstrate runtime polymorphism.

    The same pay() method is called on every payment object, and the
    correct implementation is dispatched at runtime based on the object type.

    Args:
        payment_list (list[Payment]): A list of Payment objects.
    """
    print("Processing payments...")
    for payment_method in payment_list:
        payment_method.pay()


if __name__ == "__main__":
    # Creating different payment objects
    credit_card = CreditCardPayment(250.75, "1234 5678 9012 3456")
    upi = UPIPayment(120.00, "sravan@hdfcbank")
    net_banking = NetBankingPayment(89.50, "ICICI")

    # Calling the same method on different objects — runtime polymorphism
    process_payments([credit_card, upi, net_banking])