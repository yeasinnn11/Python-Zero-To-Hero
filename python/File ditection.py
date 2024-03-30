import os

path = "C:\\Users\\gigabyte\\OneDrive\\Desktop\\folder"

if os.path.exists(path):
    print("This location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.exists(path):
        print("That is a directory")
else:
    print("That location doesn't exist")