from os import rename,remove

#Renaming the image
rename("C:\\TestData\\OutputImage.png", "C:\\TestData\\OutputImage1.png")
#Deleting the file
remove("C:\\TestData\\OutputImage1.png")
#remove("C://TestData//OutputImage1.png")  # Also works

