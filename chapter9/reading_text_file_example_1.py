#reading_text_file_example_1.py

file_object = open('C:\\TestData\\OriginalFile.txt', 'r')
print("---Approach:1---")
print("Reading each line one by one:")
first_line = file_object.readline()
second_line = file_object.readline()
third_line = file_object.readline()
print(first_line)
print(second_line)
print(third_line)
#print(first_line, end='')
#print(second_line, end='')
#print(third_line, end='')
file_object.close()

print("---Approach:2---")
print("Reading entire file using for loop:")
file_object = open('C:\\TestData\\OriginalFile.txt', 'r')
for current_line in file_object:
    print(current_line, end='')
file_object.close()

print("\n---Approach:3---")
file_object = open('C:\\TestData\\OriginalFile.txt', 'r')
print("Using the read() method.")
file_content = file_object.read()
print(file_content)

print("------------")
#file_object = open('C:\\TestData\\OriginalFile.txt', 'r')
#for current_line in file_object:
   #print(current_line, end='**')
