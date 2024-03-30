import os

source = "folder"
destination = "C:\\Users\\gigabyte\\OneDrive\\folder"

try:
    if os.path.exists(destination):
        print("There is a alredy file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+"was not found")