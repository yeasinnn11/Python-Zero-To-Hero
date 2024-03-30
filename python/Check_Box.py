from tkinter import *
def display():
    if(x.get()==1):
        print("You Agreed")
    else:
        print("You don't Agree")


window = Tk()
x = IntVar()
python_photo = PhotoImage(file='python.png')
check_button= Checkbutton(window,
                          text="I Agree with you",
                          font=("Arial",20,'bold'),
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          command=display,
                          fg="blue",
                          background="black",
                          activeforeground="blue",
                          activebackground="black",
                          padx=20,
                          pady=10,
                          image=python_photo,
                          compound='left')

check_button.pack()
window.mainloop()