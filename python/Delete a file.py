import os

import shutil

path = "folder"

try:
    #os.remove(path)
    #os.mkdir(path)
    shutil.rmtree(path)

except FileNotFoundError:
    print("This file was deleted")

except PermissionError:
    print("you can't delete this file without permission")

except OSError :
    print("you cannot delete that using that function ")

else:
    print(path+"was deleted")