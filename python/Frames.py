from tkinter import *

window = Tk()
frame = Frame(window,bg="Sky Blue",bd=5,relief=SUNKEN)
frame.pack()
#frame.place(x=0,y=0)
Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()