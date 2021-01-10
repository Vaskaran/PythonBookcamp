#Function example-1
print("***Function example-1.***")


def print_hello():
    print("Hello")


print_hello()

#Function example-2
print("\n***Function example-2.***")


def print_details(name, age):
    """
    This function takes two parameters.
    You can supply the name and age of the user
    in this function.
    """
    print(f"Hello {name}!How are you?")
    print(f"You are now {age}.")


print_details("Bob", 20)
#You can repeat function calls.
print_details("Bob", 20)
# You can vary the arguments of the functions
print_details("Sam", 35)

#The following will print the function documentation
#print(print_details.__doc__)

#Use of positional arguments are important
#print_details("Bob",20) #Ok,expected outcome
print_details(20, "Bob")  # Unexpected outcome

#Use of keyword arguments
print("\n**Using Keyword arguments.**")  # Expected outcome
print_details(age=20, name="Bob")  # Expected outcome
print_details(name="Bob", age=20)  # Again expected outcome
