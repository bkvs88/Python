"""
Super30 Learning Platform — A Complete OOP Exercise.

Combines every core concept covered so far:
- Inheritance      : User -> Student, Mentor
- Class variables  : total_users, platform_name, all_mentees
- Class methods    : get_total_users(), get_mentor_summary()
- Static method    : is_valid_email()
- Constructors     : __init__() for User, Student, and Mentor
- Instance methods : display_profile(), submit_assignment(), assign_student(), etc.
- Method overriding: display_profile() overridden in both child classes
- Objects          : multiple Student and Mentor instances
"""


class User:
    """
    Base class representing any user on the Super30 platform.

    Class variables:
        platform_name : Name of the platform (shared across all users).
        total_users   : Total number of users registered.

    Attributes:
        name    : Full name of the user.
        email   : Email address of the user.
        user_id : Auto-generated unique user identifier.
    """

    platform_name = "Super30"
    total_users = 0

    def __init__(self, name, email):
        """
        Constructor for User.

        Validates the email using the static method before creating the user.

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
        """Print the base user profile details."""
        print(f"Platform:       {User.platform_name}")
        print(f"User ID:        {self.user_id}")
        print(f"Name:           {self.name}")
        print(f"Email:          {self.email}")

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

        Checks that the email contains exactly one '@' and at least one
        '.' after the '@'.

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

    Inherits all User attributes and methods.
    Adds:
        course_name           : Name of the assigned course.
        total_assignments     : Total assignments in the course.
        completed_assignments : List of submitted assignment names.
    """

    def __init__(self, name, email, course_name):
        """
        Constructor for Student.

        Calls the parent __init__ with super(), then sets course details.

        Args:
            name (str): Full name of the student.
            email (str): Email address of the student.
            course_name (str): Name of the course assigned to the student.
        """
        # Reuse the parent constructor to set shared attributes and validate email
        super().__init__(name, email)

        self.course_name = course_name
        self.total_assignments = 5
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
            return f"{self.name}: Assignment '{assignment_name}' already submitted."

        self.completed_assignments.append(assignment_name)
        return f"{self.name}: Assignment '{assignment_name}' submitted. [{len(self.completed_assignments)}/{self.total_assignments}]"

    def assign_course(self, new_course):
        """
        Assign a new course to the student. Clears previous assignment history.

        Args:
            new_course (str): Name of the new course.
        """
        self.course_name = new_course
        self.completed_assignments = []
        print(f"{self.name}: Course changed to '{self.course_name}'. Previous assignments cleared.")

    def get_progress(self):
        """
        Return the completion percentage as a float.

        Returns:
            float: Percentage of assignments completed (0.0 to 100.0).
        """
        if self.total_assignments == 0:
            return 0.0
        return (len(self.completed_assignments) / self.total_assignments) * 100

    def display_profile(self):
        """Override the parent method to include student-specific information."""
        # Reuse parent's display_profile method
        super().display_profile()
        print(f"Role:           Student")
        print(f"Course:         {self.course_name}")
        print(f"Assignments:    {len(self.completed_assignments)}/{self.total_assignments}")
        print(f"Progress:       {self.get_progress():.0f}%")


class Mentor(User):
    """
    Child class representing a mentor, inheriting from User.

    Inherits all User attributes and methods.
    Adds:
        expertise         : Area of expertise.
        students_assigned : List of student user IDs assigned under this mentor.

    Class variable:
        all_mentees : List of all student IDs assigned across every mentor.
    """

    all_mentees = []

    def __init__(self, name, email, expertise):
        """
        Constructor for Mentor.

        Calls the parent __init__ with super(), then sets expertise.

        Args:
            name (str): Full name of the mentor.
            email (str): Email address of the mentor.
            expertise (str): Area of expertise.
        """
        # Reuse the parent constructor to set shared attributes
        super().__init__(name, email)

        self.expertise = expertise
        self.students_assigned = []

    def assign_student(self, student):
        """
        Assign a student under this mentor's guidance.

        Args:
            student (Student): The student object to assign.

        Returns:
            str: Confirmation message or a warning if already assigned.
        """
        if student.user_id in self.students_assigned:
            return f"{self.name}: Student '{student.name}' is already assigned under you."

        self.students_assigned.append(student.user_id)
        Mentor.all_mentees.append(student.user_id)
        return f"{self.name}: Student '{student.name}' ({student.user_id}) has been assigned to you."

    def display_profile(self):
        """Override the parent method to include mentor-specific information."""
        # Reuse parent's display_profile method
        super().display_profile()
        print(f"Role:           Mentor")
        print(f"Expertise:      {self.expertise}")
        print(f"Students:       {len(self.students_assigned)}")

    @classmethod
    def get_mentor_summary(cls):
        """
        Return a summary of total students assigned across all mentors.

        Returns:
            str: Total number of students assigned to all mentors combined.
        """
        return f"Total students assigned to mentors: {len(cls.all_mentees)}"


if __name__ == "__main__":
    # --- Register a mentor ---
    mentor1 = Mentor("Aditi Mehta", "aditi@super30.com", "Data Science & Python")

    # --- Register several students ---
    student1 = Student("Sravan Kumar",  "sravan@super30.com",  "Data Science")
    student2 = Student("Kumaar Reddy",  "kumaar@super30.com",  "Web Development")
    student3 = Student("Kesav Singh",   "kesav@super30.com",   "Cyber Security")

    # --- Mentor assigns students ---
    print("=" * 45)
    print("STUDENT REGISTRATION")
    print("=" * 45)
    print(mentor1.assign_student(student1))
    print(mentor1.assign_student(student2))
    print(mentor1.assign_student(student3))
    print(mentor1.assign_student(student1))  # Duplicate — should warn

    # --- Students submit assignments ---
    print("\n" + "=" * 45)
    print("ASSIGNMENT SUBMISSIONS")
    print("=" * 45)
    print(student1.submit_assignment("Assignment 1 - Python Basics"))
    print(student1.submit_assignment("Assignment 2 - NumPy"))
    print(student1.submit_assignment("Assignment 3 - Pandas"))
    print(student2.submit_assignment("Assignment 1 - HTML/CSS"))
    print(student2.submit_assignment("Assignment 2 - JavaScript"))
    print(student3.submit_assignment("Assignment 1 - Networking Basics"))
    print(student3.submit_assignment("Assignment 1 - Networking Basics"))  # Duplicate

    # --- Display all profiles ---
    print("\n" + "=" * 45)
    print("USER PROFILES")
    print("=" * 45)

    for user in [mentor1, student1, student2, student3]:
        print(f"\n--- {user.__class__.__name__} ---")
        user.display_profile()

    # --- Demonstrate course update ---
    print("\n" + "=" * 45)
    print("COURSE UPDATE")
    print("=" * 45)
    student3.assign_course("Full Stack Development")

    # --- Demonstrate email validation (static method) ---
    print("\n" + "=" * 45)
    print("EMAIL VALIDATION (Static Method)")
    print("=" * 45)
    emails = ["valid@mail.com", "invalid-mail.com", "@missinglocal.com", "missingdot@com"]
    for email in emails:
        print(f"'{email}' -> {User.is_valid_email(email)}")

    # --- Display progress & mentor summary ---
    print("\n" + "=" * 45)
    print("STUDENT PROGRESS")
    print("=" * 45)
    for student in [student1, student2, student3]:
        print(f"{student.name}: {student.get_progress():.0f}% complete")

    # --- Class method: total users & mentor summary ---
    print("\n" + "=" * 45)
    print("PLATFORM SUMMARY")
    print("=" * 45)
    print(User.get_total_users())
    print(Mentor.get_mentor_summary())
