import unittest
from employee_module import Employee


class TestEmployeeMethod(unittest.TestCase):
    def test_get_details_modified(self):
        """ Does the get_details() work correctly? """
        emp_kate = Employee('Kate', 'E002')
        self.assertTrue('Kate' in emp_kate.get_details_modified(), 'The employee name is not found.')
        self.assertTrue('E002' in emp_kate.get_details_modified(), 'The employee id is not found.')
        self.assertTrue('Abc Ltd.' in emp_kate.get_details_modified(), 'The company information is not found.')


if __name__ == '__main__':
    unittest.main()
