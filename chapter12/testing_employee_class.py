import unittest
from employee_module import Employee


class TestEmployee(unittest.TestCase):
    """ Tests for Employee class in employee_module """

    def test_employee_creation(self):
        """ Can we store the Employee details correctly? """
        emp_john = Employee('John', 'E001')
        self.assertEqual(emp_john.name, 'John', 'Employee name does not match.')
        self.assertEqual(emp_john.emp_id, 'E001', 'Employee ID does not match.')
        self.assertEqual(emp_john.company, 'Abc Ltd.', 'The company information is not found.')


if __name__ == '__main__':
    unittest.main()
