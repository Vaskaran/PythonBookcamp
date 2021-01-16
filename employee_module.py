# This is an Employee class where you can
# find the name, employee id, and company details.
# It is used in chapter11.

"""

Classes
---------
Employee
    This is a simple class. In the constructor,
    you can store employee name, employee id and
    company information. It has a method, called
    get_details() to print these information.

PersonalDetails
    This class has a method to show
    an employee with background details.
"""


class Employee:
    """
    It is a simple class to store
    basic employee information.
    """
    def __init__(self, name, emp_id):
        # Initialize name
        self.name = name
        # Initialize emp_id
        self.emp_id = emp_id
        self.company = "Abc Ltd."

    def get_details(self):
        print("\nThe current employee details are:")
        # Formatting the output using f-string
        print(f"Name: {self.name}")
        print(f"Id: {self.emp_id}")
        print(f"Company: {self.company}")

    def get_details_modified(self):
        """
        Modifying this method with return
        value for testing in Chapter-12
        """
        #print("The current employee details are as follows:")
        #Formating the output using f-string
        #print(f"Name:{self.name},Id:{self.emp_id},Company:{self.company}")
        return f"Name:{self.name},Id:{self.emp_id},Company:{self.company}"


class PersonalDetails:
    """
    This class is used to show the
    background details of an employee.
    """
    def __init__(self, name, current_company,
                 work_experience, age, address):
        # Initialize department
        self.name = name
        self.current_company = current_company
        self.work_experience = work_experience
        # Initialize age
        self.age = age
        self.address = address

    def background_details(self):
        print("-" * 10)
        print("Here are the background details:")
        #Formating the output using f-string
        print(f"Name: {self.name}")
        print(f"Current company: {self.current_company}")
        print(f"Age: {self.age},Address: {self.address}")
        print(f"Experience: {self.work_experience} yrs.")
        print("-" * 10)

