def print_file_content(input_file):
    """ This function can print the content of a text file."""
    try:
        with open(input_file,"r") as file_object:
            file_content = file_object.read()
    except FileNotFoundError as e:
        print(f"The file {input_file} is not found.")
        print(f"Error details:{e}")
    else:
        print(file_content)


print_file_content('C:\\TestData\\OriginalFile.txt')
