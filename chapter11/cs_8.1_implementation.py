class Engineering:
    """Engineering is the parent class."""

    def __init__(self, college_name):
        # Initialize name
        self.college = college_name
        self.subject_1 = "Mathematics."
        self.subject_2 = "Soft-skills."


class ComputerScience(Engineering):
    """
    ComputerScience class inherits from Engineering.
    Default institution is St.Stephen.
    """

    def __init__(self, college_name=" St. Stephen",
                 special_subject="Compiler design."):
        """ Initialize starts from parent class."""
        super().__init__(college_name)
        self.subject_3 = special_subject

    def course_details(self):
        """Prints the course details of an institution."""
        print(f"Institution name:{self.college} college.")
        print("Computer science course includes:")
        print(f"1:{self.subject_1}")
        print(f"2:{self.subject_2}")
        print(f"3:{self.subject_3}")
        print("-" * 10)


# Computer science course at Presidency College
cs_course1 = ComputerScience(" Presidency",
                             "Python Programming")
cs_course1.course_details()

# Computer science course at St.Stephen College
cs_course2 = ComputerScience()
cs_course2.course_details()


