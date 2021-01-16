class Parent:
    """ This is the parent class"""

    def __init__(self):
        self.i = 1  #public variable
        self.__j = 10  #private variable

    def __private_show_me(self):
        print(f"i={self.i}")
        print(f"__j={self.j}")

    def about_me(self):
        print(f"i={self.i}")
        print(f"__j={self.__j}")


parent_ob = Parent()
print(f"parent_ob.i={parent_ob.i}")
#print(parent_ob.__j)#will cause error
print("Calling about_me() now:")
parent_ob.about_me()
#print("Calling __private_show_me() now:")
#parent_ob.__private_show_me() #will cause error

#print(parent_ob._Parent__j)#it works and prints 10


