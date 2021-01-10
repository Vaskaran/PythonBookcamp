class Student:
    """ This is a Student class with a constructor."""

    def __init__(self, name, roll_no):
        """
        The name and roll_no is used to
        identify a student properly.
        """
        #initialize name
        self.name = name
        #initialize roll_no
        self.roll_no = roll_no

    def get_details(self):
        """
        This method prints the detail of a student.
        """
        print("The current student details are:")
        print(f"Name:{self.name}")
        print(f"Roll number:{self.roll_no}")

    def update_student_details(self, new_name, new_roll_no):
        """
        This method is used to update a student details.
        :param new_name: Updated student name.
        :param new_roll_no: Updated student roll_no
        :return: None
        """
        self.name = new_name
        self.roll_no = new_roll_no


# Creating an object from Student class.
student_1 = Student("Jack", 3)
#printing the details
student_1.get_details()
# Changing the attribute values of student_1
student_1.name = "Bob"
student_1.roll_no = 5
print("---After first update.---")
student_1.get_details()

#Second update using the method 'update_student_details'
student_1.update_student_details("Harry", 6)
print("---After second update.---")
student_1.get_details()
