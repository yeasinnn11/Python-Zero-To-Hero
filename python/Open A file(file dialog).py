from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(initialfile="E:\\Yeasinn File\\password",
                                          title="Open File")
    file = open(filepath,'r')
    print(file.read())
    file.close()
window = Tk()

button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()
