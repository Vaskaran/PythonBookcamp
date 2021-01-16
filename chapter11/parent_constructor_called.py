class Parent:
    def __init__(self):
        print(f"The Parent constructor is called.")


class Student(Parent):
    """ This is a Student class with a constructor."""
'''
    def __init__(self,name,roll_no):
        """
        The name and roll_no is used to
        identify a student properly.
        """
        print(f"The student name is:{name}")
        print(f"The student roll no is:{roll_no}")

'''
# Creating an object from Student class.
# Using the constructor that accepts two parameters.
#student_robin = Student("Robin",2)
student_robin = Student()

print(type(student_robin))  # <class '__main__.Student'>
