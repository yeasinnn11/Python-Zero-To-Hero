from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("forte",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel= Label(window,text="Enter your first name:",width=20,font="bold",fg="Dark Blue").grid(row=1,column=0)
firstNameEntry= Entry(window).grid(row=1,column=1)

lastNameLabel= Label(window,text="Enter your last name:",width=20,font="bold",fg="Dark Blue").grid(row=2,column=0)
lastNameEntry= Entry(window).grid(row=2,column=1)

emailLabel= Label(window,text="Enter your email:",width=20,font="bold",fg="Dark Blue").grid(row=3,column=0)
emailEntry= Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()
