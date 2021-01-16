import unittest
from my_library_functions import make_total_double


class LibraryFunctionsTestCases(unittest.TestCase):
    """ Tests for my_library_functions """

    def test_make_total_double(self):
        """ Can we make the total double for the numbers 25,75.3 """
        resultant_value = make_total_double(25, 75.3)
        self.assertEqual(200.6, resultant_value) #test passes
        #self.assertEqual(200.6+1,resultant_value) #test fails
        #self.assertEqual(200.6+1, resultant_value,"The actual value and expected value does not match")  #test fails
        #self.assertEqual(200.6, resultant_value, "The actual value and expected value does not match")  #test passes


if __name__ == '__main__':
    unittest.main()
