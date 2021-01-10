print("Demo5b-Not recommended.")
user_input = input("Enter a valid numbers only:")
# For simplicity, skipping the validation of user's input
a = float(user_input)
if a < 0:
    print("The number is less than 0.")
else:
    if a < 1:
        print("The number is greater than 0 but less than 1.")
    else:
        if a == 1:
            print("The number is equal to 1.")
        else:
            if a == 2:
                print("The number is equal to 2.")
            else:
                if a == 3:
                    print("The number is equal to 3.")
                else:
                    print("The number is greater than 3.")
