from tkinter import *
from tkinter import colorchooser
def click():
    #color = colorchooser.askcolor()
    #print(color)
    #colorhex = color[1]
    #print(colorhex)
    #window.config(bg=colorhex)
    window.config(bg=colorchooser.askcolor()[1])
window = Tk()
window.geometry("500x500")
button = Button(text='Click',command=click)
button.pack()
window.mainloop()