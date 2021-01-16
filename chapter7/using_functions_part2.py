print("***Demo2***")


#Using default values in a function
def print_details(name="Sam",age=35):
    """
    This function takes two parameters.
    You can supply the name and age of the user
    in this function.
    By default, the name is 'Sam' and the age is 35.
    """
    print(f"Hello {name}! How are you?")
    print(f"You are now {age}.")


print_details()  #Will take both the default values
print_details(name="Jack")  #Will take age=35 as default
print_details(age=45)  #Will take name="Sam" as default
#None of the default values are considered
print_details("Bob",20)

print("\n***Demo3***")


def calculate_sum(x,y):
    return x + y


total = calculate_sum(12,15)
print(f"The sum of 12 and 15 is:{total}")

total = calculate_sum(20.5,37)
print(f"The sum of 20.5 and 37 is:{total}")

total = calculate_sum('10','20')  #1020
print(f"The sum of '10'' and '20' is:{total}")

print("\n***Demo4***")
#Demonstration-4
initial_list = [1,2,3,4,5]
double_list = []


def make_double(input_list):
    """
    It is function that can return multiple values.
    Each element in the list will be doubled
    by this function.
    """
    for element in input_list:
        double_list.append(2 * element)


print("The initial_list is :")
print(initial_list)
print("Calling the function make_double() now.")
make_double(initial_list)
print("The double_list is :")
print(double_list)
print("The initial_list at present :")
print(initial_list)  #unchanged initial list

print("***Demo5***")
initial_list = [10, 20, 30, 40, 50]
double_list = []


def make_double(input_list):
    """
    It is function that can return multiple values.
    Each element in the list will be doubled
    by this function.
    """
    while input_list:
        element = initial_list.pop()
        #print(element)
        double_list.append(2 * element)


print("The initial_list is:")
print(initial_list)
print("Calling the function make_double() now.")
make_double(initial_list)
print("The double_list is:")
print(double_list)
print("The initial_list at present :")
print(initial_list)
