import employee_module


#from employee_module import *  # NOT a recommended practice


class Employee:
    """ This employee class stays in the current file."""
    def __init__(self):
        print("Inside  the constructor of the Employee class")


# Creating an object from the Employee class.
#emp_1 = Employee("Jack", 3) #Name collision
emp_1 = employee_module.Employee("Jack", 3)
# Setting background details for emp_1
#emp_1_details = PersonalDetails(
emp_1_details = employee_module.PersonalDetails(
    emp_1.name,
    emp_1.company,
    10.2,
    39,
    "21,Abc Road,USA")
# Printing the details
emp_1.get_details()
emp_1_details.background_details()

emp_2 = Employee()  # Uses current file’s Employee class
