print("***Using a continue statement inside a while loop.***")
current_value = 1
print(f"Initially, current_value={current_value}")
print("I skip the code when current_value becomes 3.")
while current_value < 5:
    # incrementing the value
    current_value += 1
    print(f"The current value={current_value}")
    if current_value == 3:
        continue
    print("I'm still inside the while loop.")
# This statement is placed outside the while loop
print("Job has been done. Exit from the while loop.")

