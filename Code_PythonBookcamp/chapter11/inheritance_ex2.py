class Employee:
    """Employee class is the parent class."""

    def __init__(self, name, emp_id):
        # Initialize name
        self.name = name
        # Initialize emp_id
        self.emp_id = emp_id
        self.company = "Abc Ltd."


class Developer(Employee):
    """Developer class inherits from Employee"""

    def __init__(self, name, emp_id):
        """ Initialize starts from parent class."""
        super().__init__(name, emp_id)
        # Employee.__init__(self, name, emp_id) #Also works
        # This is a class specific attribute
        self.designation = "Developer"

    def developer_details(self):
        """Prints the developer details."""
        print(f"Name:{self.name}")
        print(f"Id={self.emp_id}")
        print(f"Designation={self.designation}")
        print("-" * 10)


# Creating an instance of the Developer class
john = Developer("John S", "E001")
john.developer_details()
kate = Developer("Kate W", "E002")
kate.developer_details()
