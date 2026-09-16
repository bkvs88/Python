"""
Employee and Developer System — Demonstrates Class Inheritance in Python.

This module defines a base Employee class and a Developer child class
that inherits from it, showing how child classes extend parent functionality.
"""


class Employee:
    """
    Base class representing a generic employee.

    Attributes:
        employee_id  : Unique identifier for the employee.
        name         : Full name of the employee.
        salary       : Annual salary in dollars.
        department   : Department the employee belongs to.
    """

    def __init__(self, employee_id, name, salary, department):
        """
        Constructor for Employee.

        Args:
            employee_id (str): Unique employee identifier.
            name (str): Full name of the employee.
            salary (float): Annual salary in dollars.
            department (str): Department the employee belongs to.
        """
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        """Print employee details to the console."""
        print(f"Employee ID:    {self.employee_id}")
        print(f"Name:           {self.name}")
        print(f"Salary:         ${self.salary:,}")
        print(f"Department:     {self.department}")

    def get_annual_salary(self):
        """Return the annual salary as a formatted string."""
        return f"{self.name}'s annual salary: ${self.salary:,}"


class Developer(Employee):
    """
    Child class representing a developer, inheriting from Employee.

    Inherits all Employee attributes and methods.
    Adds:
        language  : Primary programming language.
        experience: Years of professional experience.
    """

    def __init__(self, employee_id, name, salary, department, language, experience):
        """
        Constructor for Developer.

        Calls the parent __init__ using super(), then sets developer-specific attributes.

        Args:
            employee_id (str): Unique employee identifier.
            name (str): Full name of the developer.
            salary (float): Annual salary in dollars.
            department (str): Department the developer belongs to.
            language (str): Primary programming language.
            experience (int): Years of development experience.
        """
        # Call the parent (Employee) constructor to set shared attributes
        super().__init__(employee_id, name, salary, department)

        # Developer-specific attributes
        self.language = language
        self.experience = experience

    def display_details(self):
        """
        Override the parent method to include developer-specific information.
        Calls the parent method first, then adds language and experience.
        """
        # Reuse parent's display_details method
        super().display_details()
        print(f"Language:       {self.language}")
        print(f"Experience:     {self.experience} years")


if __name__ == "__main__":
    # --- Create Employee objects (parent class) ---
    emp1 = Employee("EMP001", "Aditi Mehta", 60000, "Human Resources")
    emp2 = Employee("EMP002", "Rohan Das", 55000, "Finance")

    # --- Create Developer objects (child class) ---
    dev1 = Developer("EMP003", "Sravan Kumar", 90000, "Engineering", "Python", 5)
    dev2 = Developer("EMP004", "Kumaar Reddy", 85000, "Engineering", "Java", 3)
    dev3 = Developer("EMP005", "Kesav Singh", 95000, "Data Science", "Python", 7)

    # --- Display all employee details ---
    print("=" * 45)
    print("EMPLOYEE RECORDS")
    print("=" * 45)

    for emp in [emp1, emp2, dev1, dev2, dev3]:
        print(f"\n--- {emp.__class__.__name__} ---")
        emp.display_details()

    # --- Demonstrate parent class method on a child object ---
    print("\n" + "=" * 45)
    print("SALARY DETAILS")
    print("=" * 45)
    print(dev1.get_annual_salary())
    print(dev3.get_annual_salary())