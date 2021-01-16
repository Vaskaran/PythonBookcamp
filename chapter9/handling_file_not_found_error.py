# Using try-except to handle FileNotFoundError
try:
    my_file = 'C:\\TestData\\OriginalFile_1.txt'
    with open(my_file, 'r') as file_object:
        print("Using the read() method.")
        file_content = file_object.read()
    print(file_content)
except FileNotFoundError as e:
    print(f"The file {my_file} is not found.")
    print(f"Error details:{e}")
