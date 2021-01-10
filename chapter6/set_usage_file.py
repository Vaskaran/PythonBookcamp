# Creating a set
my_set = {1, 2, 3, "Jack", "Bob"}
print("The my_set contains:")
print(my_set)
print("----------------")

# Alternative way to create a set
# my_set=set(iterable_element)
# Using a list now to create a set
my_set = set([1, 2, 3, "Jack", "Bob"])
print("The my_set contains:")
print(my_set)
print("----------------")

# Using a tuple to create a set
my_set = set((1, 2, 3, "Jack", "Bob"))
print("The my_set contains:")
print(my_set)
print("----------------")

# A set does not contain duplicates
my_set1 = {1, 2, 3, "Jack", 2, "Bob", 3, 1}
print("The my_set1 contains:")
print(my_set1)

my_set2 = {"Sam", "Bob", "Jack", "Sam", "Jack", "Ester"}
print("The my_set2 contains:")
print(my_set2)
print("----------------")

# Sets are mutable
my_set = {1, 2, 3, 4, 5}
#my_set = {}#it is treated as empty dictionary
#my_set=set()#this is ok for an empty set
print("The my_set contains:")
print(my_set)
print("Adding 6 to the set now.")
my_set.add(6)
print("Now the set is as follows:")
print(my_set)
print("Removing 2 from the set now.")
my_set.remove(2)
print("Now my_set is:")
print(my_set)
print("----------------")

# Strings are iterables.So, you can use strings to set().
my_str = "vaskaran"
my_set = set(my_str)
print("The my_set contains:")
print(my_set)

print("----------------")
# Sets are unordered.You cannot access the elements by referring an index
my_set = set([2,"abc",1,5])
print("The my_set contains:")
print(my_set)
print("Trying to access the 0th element.")
#print(my_set[0])#error

# You cannot access set elements by referring an index.
# But You can loop through the elements.
my_set = set([2,"abc",1,5])
print("The my_set contains:")
for item in my_set:
    print(item)

print("----------------")
# Remove an element from a set
my_set = set([1,2,3,4,5])
print("The my_set contains:")
print(my_set)
print("Removing 5 using remove().")
my_set.remove(5)
print("Now the my_set contains:")
print(my_set)
print("Removing 4 now using discard().")
my_set.discard(4)
print("Now the my_set contains:")
print(my_set)

# Trying to remove 4 when it is absent in the set.
#my_set.discard(4) # no error is raised
#my_set.remove(4)  # error is raised
print("----------------")

