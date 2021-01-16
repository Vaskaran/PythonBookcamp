my_list = [1, 2, 3, 4]
#If condition is False, AssertionError is raised.
# assert len(my_list) >= 5, "List length is less than 5."

try:
    assert len(my_list) >= 5, "List length is less than 5."
except AssertionError as e:
    print(f"Error details:{e}")

