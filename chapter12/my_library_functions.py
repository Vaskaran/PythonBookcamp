# I write test cases to verify the following functions.

""" Support to use custom functions.

Functions
---------
make_total_double()
    This function takes two numbers and returns the double.

make_total_double()
    This function takes three numbers and returns the average.
    The third number is optional.

"""


def make_total_double(first,second):
    """
    This function takes two numbers and returns the double.
    """
    total = first + second
    return total * 2


def make_average(first,second,third=0):
    """
    This function takes three numbers and returns the average.
    The third number is optional.
    """
    total = first + second + third
    return total / 3
