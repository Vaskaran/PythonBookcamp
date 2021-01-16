# Opening two files-one for reading and one for writing
input_file = open('C:\\TestData\\OriginalFile.txt', 'r')
# Will NOT work if the file does not exist
output_file = open('C:\\TestData\\OutputFile.txt', 'r+')
# Will work even if the file does not exist
#output_file = open('C:\\TestData\\OutputFile.txt', 'w')
content = input_file.read(15)
while len(content):
    output_file.write(content)
    #output_file.write(content + "\n")
    content = input_file.read(15)
input_file.close()
output_file.close()
