"""
Employee Management System — OOP Exercise in Python.

Models employees with ID, name, department, salary, and designation.
Provides methods to display employee information, update the salary,
and calculate annual salary (with support for monthly pay tracking).
"""


class Employee:
    """
    Base class representing an employee.

    Class variable:
        total_employees : Total number of Employee objects created.

    Attributes:
        employee_id : Unique identifier for the employee.
        name        : Full name of the employee.
        department  : Department the employee belongs to.
        salary      : Monthly salary in dollars.
        designation : Job title / designation of the employee.
    """

    total_employees = 0

    def __init__(self, employee_id, name, department, salary, designation):
        """
        Constructor for Employee.

        Args:
            employee_id (str): Unique employee identifier.
            name (str): Full name of the employee.
            department (str): Department the employee works in.
            salary (float): Monthly salary in dollars.
            designation (str): Job title of the employee.
        """
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

        # Increment the class variable for every new employee created
        Employee.total_employees += 1

    def display_info(self):
        """Print the full employee information to the console."""
        print(f"Employee ID:    {self.employee_id}")
        print(f"Name:           {self.name}")
        print(f"Department:     {self.department}")
        print(f"Designation:    {self.designation}")
        print(f"Monthly Salary: ${self.salary:,.2f}")

    def update_salary(self, new_salary):
        """
        Update the employee's monthly salary.

        Args:
            new_salary (float): New monthly salary in dollars.
        """
        old_salary = self.salary
        self.salary = new_salary
        print(f"{self.name}: salary updated from ${old_salary:,.2f} "
              f"to ${self.salary:,.2f} per month.")

    def calculate_annual_salary(self):
        """
        Calculate the employee's annual salary.

        Returns:
            float: Annual salary (12 x monthly salary).
        """
        return self.salary * 12

    @classmethod
    def get_total_employees(cls):
        """
        Return the total number of employees created.

        Returns:
            str: A message showing the total employee count.
        """
        return f"Total employees created: {cls.total_employees}"


if __name__ == "__main__":
    # --- Create 5 Employee objects ---
    emp1 = Employee("EMP001", "Sravan Kumar", "Engineering", 7500.50, "Software Engineer")
    emp2 = Employee("EMP002", "Divya Kumar", "Human Resources", 5200.00, "HR Executive")
    emp3 = Employee("EMP003", "Deepansh", "Finance", 6100.75, "Financial Analyst")
    emp4 = Employee("EMP004", "Kesav Singh", "Data Science", 8200.00, "Data Scientist")
    emp5 = Employee("EMP005", "Aditi Mehta", "Marketing", 4800.25, "Marketing Manager")

    # --- Display all employee information ---
    print("=" * 45)
    print("EMPLOYEE RECORDS")
    print("=" * 45)

    for emp in [emp1, emp2, emp3, emp4, emp5]:
        print(f"\n--- {emp.employee_id}: {emp.name} ---")
        emp.display_info()

    # --- Show annual salary of every employee ---
    print("\n" + "=" * 45)
    print("ANNUAL SALARY (calculate_annual_salary)")
    print("=" * 45)
    for emp in [emp1, emp2, emp3, emp4, emp5]:
        print(f"{emp.name}: ${emp.calculate_annual_salary():,.2f}/year")

    # --- Demonstrate salary update ---
    print("\n" + "=" * 45)
    print("SALARY UPDATES (update_salary)")
    print("=" * 45)
    emp1.update_salary(8500.50)
    emp4.update_salary(9000.00)

    # --- Verify the update with the new annual salary ---
    print("\n" + "=" * 45)
    print("UPDATED ANNUAL SALARIES")
    print("=" * 45)
    print(f"{emp1.name}: ${emp1.calculate_annual_salary():,.2f}/year")
    print(f"{emp4.name}: ${emp4.calculate_annual_salary():,.2f}/year")

    # --- Class method summary ---
    print("\n" + "=" * 45)
    print("EMPLOYEE SUMMARY")
    print("=" * 45)
    print(Employee.get_total_employees())