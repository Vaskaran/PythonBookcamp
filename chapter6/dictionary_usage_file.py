# A dictionary with with 5 key-value pair
my_dictionary = {1: "John", 2: 12, 3: "Sam", 4: True, 5: 50.7}
print("The my_dictionary contains:")
print(my_dictionary)
print("----------------")

# A dictionary with 5 key-value pair
# Choosing different types of keys in the same dictionary
my_dictionary = {1: "John", 2: 12, 3: "Sam", 'fourth': True, 'fifth': 50.7}
print("The my_dictionary contains:")
print(my_dictionary)
print("----------------")

# I want to print values for particular keys
my_dictionary = {1: "John", 2: 12, 3: "Sam", 'fourth': True, 'fifth': 50.7}
print("The my_dictionary contains:")
print(my_dictionary)
print("Value at key 1:", my_dictionary[1])
print("Value at key 2:", my_dictionary[2])
print("Value at key 3:", my_dictionary[3])
print("Value at key 'fourth':", my_dictionary['fourth'])
print("Value at key 'fifth'::", my_dictionary['fifth'])
print("----------------")

# If you assign different values for the same keys
# last assigned value will be kept
my_dictionary = {1: "John", 2: "Sam", 3: "Jack",1: "Bob"}
print("The my_dictionary contains:")
print(my_dictionary)
print("Value at key 1:", my_dictionary[1])
print(f"Number of contents:{len(my_dictionary)}")
print("----------------")
