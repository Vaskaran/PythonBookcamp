from employee_module import Employee, PersonalDetails

# Creating an object from Employee class.
emp_1 = Employee("Jack", 3)
# Setting background details for emp_1
emp_1_details = PersonalDetails(emp_1.name,
                                emp_1.company,
                                10.2,
                                39,
                                "21,Abc Road,USA")
# Printing the details
emp_1.get_details()
emp_1_details.background_details()
