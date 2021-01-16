# Supply a name
user_name = input("Enter your name:")
# Enter the age
user_age = input("Enter your age:")
# Using commas
print("Welcome,", user_name, "! you are now ", user_age)
# Using f-strings(Python 3.6 onwards)
print(f"Welcome,{user_name}! you are now {user_age}")
# Printing using string concatenation
print("Welcome," + user_name + "! you are now " + str(user_age))

#user_name="John"
#print(f"Hello, {user_name}!")