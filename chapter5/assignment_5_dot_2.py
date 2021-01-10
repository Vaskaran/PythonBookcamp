# Solution to Assignment 5.2
# A list of numbers
number_list = [1, 2.2, 4.4, 5, 6, 9.3, 102]
print("Printing the numbers inside number_list using a 'for' loop:")
for number in number_list:
    print(number)

print("Now printing the numbers which has the index between 2 and 5:")
for index in range(2, 6):
    print(number_list[index])