print("***Using a break statement inside a while loop.***" )
current_value = 1
print(f"Initially, current_value={current_value}")
print("I exit loop when current_value becomes 3.")
while current_value < 5:
    # incrementing the value
    current_value += 1
    print(f"The current value={current_value}")
    if current_value == 3:
        break
    print("I'm still inside the while loop.")
# This statement is placed outside the while loop
print("Job done.I've exited from the while loop.")
