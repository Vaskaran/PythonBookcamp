#Exercise-4.1
a = 5
if a > 10:
    print("The number is greater than 10.")
elif a == 10:
    print("The number is equal to 10.")
print("--------End of Exercise 4.1----------------")

#Exercise-4.2
a = 5
#if a < 7 and a > 9:  # Wrong logic.This condition cannot be satisfied.
if a < 7 or a > 9:  # ok.
    print("The if condition is satisfied.")
else:
    print("The if condition will never be satisfied.")
print("--------End of Exercise 4.2----------------")

#Exercise-4.3
number = 0
#number = -34
if number:
    print(f"The if condition is satisfied.number={number}")
else:
    print(f"The if condition is not satisfied.number={number}")

print("--------End of Exercise 4.3----------------")
