import os


class ScoreExceedsError(Exception):
    """ This is a custom exception."""
    pass


def calculate_grade(a1_score,
                    a2_score,
                    e_score):
    """
    This function calculates the final score.
    Here is the consideration:
    25% of the total marks in assignment and
    75% of the total marks make the grade card.
    """
    final_score = (a1_score + a2_score) * .25\
                  + e_score * .75
    return final_score


def make_grade(score):
    """ This function makes the grade."""
    grade = ""
    if score > 90:
        grade = "A+(Outstanding)"
    elif score > 80:
        grade = "A(Very Good)"
    elif score >= 70:
        grade = "B(Good)"
    else:
        grade = "F(Fail)"
    return grade


def save_scores(name,
                assign1,
                assign2,
                exam,
                score,
                grade):
    """
    This function stores the result in a text file.
    It picks the current working directory.Then create a
    directory(if it does not exist),called GradeScores.
    All records are stored as test files inside
    this directory.
    """
    try:
        # Retrieve the current working directory
        current_path = os.getcwd()
        print("The current working directory:")
        print(current_path)
        # Adding a relative path to the current path
        relative_path = "GradeScores"
        new_path = os.path.join(current_path,
                                relative_path)
        # Making the directory if it does not exist
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        new_path = new_path + '\\' + name + '.txt'
        print("Get the report card at:")
        print(new_path)
        with open(new_path,'w') as file_object:
            file_object.write("***Report Card***")
            file_object.write("\n***Course name: Python for Beginners***\n")
            file_object.write("=" * 50)
            file_object.write(f"\nStudent Name: {name}")
            file_object.write(f"\nAssignment-1 Score:{assign1}")
            file_object.write(f"\nAssignment-2 Score:{assign2}")
            file_object.write(f"\nExam Score:{exam}")
            file_object.write(f"\nFinal score:{score}")
            file_object.write(f"\nGrade/Remark: {grade}")
    except FileNotFoundError as e:
        print(f"The file is missing.Details:{e}")
    except Exception as e:
        print(f"Error details: {e}")


def main():
    """
    It is the top level function for
    this application.
    """

    try:
        student_name = input("Enter the student name:")
        assign1 = float(input("Assignment-1 score:"))
        if assign1 > 50:
            raise ScoreExceedsError("Assignment1 score cannot be greater than 50.")
        assign2 = float(input("Assignment-2 score:"))
        if assign2 > 50:
            raise ScoreExceedsError("Assignment2 score cannot be greater than 50.")
        exam = float(input("Exam score:"))
        if exam > 100:
            raise ScoreExceedsError("Final exam score cannot be greater than 100.")
    except ValueError as e:
        print(f"Invalid input.Details:{e}")
    except ScoreExceedsError as e:
        print(f"Error: {e}")
        print("Provide the correct input next time!")
    except Exception as e:
        print(f"Error details: {e}")
    else:
        final_score = calculate_grade(assign1,assign2,exam)
        print(f"Final score:{final_score}")
        grade_score = make_grade(final_score)
        print(f"Grade: {grade_score}")
        save_scores(student_name,
                    assign1,
                    assign2,
                    exam,
                    final_score,
                    grade_score)


main()
