"""
Learning Platform Override — Inheritance & Method Overriding Exercise.

Focuses specifically on:
- Inheritance      : User (parent) -> Student, Mentor, Admin (children)
- Common properties in the parent and role-specific behaviour in the children
- Method overriding: display_profile() implemented differently in each role
- Constructors     : __init__() for User and every child class via super()
- Class variables  : platform_name, total_users
- Objects          : instances of every role
"""


class User:
    """
    Base class representing any user on the learning platform.

    Class variables:
        platform_name : Name of the platform (shared across all users).
        total_users   : Total number of users registered.

    Attributes:
        name    : Full name of the user.
        email   : Email address of the user.
        user_id : Auto-generated unique user identifier.
    """

    platform_name = "Euron Super30"
    total_users = 0

    def __init__(self, name, email):
        """
        Constructor for User.

        Validates the email before creating the user.

        Args:
            name (str): Full name of the user.
            email (str): Email address of the user.

        Raises:
            ValueError: If the email address is invalid.
        """
        if not User.is_valid_email(email):
            raise ValueError(f"Invalid email address: {email}")

        self.name = name
        self.email = email

        # Increment the class variable every time a new user is created
        User.total_users += 1
        self.user_id = f"USR{User.total_users:03d}"

    def display_profile(self):
        """Print the base user profile details — to be overridden by children."""
        print(f"Platform:       {User.platform_name}")
        print(f"User ID:        {self.user_id}")
        print(f"Name:           {self.name}")
        print(f"Email:          {self.email}")

    def access_dashboard(self):
        """
        Show the dashboard available to every user.

        Returns:
            str: A generic welcome message.
        """
        return f"{self.name}: Welcome to your dashboard. Select a course to begin."

    @classmethod
    def get_total_users(cls):
        """
        Return the total number of users registered on the platform.

        Returns:
            str: A message showing the total user count.
        """
        return f"Total users registered: {cls.total_users}"

    @staticmethod
    def is_valid_email(email):
        """
        Validate whether an email address is well-formed.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if "@" not in email:
            return False
        local, domain = email.split("@", 1)
        if not local or "." not in domain:
            return False
        return True


class Student(User):
    """
    Child class representing a student, inheriting from User.

    Role-specific additions:
        course_name           : Course the student is enrolled in.
        completed_assignments : List of submitted assignment names.
    """

    def __init__(self, name, email, course_name):
        """
        Constructor for Student.

        Args:
            name (str): Full name of the student.
            email (str): Email address of the student.
            course_name (str): Name of the enrolled course.
        """
        super().__init__(name, email)
        self.course_name = course_name
        self.completed_assignments = []

    def submit_assignment(self, assignment_name):
        """
        Record the submission of an assignment.

        Args:
            assignment_name (str): Name or title of the assignment.

        Returns:
            str: Confirmation message, or a warning if already submitted.
        """
        if assignment_name in self.completed_assignments:
            return f"{self.name}: '{assignment_name}' was already submitted."

        self.completed_assignments.append(assignment_name)
        return f"{self.name}: '{assignment_name}' submitted successfully."

    def display_profile(self):
        """Override the parent method with student-specific details."""
        super().display_profile()
        print(f"Role:           Student")
        print(f"Course:         {self.course_name}")
        print(f"Assignments:    {len(self.completed_assignments)}")

    def access_dashboard(self):
        """Override the parent method with a student-specific dashboard."""
        return f"{self.name}: Student dashboard loaded — {self.course_name}."


class Mentor(User):
    """
    Child class representing a mentor, inheriting from User.

    Role-specific additions:
        expertise     : Area of expertise.
        mentee_names  : List of student names under this mentor.
    """

    def __init__(self, name, email, expertise):
        """
        Constructor for Mentor.

        Args:
            name (str): Full name of the mentor.
            email (str): Email address of the mentor.
            expertise (str): Area of expertise.
        """
        super().__init__(name, email)
        self.expertise = expertise
        self.mentee_names = []

    def assign_student(self, student):
        """
        Place a student under this mentor's guidance.

        Args:
            student (Student): The student to assign.

        Returns:
            str: Confirmation message or a warning if already assigned.
        """
        if student.name in self.mentee_names:
            return f"{self.name}: {student.name} is already your mentee."

        self.mentee_names.append(student.name)
        return f"{self.name}: {student.name} is now your mentee."

    def display_profile(self):
        """Override the parent method with mentor-specific details."""
        super().display_profile()
        print(f"Role:           Mentor")
        print(f"Expertise:      {self.expertise}")
        print(f"Mentees:        {len(self.mentee_names)}")

    def access_dashboard(self):
        """Override the parent method with a mentor-specific dashboard."""
        return f"{self.name}: Mentor dashboard loaded — review mentee submissions."


class Admin(User):
    """
    Child class representing an admin, inheriting from User.

    Role-specific additions:
        department : The department the admin manages.
        is_super   : Whether the admin holds full platform rights.
    """

    def __init__(self, name, email, department, is_super=False):
        """
        Constructor for Admin.

        Args:
            name (str): Full name of the admin.
            email (str): Email address of the admin.
            department (str): Department the admin manages.
            is_super (bool): Whether the admin has full platform rights.
        """
        super().__init__(name, email)
        self.department = department
        self.is_super = is_super

    def suspend_user(self, user):
        """
        Suspend a user's account (admin-only action).

        Args:
            user (User): The user to suspend.

        Returns:
            str: Confirmation message.
        """
        return f"{self.name}: Account of {user.name} ({user.user_id}) suspended."

    def display_profile(self):
        """Override the parent method with admin-specific details."""
        super().display_profile()
        print(f"Role:           Admin")
        print(f"Department:     {self.department}")
        print(f"Super Admin:    {'Yes' if self.is_super else 'No'}")

    def access_dashboard(self):
        """Override the parent method with an admin-specific dashboard."""
        return f"{self.name}: Admin dashboard loaded — platform analytics available."


if __name__ == "__main__":
    # --- Create objects of each role ---
    student1 = Student("Sravan Kumar", "sravan@super30.com", "Data Science")
    student2 = Student("Divya Kumar", "divya@super30.com", "Web Development")
    mentor1 = Mentor("Deepansh", "deepansh@super30.com", "Data Science & Python")
    admin1 = Admin("Kesav venkat", "kesav@super30.com", "Operations", is_super=True)

    # --- Role-specific functionality ---
    print("=" * 45)
    print("ROLE-SPECIFIC ACTIONS")
    print("=" * 45)
    print(student1.submit_assignment("Assignment 1 - Python Basics"))
    print(mentor1.assign_student(student1))
    print(mentor1.assign_student(student2))
    print(admin1.suspend_user(student2))

    # --- Demonstrate method overriding via runtime polymorphism ---
    print("\n" + "=" * 45)
    print("METHOD OVERRIDING — display_profile()")
    print("=" * 45)

    # Same method name, different output per object type
    for user in [student1, mentor1, admin1]:
        print(f"\n--- {user.__class__.__name__} ---")
        user.display_profile()

    # --- Demonstrate access_dashboard() override too ---
    print("\n" + "=" * 45)
    print("METHOD OVERRIDING — access_dashboard()")
    print("=" * 45)
    for user in [student1, student2, mentor1, admin1]:
        print(user.access_dashboard())

    # --- Class method: total users ---
    print("\n" + "=" * 45)
    print("PLATFORM SUMMARY")
    print("=" * 45)
    print(User.get_total_users())