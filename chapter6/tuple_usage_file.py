# A tuple with 5 elements
my_tuple = ("John", 12, "Sam", True, 50.7)
print("The content of my_tuple is:")
print(my_tuple)
#my_tuple.remove(12) #error
#my_tuple.append("Jack") #error
print("----------------")

# Indexing is similar to lists
my_tuple = ("John", 12, "Sam", True, 50.7)
print("The content of my_tuple is:")
print(my_tuple)
# Printing the first element
print("The first element is:")
print(my_tuple[0])
print("The last element is:")
print(my_tuple[-1])
print("Printing the elements from index 1 to index 3.")
print(my_tuple[1:4])
print("Printing the elements from index 2 to end.")
print(my_tuple[2:])
print("----------------")

# You cannot reassign the value inside a tuple.
my_tuple = ("John", 12, "Sam", True, 50.7)
print("The content of my_tuple is:")
print(my_tuple)
print("Trying to replace 'Sam' with 'Bob':")
#my_tuple[2]= 'Bob' #error
print("----------------")

my_list = ["John", 12, "Sam", True, 50.7]
print("The content of my_list is:")
print(my_list)
# Converting the list to a tuple
my_tuple = tuple(my_list)
print("The content of my_tuple is:")
print(my_tuple)

print("----------------")

# Reversing a tuple
my_tuple = (1, 2, 3, 4, 5)
print("The content of my_tuple is:")
print(my_tuple)

print("Reversing the tuple:")
rev_tuple = tuple(reversed(my_tuple))
print("The content of rev_tuple is:")
print(rev_tuple)


