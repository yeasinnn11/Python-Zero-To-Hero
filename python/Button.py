from tkinter import *

window = Tk()

count = 0

photo = PhotoImage(file='Love.png')
def click():
    global count
    count+=1
    print(count)

button = Button(window,
                text="click button",
                command=click,
                font=("Comic Sans",30),
                fg="red",
                bg="#000000",
                activeforeground="red",
                activebackground="#000000",
                state=ACTIVE,
                image=photo,
                compound="top")




button.pack()
window.mainloop()