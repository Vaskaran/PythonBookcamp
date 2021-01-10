print("Exercise 6.1")
print("-"*15)
my_list = ["John", 12, 25, 12, "Sam", True, 50.7]
print("The original list is:")
print(my_list)
#Removing the last two elements from the list
del(my_list[-2:])
print("Now the list is:")
print(my_list)

print("-"*15)

print("Exercise 6.2")
print("-"*15)
my_tuple = ("John", 12, 25, 12, "Sam", True, 50.7)
print("The original tuple is:")
print(my_tuple)
#Printing the 3 element
print("The third element:")
print(my_tuple[2])
print("The third element from last:")
print(my_tuple[-3])
print("-"*15)

print("Exercise 6.3")
print("-"*15)
my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)
print("The original tuple is:")
print(my_tuple)

print("The reversed tuple is:")
rev_tuple = tuple(reversed(my_tuple))
print(rev_tuple)

print(f"The number of 4 in this tuple:{rev_tuple.count(4)}")

print("Exercise 6.5")
print("-"*15)
my_tuple = (1, 2, 2, 3, 4, 4, 5)
my_set = set(my_tuple)
print("The my_set is:")
print(my_set)

print("Exercise 6.6")
print("-"*15)
my_list=["red", "blue"]
my_set = set(my_list)
print("The my_set is:")
print(my_set)
my_set.discard("green")

