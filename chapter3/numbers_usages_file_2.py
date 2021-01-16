# importing math functions
from math import *;

# Printing the square root of 25
print(f"Square root of 25 is :{sqrt(25)}")  # 5.0
# Printing the square root of 6.25
print(f"Square root of 6.25 is :{sqrt(6.25)}")  # 2.5

print("-" * 10)

# Printing the ceiling value
# This is the smallest integer less than the number
# you defined.

print(f"The ceiling value of 39.3 is :{ceil(39.3)}")  # 40
# Printing the floor value
# This is the biggest integer NOT greater than the number
# you defined.
print(f"The floor value of 39.3 is : {floor(39.3)}")  # 39

print("-" * 10)

# Finding the gcd of 4 and 14
print(f"The gcd of 4 and 14 is : {gcd(4,14)}")  # prints 2
# Finding the gcd of 14 and 63
print(f"The gcd of 63 and 14 is : {gcd(63,14)}")  # prints 7

print("-" * 10)

# Finding the factorial of 5
print(f"The factorial of 5 is : {factorial(5)}")  # prints 120
# Finding the factorial of 7
print(f"The factorial of 7 is : {factorial(7)}")  # prints 5040

print("-" * 10)


#Supply a name
user_name = input("Enter your name:")
#Enter the age
user_age = input("Enter your age:")
# Printing using commas
print("Hello,", user_name, "! you are now ", user_age)
# Printing using string concatenation
print("Hello," + user_name + "! you are now " + str(user_age))
# Printing using f-strings
print(f"Hello,{user_name}! you are now {user_age}")


