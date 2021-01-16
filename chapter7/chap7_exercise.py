print("Exercise-7.1")


def print_x(x):
    print(x)


def print_y(y):
    print(y)


def main():
    print_x(10)
    print_y(20)


main()
print("-" * 30)

print("Exercise-7.2")


def print_me(x):
    x += 2
    print(x)


def print_me(x):
    x += 3
    print(x)


print_me(5)
print("-" * 30)

print("Exercise-7.3")


def print_me(x):
    x += 2
    print(x)


def print_me(y):
    y += 3
    print(y)


print_me(5)
print("-" * 30)

print("Exercise-7.4")

x = 10
print(f"x={x}")


def print_me(x):
    x += 2
    print(f"Now x={x}")


print_me(x)
print(f"Here x={x}")
print("-" * 30)

print("Exercise-7.5")


def print_me(x):
    print(x)


def print_me(x, y):
    print(x)
    print(y)


#print_me(5)  # error now
print_me(5,7)  # ok
print("-" * 30)

print("Exercise-7.6")
original_list = [100, 200, 300, 400, 500]
# Adds 2 to each item in the list
new_list = list(map(lambda x: x * 1.05, original_list))
print("The original list is as follows:")
print(original_list)
print("The updated list is as follows:")
print(new_list)
