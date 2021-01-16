print("=" * 25)
print("This is a simple calculator.")
print("It supports the following operations:")
print("i)Addition"
      "\nii)Subtraction"
      "\niii)Multiplication and "
      "\niv)Division.")
print("=" * 25)
valid_operators = ["+", "-", "*", "/"]


def add_numbers(num1, num2):
    """
    Adds the numbers.
    """
    return num1 + num2


def subtract_numbers(num1, num2):
    """
    Subtracts the numbers.
    """
    return num1 - num2


def multiply_numbers(num1, num2):
    """
    Multiplies the numbers.
    """
    return num1 * num2


def divide_numbers(num1, num2):
    """
    Divide num1 by num2.
    """
    return num1 / num2


def compute(num1, operator, num2):
    """
    This function computes the final result.
    """
    result = 0  #default value

    if operator == '+':
        result = add_numbers(num1,num2)
    elif operator == '-':
        result = subtract_numbers(num1,num2)
    elif operator == '*':
        result = multiply_numbers(num1,num2)
    else:
        result = divide_numbers(num1, num2)
    print(f"The final result is:{result}")


def main():
    """
    This is the top-level function.
    It calls the compute() function.
    """
    usr_input1 = input("Enter the first number:")
    first_number = float(usr_input1)
    usr_input2 = input("Enter the next number:")
    second_number = float(usr_input2)
    usr_opr = input("Enter an operator(+,-,*,/): ")
    if usr_opr in valid_operators:
        compute(first_number, usr_opr, second_number)
    else:
        print("Invalid operator. Cannot compute the result.")


main()
