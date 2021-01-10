class Color:
    """ This is the parent class"""
    fav_color = "Green"

    def __init__(self, color):
        self.fav_color = color

    def instance_method(self):
        print("I am an instance method.")
        print("Call me with an instance and a dot operator.")
        print(f"My favourite color is: {self.fav_color}")
        print("+" * 15)

    @staticmethod
    def static_method():
        print("I am a static method.")
        print("You can call me without a class instance.")
        print(f"My favourite color is: {Color.fav_color}")
        print("+" * 15)

    @classmethod
    def class_method(cls):
        print("I am a class method.")
        print("You can call me without a class instance.")
        print("In general, you use cls as the class parameter.")
        print(f"My favourite color is: {cls.fav_color}")
        print("+" * 15)


#Creating an object from Student class
my_color = Color("Blue")
print("Calling the instance_method() now.")
my_color.instance_method()

print("Calling the static_method() now.")
Color.static_method()

print("Calling the class_method() now.")
Color.class_method()

print("Changing the color inside the instance now.")
my_color.fav_color = "Red"

print("Calling the instance_method() now.")
my_color.instance_method()

print("Calling the static_method() now.")
Color.static_method()

print("Calling the class_method() now.")
Color.class_method()


'''
print("Alternative way of calling the static and class method.")
#Also works
my_color.static_method()
my_color.class_method()
'''
