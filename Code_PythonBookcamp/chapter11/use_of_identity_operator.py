class Student:
    """ This is a Student class with a constructor."""
    def __init__(self, name, roll_no):
        """
        The name and roll_no is used to
        identify a student properly.
        """
        self.name = name
        #initialize roll_no
        self.roll_no = roll_no
        print(f"Name:{self.name}")
        print(f"Roll number is:{self.roll_no}")


# Creating an object from Student class.
# Using the constructor that accepts two parameters.
print("Creating jack object:")
jack = Student("Jack", 3)
print("\nCreating jack_2 object:")
jack_2 = Student("Jack", 3)

print("\nUse of identity operator:")
print("jack is jack_2?", jack is jack_2) # False

print("Introducing jack_3 object")
jack_3 = jack
print("jack_3 is jack?", jack_3 is jack) # True
print("jack_3 is jack_2?", jack_3 is jack_2) # False

print("-"*15)
# You append the following lines to test further
print("The type(jack) is Student?")
print(type(jack) is Student) # True

print("The type(jack) is int?")
print(type(jack) is int) #False

print("The type(jack) is NOT int?")
print(type(jack) is not int) # True
