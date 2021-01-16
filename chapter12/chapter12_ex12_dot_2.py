import unittest
from math import sqrt, floor, gcd


class TestEmployeeMethod(unittest.TestCase):
    def test_inbuilt_functions(self):
        """ Do the methods sqrt(),floor(), and gcd() correctly? """
        self.assertEqual(5.0, sqrt(25), 'The sqrt(25) does not give the expected result.')
        self.assertEqual(100, floor(100.2), 'The floor(100.2) does not give the expected result.')
        self.assertEqual(2, gcd(4, 10), 'The gcd(4,10) does not give the expected result.')


if __name__ == '__main__':
    unittest.main()
