print("Exercise-11.1 and Exercise -11.2")


class Student:
    class_name = "Student"

    def __init__(self,roll_number):
        self.roll_number = roll_number

    def about_me(self,name):
        """ A simple method """
        print(f"Hello,{name}!")
        print(f"You belong to {self.class_name} class!")
        print(f"Your roll number is:{self.roll_number}")


#Creating an object from Student class
student_1 = Student(25)  #correct.Ex-11.1
#student_1 = Student() #error. Ex-11.2
#Invoking the method
student_1.about_me("Mike")

print("-" * 30)
print("Exercise-11.3")


class College:
    college = "Abc"

    def __init__(self, name, stud_name, roll_number):
        self.college = name
        self.stud_name = stud_name
        self.roll_number = roll_number

    def about_me(self):
        print(f"College name is: {self.college}")
        print(f"The student name is: {self.stud_name}")
        print(f"The roll number is: {self.roll_number}")


student_1 = College("St. Stephen", "Bob", 2)
student_1.about_me()

print("-" * 30)
print("Exercise-11.4")


class Student:
    def __init__(self, roll_number, name="Mike"):
        self.name = name
        self.roll_number = roll_number

    def about_me(self):
        print(f"Name is: {self.name}")
        print(f"The roll number is: {self.roll_number}")


student_1 = Student("Bob",1)
print("\nStudent-1 detail:")
student_1.about_me()

print("\nStudent-2 detail:")
student_2 = Student(2)
student_2.about_me()

#student_3 = Student() # Error: passing a roll number is a must now


print("-" * 30)
print("Exercise-11.5")


class Parent:
    @staticmethod
    def static_method():
        print("Static method inside Parent is called.")

    @classmethod
    def class_method(cls):
        print(f"Class method is called.Invoker type:{cls}")


class Child(Parent):
    """ This is a Child class."""

    @staticmethod
    def static_method():
        print("The static method inside Child is called.")


parent_ob = Parent()
child_ob = Child()
parent_ob.class_method()
child_ob.class_method()
parent_ob.static_method()
child_ob.static_method()

print("-" * 30)
print("Exercise-11.6")


class ParentClass:
    @staticmethod
    def static_method():
        print("Static method inside Parent is called.")


class ChildClass(Parent):
    pass


ParentClass.static_method()
ChildClass.static_method()

print("-" * 30)

