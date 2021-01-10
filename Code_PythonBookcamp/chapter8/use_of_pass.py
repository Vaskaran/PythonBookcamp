print("This program prints the sum of two valid integers.")
first_input = input("Enter a valid integer:")
second_input = input("Enter another valid integer:")
total = 0  #default value
try:
    a = int(first_input)
    b = int(second_input)
except ValueError as e:
    # print("Provide a correct input next time!")
    pass
else:
    total = a + b
    print(f"Sum of numbers :{total}")

print("The program completes successfully.")
