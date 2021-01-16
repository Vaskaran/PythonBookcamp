# A list with three strings
my_list1 = ["John","Bob","Sam"]
print("The my_list1 is as follows:")
print(my_list1)

# A list with five numbers
my_list2 = [1,2,3.7,4,5.2]
print("The my_list2 is as follows:")
print(my_list2)

print("----------------")

# A list can store mixed data types
my_list = ["John",12,"Sam",True,50.7]
print(my_list)
print("----------------")

# You can use list index.The usage is similar to strings.
my_list = ["John",12,"Sam",True,50.7]
print(my_list[0])  # John
print(my_list[1])  # 12
print(my_list[2])  # Sam
print(my_list[3])  # True
print(my_list[4])  # 50.7
# Error: List index out of range
# print(my_list[5])
print("----------------")

# You can use list indexing from the right end.
# In this case, it starts from -1
my_list = ["John",12,"Sam",True,50.7]
print(my_list[-1])  # 50.7
print(my_list[-2])  # True
print(my_list[-3])  # Sam
print(my_list[-4])  # 12
print(my_list[-5])  # John
# Error: List index out of range
# print(my_list[-6])
print("----------------")

# Printing list elements starting from a particular position
my_list = ["John",12,"Sam",True,50.7]
print("The original list is as follows:")
print(my_list)
print("Printing the elements starting from index position 2 to end:")
print(my_list[2:])
print("Printing the elements starting from index position 1 to 3(i.e.4-1):")
print(my_list[1:4])
print("----------------")

# You can reassign a new value inside the list
my_list = ["John",12,"Sam",True,50.7]
print("The original list is as follows:")
print(my_list)
print("Changing the element at index 2.")
my_list[2] = "Bob"
print("Now the list is as follows:")
print(my_list)
print("----------------")

# Concatenation example
my_list1 = ["John",12,50.7]
my_list2 = ["Sam",25,"John",False,100.2]
print("Original lists are :")
print(my_list1)
print(my_list2)
print("After concatenating the lists, you get the following list:")
print(my_list1 + my_list2)
print("----------------")

# Printing specific number of elements of a list from end.
my_list = ["John",12,"Sam",True,50.7]
print("The original list is:")
print(my_list)
print("The last 3 elements of the list are:")
print(my_list[-3:])
print("The last 2 elements of the list are:")
print(my_list[-2:])
print("The last element of the list is:")
print(my_list[-1])
print("----------------")

# Removing an element using del()
my_list = ["John", 12, "Sam", True, 50.7]
print("The original list is:")
print(my_list)
print("Removing the element at index 2.")
del (my_list[2])
print("Now the list is:")
print(my_list)
print("Removing the element at index 3 from this updated list.")
del (my_list[3])
print("The updated list is:")
print(my_list)
print("----------------")

# Removing an element using remove() function
my_list = ["John", 12, 25, 12, "Sam", True, 50.7]
print("The original list is:")
print(my_list)
print("Removing the first occurrence of 12 inside the list.")
my_list.remove(12)
print("Now the list is:")
print(my_list)
print("----------------")

# Elements are case-sensitive
my_list = ["John", 12, "sam", 25.7, "Sam", True]
print("The original list is:")
print(my_list)
print("Removing the first occurrence of 'Sam' inside the list.")
my_list.remove('Sam')
print("Now the list is:")
print(my_list)
print("----------------")

# Removing an element using pop()
my_list = ["John", 12, 25, 12, "Sam", True, 50.7]
print("The original list is:")
print(my_list)
print("Removing an element inside the list at index 3 using pop().")
my_list.pop(3)
print("Now the list is:")
print(my_list)
print("----------------")

# Checking whether an element is present inside a list
my_list = ["John", "Bob", "Sam", "Ester", 1, 2, 3, 4]
print("Is 'Sam' present inside the list?")
print('Sam' in my_list)  # True
print("Is 'Jeniffer' present inside the list?")
print('Jennifer' in my_list)  # False
print("Is 3 present inside the list?")
print(3 in my_list)  # True
print("Is 5 present inside the list?")
print(5 in my_list)  # False

# Checking whether an element is absent inside a list
print("Is 'Jeniffer' NOT present inside the list?")
print('Jennifer' not in my_list)  # True

