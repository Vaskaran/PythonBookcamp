# Demonstration-2

"""
If you do not supply any constructor for your class,
Python will  call the superclass constructor for you.
To understand ‘Superclass’, you need to learn inheritance
which I discuss later in this chapter.
In Python 3.x , object is the root of all classes.
Once you learn inheritance, you’ll see that in
this demonstration,class Student and
class Student(object) are same.
"""


#class Student(object):

class Student:
    """ This is a Student class with a constructor."""

    def __init__(self, name, roll_no):
        """
        The name and roll_no is used to
        identify a student properly.
        """
        print(f"The student name is: {name}")
        print(f"The student roll number is: {roll_no}")


# Creating an object from Student class.
# Using the constructor which has two parameters.
student_robin = Student("Robin", 2)
# Another object
#student_kate = Student("Kate", 4)

