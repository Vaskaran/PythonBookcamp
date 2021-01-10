from random import randint

x = randint(10, 12)
#First question with initial data
question1 = "2*3-4"
# Replacing 2 in question1 with x
question1 = question1.replace("2", str(x))

#Second question with initial data
question2 = "1+(2*3)/4"
# Replacing 1 in question2 with x
question2 = question2.replace("1", str(x))

#Third question with initial data
question3 = "5*8%3"
# Replacing 5 in question3 with x
question3 = question3.replace("5", str(x))

# The randint(1,3) function returns a number
# between 1 and 3 (both included)
pick_question = randint(1,3)
if pick_question == 1:
    quiz = question1
elif pick_question == 2:
    quiz = question2
else:
    quiz = question3

print(f"Predict the value of the following expression:{quiz}")
# User's input
user_input = input("Enter your answer:")
# Converting it to float
predicted_value = float(user_input)
actual_value = eval(quiz)
if predicted_value == actual_value:
    print("Correct answer.")
else:
    print("Your answer is wrong.")
    print(f"The correct answer is:{actual_value}")
