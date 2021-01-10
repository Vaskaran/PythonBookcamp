class Student:
    #name = "Student class"
    #rollno=10

    #def __init__(self):
    #print("You do not need to supply any parameter.")

    def __init__(self, name):
        print("You need to supply a name.")
        #print(f"You've supplied the name:{name}")

    #def __init__(self, name, roll_no):
    #print("Supply a name and a roll number.")


# Creating an object from Student class.
# Using the non-parameterised constructor.
#object1 = Student()
# Using the constructor that has one parameter.
object2 = Student("John")
# Using the constructor that accepts two parameters.
# object3 = Student("Robin",2)
