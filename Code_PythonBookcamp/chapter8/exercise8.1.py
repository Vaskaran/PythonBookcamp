# Exercise 8.1
try:
    result = 15/0
except ArithmeticError:
    print("Caught the ArithmeticError.Your divisor is zero.")
except ZeroDivisionError:
    print("Caught ZeroDivisionError.Correct the divisor which is zero at present.")


