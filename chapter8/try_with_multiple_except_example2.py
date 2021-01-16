print("***The following program can handle the non-system-exiting exceptions.***")
a = input("Enter a valid integer:")
b = input("Enter another valid integer:")
try:
    result = int(a) / int(b)
#except Exception as e:
    #print("An unknown error occurred.")
    #print(f"Error details:{e}")
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details: {e}")
except ValueError as e:
    print("Invalid input! Provide a correct input next time!")
    print(f"Error details: {e}")
except Exception as e:
    print("An unknown error occurred.")
else:
    print(f"Result of the division is : {result}")
print("The program completes successfully.")

