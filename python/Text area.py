from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,bg="light blue",
            font=("Forte",25),
            height=15,
            width=30,
            padx=20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()
