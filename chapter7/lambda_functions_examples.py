print("***Demo6***")
print("***Lambda function example-1.***")
say_hello = lambda: print("Hello, Reader!")
say_hello()

print("***Lambda function example-2.***")
make_double = lambda x:x * 2
print(f"Double of 10 is:{make_double(10)}")
print(f"Double of 25.35 is:{make_double(25.35)}")

print("\n***Demo7***")
original_list = [1, 2, 3, 4, 5]
# Adds 2 to each item in the list
new_list = list(map(lambda x: x + 2, original_list))
print("The original list is as follows:")
print(original_list)
print("The updated list is as follows:")
print(new_list)

