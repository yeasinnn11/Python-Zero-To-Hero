from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("500x500")
window.title("Yeasin first GUI program")

logo = PhotoImage(file='logo.png')
window.iconphoto(True,logo)
window.config(background="#000000")


window.mainloop() #place window on computer screen, listen for events