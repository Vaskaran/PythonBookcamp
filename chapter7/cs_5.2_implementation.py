# All questions
question1 = "Q1.What is the value of the expression:2*3-4?" \
            "\n(a)1" \
            "\n(b)2" \
            "\n(c)3" \
            "\n(d)None."
question2 = "\nQ2.What is the value of the expression:1+(2*3)/4?" \
            "\n(a)1.5" \
            "\n(b)3" \
            "\n(c)3.5" \
            "\n(d)None."
question3 = "\nQ3.The set data type can hold duplicate values." \
            "The statement is:" \
            "\n(a)False" \
            "\n(b)True" \
            "\n(c)Partially correct." \
            "\n(d)None."

# Storing the questions with answer keys
# inside the following dictionary.
question_bank = {question1: "b",
                 question2: "c",
                 question3: "a"}


def run_test(questions):
    """
        This function takes the question bank as a parameter.
        You can supply the question bank with answer keys
        in this function.
        """
    print("Welcome to the MCQ test.")
    print("=" * 25)
    score = 0  # initial value
    for key in questions:
        print(key)
        user_input = input("Type your answer(a/b/c/d):")
        if user_input == question_bank[key]:
            score += 1
    print(f"\nYour Score:{score} out of {len(questions)}")


run_test(question_bank)
