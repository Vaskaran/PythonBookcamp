from random import randint

picked_number = randint(1, 15)
print("The computer has picked a random number for you.")
print("Clue: It is between 1 and 15 (both inclusive).")
print("Can you guess it within 3 attempts? Make a try.")
no_of_attempt = 0
guess = False
user_input = 0  # an initial value
while no_of_attempt < 3:
    #User's input
    user_input = int(input("Enter your answer:"))
    no_of_attempt += 1
    if user_input == picked_number:
        guess = True
        break
    elif user_input > picked_number:
        print("It is high. Try again!")
    else:
        print("It is low. Try again!")
if guess:
    print("Excellent. You have guessed it right.")
    print(f"you've taken {no_of_attempt} attempt(s).")
else:
    print(f"The computer picked the number:{picked_number}.")
    print("You have lost the game now!")
