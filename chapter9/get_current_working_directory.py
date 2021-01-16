import os

current_path = os.getcwd()
print("The current working directory is as follows:")
print(current_path)

relative_path = "AnotherDirectory\\SubDirectory"
new_path = os.path.join(os.getcwd(), relative_path)
print("The new path is as follows:")
print(new_path)
