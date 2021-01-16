text = "abcABc"
print("The text is: " + text)
# Printing individual characters inside the string
print("The first occurrence of 'A' is at index:")
print(text.index("A"))
print("The first occurrence of 'c' is at index:")
print(text.index("c"))
print("The first occurrence of 'bcA' is at index:")
print(text.index("bcA"))

print("-"*10)

# I want to examine what happens if the intended character
# is NOT present inside the string.
text = " Hello, John!"
#print(text.index("y")) #error now

# I want to examine a function that accepts multiple parameters
# Using the replace() function for this example.
text = "Hello, John!"
print("Initial text is :" + text)
print("Replacing the name 'John' with 'Bob' now.")
text = text.replace("John", "Bob")
print("The changed text is :" + text)
