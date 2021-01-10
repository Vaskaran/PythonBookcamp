class Shape:
    """
    This is the Shape class.
    It is the parent class of Rectangle
    in this example.
    """

    def __init__(self):
        self.type = "Shape"

    def about_me(self):
        print(f"I am a {self.type}.")


class Rectangle(Shape):
    """
    This is the Rectangle class which
    inherits from  the Shape class
    """

    def __init__(self):
        self.type = "Rectangle"

    def about_me(self):
        print(f"I am a {self.type}.")


print("***Simple inheritance example.***")
shape_ob = Shape()
print(f"The shape_ob.type={ shape_ob.type}")
shape_ob.about_me()

rectangle_ob = Rectangle()
print(f"The rectangle_ob.type={ rectangle_ob.type}")
rectangle_ob.about_me()
