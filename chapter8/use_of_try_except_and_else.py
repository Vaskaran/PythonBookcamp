print("The following program can handle the ZeroDivisionError and ValueError both.")
a = input("Enter a valid integer:")
b = input("Enter another valid integer:")
try:
    result = int(a) / int(b)
    #print(f"Result of the division is : {result}")
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details: {e}")
except ValueError as e:
    print("Invalid input! Provide correct input next time!")
    print(f"Error details:{e}")
else:
    print(f"The result of the division is: {result}")
print("The program completes successfully.")
