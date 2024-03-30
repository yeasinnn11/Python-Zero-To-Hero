

#try:
    #with open('C:\\Users\\gigabyte\\OneDrive\\Desktop\\text.txt') as file:
            #print(file.read())

#except FileNotFoundError:
    #print("That file was not found ")



                          #write a file
#text = "Have a nice day"

#with open("C:\\Users\\gigabyte\\OneDrive\\Desktop\\text.txt","a") as file:
    #file.write(text)


                        #copy a file

# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies meradata (file's creation and modification times)

import shutil

shutil.copyfile("C:\\Users\\gigabyte\\OneDrive\\Desktop\\text.txt",
                "C:\\Users\\gigabyte\\OneDrive\\Desktop\\copy.txt")

#sroce, destination