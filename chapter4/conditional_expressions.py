a = input("Enter a valid integer for the dividend:")
b = input("Enter a valid integer for the divisor:")
# Skipping the input validation...
dividend = int(a)
divisor = int(b)

if divisor != 0:
    result = dividend / divisor
    print(f"Division successful.The result is:{result}")
else:
    print("You cannot proceed when the divisor is 0.")

# Alternative version
result = 0  # some initial value
result = dividend / divisor if divisor != 0 else print("You cannot set the divisor to 0.")
print(f"The result is:{result}")

b = 0
#Example:inline -if
a = 5 if b != 0 else 1
print(a)
