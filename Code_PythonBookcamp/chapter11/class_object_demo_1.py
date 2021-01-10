# Demonstration-1
# The class definition


class Student:
    """ This is a simple Student class."""
    name = "Student class"

    def say_hi(self,student_name):
        """ A simple method to say hello to a student."""
        print(f"Hello {student_name}!")
        print(f"You are using {self.name} now.")


#Creating an object from Student class
object1 = Student()
#Invoking the method
object1.say_hi("John")

#Creating another object from Student class
object2 = Student()
#Invoking the method
object2.say_hi("Kate")

#print(type(object1))  # <class '__main__.Student'>
#print(type(object2))  # <class '__main__.Student'>
