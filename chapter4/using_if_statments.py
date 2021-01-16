# Demo1
a = 11
print("Demo1")
if a > 10:
    print("The current value inside a is greater than 10.")
# Demo2
print("Demo2")
a = 5
if a > 10:
    print("The current value inside a is greater than 10.")
else:
    print("The current value of a is less than or equal to 10.")

# Demo3
print("Demo3")
a = 5
if a == 5:
    print("a is equal to 5.")
else:
    print("a is NOT equal to 5.")

# Demo4
print("Demo4")
a = 25
if a != 7:
    print("a is NOT equal to 7.")
else:
    print("a is equal to 7.")

# Demo5
print("Demo5")
user_input = input("Enter a valid number only:")
# Skipping the validation of user's input
a = float(user_input)
if a > 10:
    print("The number is greater than 10.")
elif a == 10:
    print("The number is equal to 10.")
else:
    print("The number is less than 10.")

# Demo6
print("Demo6")
user_input = input("Enter your age:")
# Skipping the validation of user's input
age = float(user_input)
if age < 10:
    print("Hi Dear.You can use the product for free.")
elif age>= 10 and age <20:
    print("Please donate 1$ for the product.")
elif age >= 20 and age < 30:
    print("Please donate 2$ for the product.")
elif age >= 30 and age < 40:
    print("Please donate 3$ for the product.")
else:
    print("Please donate 4$ for the product.")

# Demo6.1-Improvement to demo6
print("Demo6.1")
user_input = input("Enter your age :")
# For simplicity, skipping the validation of user's input
age = float(user_input)
if age < 10:
    print("Hi Dear.You can use the product for free.")
    #I’m simplifying the expression
elif 10 <= age < 20:
    print("Please donate 1$ for the product.")
    #Using brackets for better readability
elif (age >= 20) and (age < 30):
    print("Please donate 2$ for the product.")
    # Using brackets for better readability
elif (age >= 30) and (age < 40):
    print("Please donate 3$ for the product.")
else:
    print("Please donate 4$ for the product.")
