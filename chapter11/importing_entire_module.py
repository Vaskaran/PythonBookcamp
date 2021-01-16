import employee_module

# Creating an object from the Employee class.
emp_1 = employee_module.Employee("Jack", 3)
# Setting background details for emp_1
emp_1_details= employee_module.PersonalDetails(
    emp_1.name,
    emp_1.company,
    10.2,
    39,
    "21,Abc Road,USA")
# Printing the details
emp_1.get_details()
emp_1_details.background_details()
