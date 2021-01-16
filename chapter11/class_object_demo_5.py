class Student:
    def __init__(self,name,roll_no):
        #initialize name
        self.name = name
        #initialize roll_no
        self.roll_no = roll_no
        self.college = "St.Stephen"

    def get_details(self):
        print("The current student's detail is:")
        # Formatting the output using f-string
        # This syntax is available from Python 3.6 onwards)
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_no}")
        print(f"College: {self.college}")


# Creating an object from Student class.
student_1 = Student("Jack", 3)
#printing the details
student_1.get_details()

# Creating another object from Student class.
student_1 = Student("Kate", 4)
#printing the details
student_1.get_details()
