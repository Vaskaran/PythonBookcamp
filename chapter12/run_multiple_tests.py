import unittest
import my_library_functions as ml  # importing everything from the module


class LibraryFunctionsTestCases(unittest.TestCase):
    """ Tests for my_library_functions """

    def test_make_total_double(self):
        """ Can we make the average of
        the numbers 25,75.3 """
        resultant_value = ml.make_total_double(25,75.2)
        self.assertEqual(200.4,resultant_value)  #test passes

    def test_make_average_two_numbers(self):
        """ Can we make the the average of the
        numbers 25,75.8,and 0(optional)?"""
        resultant_value = ml.make_average(25,75.8)
        self.assertEqual(33.6,resultant_value)  # test passes
        #self.assertEqual(40, resultant_value) # test fails

    def test_make_average_three_numbers(self):
        """ Can we make the average of the
        numbers 10,20.9 and 30 ?"""
        resultant_value = ml.make_average(10,20.9,30)
        self.assertEqual(20.3,resultant_value)


if __name__ == '__main__':
    unittest.main()
