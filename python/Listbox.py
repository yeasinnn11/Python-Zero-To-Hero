def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    for index in food:
        print("Yot have ordered: "+index)
    #print("You have order "+ listbox.get(listbox.curselection()))

def Add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def Delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


from tkinter import *

window = Tk()
window.title("Entry Box")
listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Forte",40),
                  width=12,
                  selectmode=MULTIPLE)
                  #height=7)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Jhal muri")
listbox.insert(3,"Bhel puri")
listbox.insert(4,"Hamburger")
listbox.insert(5,"Hilish pulaw")
listbox.insert(6,"Chingri Bhorta")
listbox.config(height=listbox.size())

entrybox= Entry(window)
entrybox.pack()

submitbutton = Button(window,text="Submit",command=submit)
submitbutton.pack()
Addbutton = Button(window,text="Add",command=Add)
Addbutton.pack()
Deletebutton = Button(window,text="Delete",command=Delete)
Deletebutton.pack()
window.mainloop()