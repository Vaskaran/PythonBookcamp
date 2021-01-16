class Student:
    """ This is a Student class with a constructor."""
    def __init__(self, name, roll_no):
        """
        The name and roll_no is used to
        identify a student properly.
        """
        print("This constructor has two parameters.")
        #initialize name
        self.name = name
        #initialize roll_no
        self.roll_no = roll_no
        print(f"The student name is: {self.name}")
        print(f"The student roll number is: {self.roll_no}")


# Creating an object from Student class.
# Using the constructor that accepts two parameters.
student_jack = Student("Jack", 3)


# Changing the attribute values of student_jack
student_jack .name = "Bob"
student_jack .roll_no = 5
print("Now student_jack has the following details:")
print(f"Student name= {student_jack.name}")
print(f"Student roll number= {student_jack.roll_no}")
