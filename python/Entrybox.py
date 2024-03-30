from tkinter import *

def submit():
    username = entry.get()
    print("hey " +username)
    #entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1, END)
window = Tk()
entry = Entry(window,
              font=("Arial",30),
              fg="red",
              background="black",
              show="*")
#entry.insert(0,'Hafsa')
entry.pack(side=LEFT)
submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)
delete_button = Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)
backspace_button = Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=RIGHT)
window.mainloop()