#Following example uses a custom exception
class MyException(Exception):
    """ This is a custom exception."""
    pass


try:
    user_input = int(input("Enter an integer which is not greater than 100:"))
    if user_input > 100:
        raise MyException("You have made the integer greater than 100.")
    print(f"Well done.You have entered:{user_input}")
except MyException as e:
    print(f"Custom exception is raised.Error Details:{e}")
except ValueError as e:
    print(f"Here is the error Details:{e}")


