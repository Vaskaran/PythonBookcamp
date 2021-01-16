print("Example of a global variable.")
x = 10
print(f"x={x}")


def print_me():
    global x
    x += 2
    print(f"Now x={x}")


print_me()
print(f"Here x={x}")
print("-" * 30)
