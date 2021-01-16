print("Exercise-8.4")
print("*" * 20)


def test_me():
    flag = True

    while flag:
        user_input = input("Keep entering a valid integer.(Type q to quit):")
        if user_input == 'q':
            break
        try:
            display_me = int(user_input)
            print(f"Correct.You entered:{display_me}")
        except Exception as e:
            print(f"Error:{e}")

    #This statement is placed outside the while loop
    print("End of the exercise.")


test_me()
