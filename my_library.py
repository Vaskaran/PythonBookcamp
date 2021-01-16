# A simple list
my_list = [1, 2, 3, 4, 5]

# A simple dictionary
my_dictionary = {1: "Jack", 2: "Kate", 3: "Bob"}


def make_total_double(first, second):
    """
    This function takes two numbers
    and returns the double.
    """
    total = first + second
    return total * 2


def make_average(first, second, third=0):
    """
    This function takes three numbers and
    returns the average.
    The third number is optional.
    """
    total = first + second + third
    return total / 3
