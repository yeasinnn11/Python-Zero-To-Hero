from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll mouse click
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)
#window.bind("<Enter>",doSomething)
#window.bind("<Leave>",doSomething)
window.bind("<Motion>",doSomething)
window.mainloop()