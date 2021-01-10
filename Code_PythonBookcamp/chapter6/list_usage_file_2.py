
# Finding the maximum and minimum from a list
# This list contains the numbers only
my_list = [1, 23, 56.2, -3.7, 999]
print("The original list is:")
print(my_list)
print(f"Largest number is :{max(my_list)}")  # 999
print(f"Smallest number is :{min(my_list)}")  # -3.7
print("----------------")


#For this segment, you'll receive error
#my_list = [1, 23, 56.2, -3.7, 999, "abc", "bob"]
#print("The original list is : ")
#print(my_list)
#print(f"Largest number is :{max(my_list)}")
#print(f"Smallest number is :{min(my_list)}")


# Testing booleans with max() and min()
my_list = [0.75, True, False, 0.5, 0.6, 1, 0]
print("The original list is :")
print(my_list)
print(f"Largest number is :{max(my_list)}")  # True
print(f"Smallest number is :{min(my_list)}")  # False
print("----------------")


# have interchanged the positions of True and 1 in this list.
#Also, at the same time, I have interchanged the position of False and 0 here)

# Testing booleans with max() and min()
my_list = [0.75, 1, 0, 0.5, 0.6, True, False]
print("The original list is as follows")
print(my_list)
print(f"Largest number is :{max(my_list)}")  # 1
print(f"Smallest number is :{min(my_list)}")  # 0
print("----------------")

# I want to add an element at the end of a list
my_list = ["John", 12, "Sam", True, 50.7]
print("The original list is:")
print(my_list)
print("Appending the element 25 at the end of list.")
my_list.append(25)
print("Now the list is :")
print(my_list)
print("Appending another element 'Bob' now.")
my_list.append("Bob")
print("The modified list:")
print(my_list)
#Using append(), at a time, you can add one element only.
#my_list.append(10,20) #error

print("----------------")
'''
You have just that using append(), you can add a single element only.
But this function allows you to add a list that contains multiple elements.
Let’s see how it looks after this addition.
'''

my_list = ["John", 12, "Sam", True, 50.7]
print("The initial list is:")
print(my_list)
print("Appending the list [10,'Bob',100.2] at the end of list:")
my_list.append([10, 'Bob', 100.2])
print("The modified list is :")
print(my_list)
print("----------------")

# You can add multiple elements in a list
# using extend() function.
# Here is an example.
my_list = ["John", 12, "Sam", True, 50.7]
print("The original list is as follows")
print(my_list)
print("Adding 10,'Bob', and 100.2 at the list end.")
my_list.extend([10, 'Bob', 100.2])
print("Now the list is as follows:")
print(my_list)
print("----------------")

#Till now, you saw that I’m adding the elements at the end of a list.
#But you have the option to add an element in a particular position.
my_list = ["John", 12, "Sam", True, 50.7]
print("The original list is:")
print(my_list)
print("Adding the element 'Jack' at index 3.")
my_list.insert(3, "Jack")
print("Now the list is as follows:")
print(my_list)
print("----------------")


#Using sort()
my_list = [33, 11, 555, 77, 111, 333]
print("The initial list is:")
print(my_list)
print("Using sort() on my_list now.")
my_list.sort()
print("Now the list is:")
print(my_list)
print("----------------")

#Using sorted()
my_list = [33, 11, 555, 77, 111, 333]
print("Initially, my_list is:")
print(my_list)
print("Printing the sorted list now.")
print(sorted(my_list))
print("The my_list now:")
print(my_list)
print("----------------")
