print(1)  # Prints 1
print(5.7)  # Prints 5.7
print(-6.789)  # Prints -6.789

print("-"*10)

# Performing some basic arithmetic operations
print(1 + 2)  # Prints 3
print(10 - 3)  # Prints 7
print(25 * 3)  # Prints 75
print(12.88 / 4)  # Prints 3.22
# You can perform complex mathematical
# operations too inside the print function
print(1 + 2 * 3)  # Prints 7
print((1 + 2) * 3)  # Prints 9

print("-"*10)
# You can get a closer value
print(10.5 - 2.1)  # prints 8.4
print(10.2 - 3)  # prints 7.199999999999999

print("-"*10)

# Using variables
my_int = 125
print(my_int)  # Prints 125
my_float = 25.763
print(my_float)  # Prints 25.763

# Difference between number and strings
print("1" + "2")  # Prints 12
print(1 + 2)  # Prints 3

my_string1 = "10"
my_string2 = "22"
my_int1 = 10
my_int2 = 22
print(my_string1 + my_string2)  # Prints 1022
print(my_int1 + my_int2)  # Prints 32

print("-"*10)

print("The value inside my_int1 is  :", my_int1)  # This is ok,Prints 10
#print("The value inside my_int1 is  :" + my_int1)  # error
# print(my_int1 + " is my first number") #error

print("The value inside my_int1 is  :" + str(my_int1))  # Ok

print("-"*10)

my_string1 = "12"
# Converting string to an int
print(int(my_string1, 10))  # prints 12

# All strings are NOT convertible to an int
my_string2 = "abc"
# print(int(my_string2, 10))  # Error

my_string1 = "25"
my_string2 = "abc"
print(my_string1.isdigit())  # True
print(my_string2.isdigit())  # False

print("-"*10)

# using f-strings
user_name="John"
print(f"Hello,{user_name}!")

print("-"*10)
# Rounding a number
print(round(2.7))  # Prints 2
print(round(5.32))  # Prints 5

print("-"*10)

# Finding the maximum
print(max(1, 2, 3, 4, 5))  # Prints 5
# Finding the minimum
print(min(1, 2, 3, 4, 5))  # Prints 1
print("-"*10)