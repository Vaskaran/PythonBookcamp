# Using with keyword in this example.
# Python closes the file when it is no longer needed.
with open('C:\\TestData\\OriginalFile.txt', 'r') as file_object:
    '''
    print("---Approach:1---")
    print("Reading each lines one by one:")
    first_line = file_object.readline()
    second_line = file_object.readline()
    third_line = file_object.readline()
    #print(first_line)
    #print(second_line)
    #print(third_line)
    print(first_line, end='')
    print(second_line, end='')
    print(third_line, end='')

    #myfile.close()
    '''
    '''
    print("---Approach:2---")
    print("Reading entire file using for loop:")
    #myfile = open('C:\\TestData\\OriginalFile.txt','r')
    for current_line in file_object:
        print(current_line, end='')

    #file_object.close()
    '''
    print("---Approach:3---")
    print("Using the read() method.")
    file_content = file_object.read()
print(file_content)


