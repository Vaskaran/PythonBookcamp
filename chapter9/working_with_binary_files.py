# Opening two files-one for reading and one for writing
input_file = open("C:\\TestData\\MyImage.png", "rb")
output_file = open("C:\\TestData\\OutputImage.png", "wb")
content = input_file.read(15)
while len(content):
    output_file.write(content)
    content = input_file.read(15)
input_file.close()
output_file.close()
