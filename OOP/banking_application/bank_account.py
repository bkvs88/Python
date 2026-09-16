"""
Simplified Banking Application using Object-Oriented Programming.

This module defines a BankAccount class that models a real-world bank
account, providing methods to deposit, withdraw, check balance, and
display account details. It also demonstrates core OOP concepts such as
class variables and class methods.
"""


class BankAccount:
    """
    Represents a bank account.

    Class variables:
        bank_name      : The name of the bank, shared by all accounts.
        total_accounts : Total number of accounts created so far.

    Instance attributes:
        account_holder : Name of the account holder.
        account_number : A unique auto-generated account number.
        balance        : Current available balance in the account.
    """

    # Class variable: shared across all instances of the class
    bank_name = "National Bank"

    # Class variable: keeps track of the total number of accounts created
    total_accounts = 0

    def __init__(self, account_holder, initial_balance=0):
        """
        Constructor. Runs automatically when a new BankAccount is created.

        Args:
            account_holder (str): Name of the account holder.
            initial_balance (float, optional): Opening balance. Defaults to 0.

        Side effects:
            - Increments the class variable total_accounts for every new account.
            - Assigns a unique account number based on total_accounts.
        """
        # Instance variables: unique to each account object
        self.account_holder = account_holder
        self.balance = initial_balance

        # Increment the class variable every time a new account is created
        BankAccount.total_accounts += 1

        # Auto-generate a unique account number (e.g., ACC0001)
        self.account_number = f"ACC{BankAccount.total_accounts:04d}"

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit.

        Returns:
            str: A confirmation message with the new balance,
                 or an error message if the amount is invalid.
        """
        # Validation: deposit amount must be greater than zero
        if amount <= 0:
            return "Deposit amount must be positive."

        # Add the amount to the current balance
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            str: A confirmation message with the new balance,
                 or an error message if the amount is invalid.

        Validation:
            - The withdrawal amount must be positive.
            - The user cannot withdraw more money than is available.
        """
        # Validation: withdrawal amount must be greater than zero
        if amount <= 0:
            return "Withdrawal amount must be positive."

        # Validation: prevent overdrawing the account
        if amount > self.balance:
            return "Insufficient funds. Cannot withdraw more than available balance."

        # Subtract the amount from the current balance
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

    def check_balance(self):
        """
        Return the current account balance.

        Returns:
            str: A message showing the current balance.
        """
        return f"Current balance: ${self.balance}"

    def display_account_details(self):
        """Print full details of the account to the console."""
        print(f"Bank:           {BankAccount.bank_name}")
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Balance:        ${self.balance}")

    @classmethod
    def change_bank_name(cls, new_name):
        """
        Change the bank name for every account.

        Args:
            new_name (str): The new bank name.
        """
        cls.bank_name = new_name

    @classmethod
    def get_total_accounts(cls):
        """
        Return the total number of accounts created.

        Returns:
            str: A message showing the total account count.
        """
        return f"Total bank accounts created: {cls.total_accounts}"


if __name__ == "__main__":
    # Create a couple of account objects from the BankAccount class
    acc1 = BankAccount("Sravan", 1000)  # Account with an initial balance
    acc2 = BankAccount("Kumaar")        # Account that starts at $0

    # Display details of the first account
    print("--- Account 1 ---")
    acc1.display_account_details()

    # Deposit some money and try over-withdrawing (should fail validation)
    print(acc1.deposit(500))
    print(acc1.withdraw(2000))  # More than available -> rejected

    # Withdraw a valid amount
    print(acc1.withdraw(300))

    # Check the updated balance
    print(acc1.check_balance())

    # Display details of the second account
    print("\n--- Account 2 ---")
    acc2.display_account_details()

    # Change the shared bank name using the class method
    print("\n--- Change bank name ---")
    BankAccount.change_bank_name("Global Trust Bank")

    # The new bank name now reflects on every existing account
    acc1.display_account_details()
    print(acc2.check_balance())

    # Bonus: verify the total number of accounts created
    print("\n" + BankAccount.get_total_accounts())