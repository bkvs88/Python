"""
Online Learning Platform — Demonstrates Inheritance with Course & PremiumCourse.

This module models an EdTech platform where a base Course class is extended
by a PremiumCourse child class, adding mentor support and live sessions.
"""


class Course:
    """
    Base class representing a regular course on the platform.

    Class variable:
        total_courses : Total number of courses created.

    Attributes:
        name            : Course title.
        instructor      : Name of the instructor.
        duration        : Course duration in hours.
        price           : Course price in dollars.
    """

    # Class variable: shared across all courses
    total_courses = 0

    def __init__(self, name, instructor, duration, price):
        """
        Constructor for Course.

        Args:
            name (str): Course title.
            instructor (str): Instructor name.
            duration (int): Duration in hours.
            price (float): Course price in dollars.
        """
        self.name = name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        # Increment the class variable for every new course created
        Course.total_courses += 1

    def show_course_details(self):
        """Print the base course details to the console."""
        print(f"Course:         {self.name}")
        print(f"Instructor:     {self.instructor}")
        print(f"Duration:       {self.duration} hours")
        print(f"Price:          ${self.price}")

    def calculate_discount(self, discount_percent):
        """
        Calculate the discounted price of the course.

        Args:
            discount_percent (float): Discount percentage (e.g., 20 for 20%).

        Returns:
            str: A message with the discount and final price.
        """
        discount_amount = self.price * (discount_percent / 100)
        final_price = self.price - discount_amount
        return f"{discount_percent}% off -> ${final_price:.2f}"

    @classmethod
    def get_course_count(cls):
        """
        Return the total number of courses created.

        Returns:
            str: A message showing the total course count.
        """
        return f"Total courses created: {cls.total_courses}"


class PremiumCourse(Course):
    """
    Child class representing a premium course, inheriting from Course.

    Inherits all Course attributes and methods.
    Adds:
        mentor_support : Whether 1-on-1 mentor support is included (bool).
        live_sessions  : Whether live sessions are included (bool).
    """

    def __init__(self, name, instructor, duration, price, mentor_support, live_sessions):
        """
        Constructor for PremiumCourse.

        Calls the parent __init__ with super(), then adds premium attributes.

        Args:
            name (str): Course title.
            instructor (str): Instructor name.
            duration (int): Duration in hours.
            price (float): Course price in dollars.
            mentor_support (bool): True if mentor support is included.
            live_sessions (bool): True if live sessions are included.
        """
        # Reuse the parent constructor to set shared attributes
        super().__init__(name, instructor, duration, price)

        # Premium-specific attributes
        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_course_details(self):
        """
        Override the parent method to include premium features.
        Calls super().show_course_details() first, then prints premium info.
        """
        # Reuse parent's show_course_details method
        super().show_course_details()
        print(f"Mentor Support: {'Yes' if self.mentor_support else 'No'}")
        print(f"Live Sessions:  {'Yes' if self.live_sessions else 'No'}")


if __name__ == "__main__":
    # --- Create regular Course objects (parent class) ---
    core_python = Course("Core Python Basics", "Sravan Kumar", 12, 499)
    web_dev     = Course("Full Stack Web Dev", "Aditi Mehta", 40, 999)

    # --- Create PremiumCourse objects (child class) ---
    premium_ds   = PremiumCourse("Data Science Pro", "Kesav Singh", 60, 1499, True, True)
    premium_cyber= PremiumCourse("Cyber Security Mastery", "Rohan Das", 55, 1299, True, True)
    premium_py   = PremiumCourse("Advanced Python", "Kumaar Reddy", 30, 799, False, False)

    # --- Display all course details ---
    print("=" * 45)
    print("COURSE CATALOG")
    print("=" * 45)

    for course in [core_python, web_dev, premium_ds, premium_cyber, premium_py]:
        print(f"\n--- {course.__class__.__name__} ---")
        course.show_course_details()

    # --- Demonstrate discount calculation (inherited by child class) ---
    print("\n" + "=" * 45)
    print("DISCOUNT OFFERS")
    print("=" * 45)
    print(f"Core Python: {core_python.calculate_discount(20)}")
    print(f"Data Science Pro: {premium_ds.calculate_discount(30)}")
    print(f"Advanced Python: {premium_py.calculate_discount(10)}")

    # --- Use the class method to see the total course count ---
    print("\n" + "=" * 45)
    print("COURSE COUNT (Class Method)")
    print("=" * 45)
    print(Course.get_course_count())