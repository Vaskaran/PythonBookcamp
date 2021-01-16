#Solution to Exercise 3.1
#First user input
first_input = input("Enter first number:")
#Converting it to float
first_number = float(first_input)
#Second user input
second_input = input("Enter second number:")
#Converting it to float
second_number = float(second_input)
#Calculating the average
average = (first_number + second_number) / 2
print("Average is :",average)
print("--------End of Exercise 3.1----------------")

#Solution to Exercise 3.2
print("Hello,\nReader!")
print("--------End of Exercise 3.2----------------")

#Exercise 3.3
print('The height of Andrew is 6\'9" ')
#Alternative:
print("The height of Andrew is 6'9\" ")
print("--------End of Exercise 3.3----------------")

#Exercise 3.4
x, y = 10, 2.5
print(x + y)  #12.5
print(x / y)  #4.0
print("Difference of x and y is:", x - y)  #7.5
#print("x*y=:"+ x*y) #Error: can only concatenate str (not "float") to str
#print(x+ "is stored in x.") #Error: unsupported operand type(s) for +: 'int' and 'str'
print("--------End of Exercise 3.4----------------")

#Exercise 3.5
x = 12
#print("x= "+12)# Prints nothing as it is inside a commented line
print("--------End of Exercise 3.5----------------")

#Exercise 3.6

#Get the radius from the user and converting it into a float
radius = float(input("Enter the radius of the circle:"))
#Area of a circle=(22/7)*r*r where r is the radius
area = (22/7)*radius*radius
print(f"The area of the circle is:{area} square unit.")
print("--------End of Exercise 3.6----------------")
