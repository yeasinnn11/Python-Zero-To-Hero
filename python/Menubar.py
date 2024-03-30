from tkinter import *

def openFile():
    print("File Have been opened")
def saveFile():
    print("File Have been Saved")
def copy():
    print("File Have been Copied")
def cut():
    print("File Have been Cut")
def paste():
    print("File Have been Pasted")
window = Tk()

openImage = PhotoImage(file="folder.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("Mv Boli",10))
menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("Mv Boli",10))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()