from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " Degree c~")
window = Tk()
hotImage = PhotoImage(file="hot.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()
scale = Scale(window,
              from_=100,
              to=0,
              length=700,
              orient=VERTICAL,
              font=("Consolas",20),
              tickinterval=10,
              #showvalue=0,
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="#111111",

              )
scale.pack()
coldImage = PhotoImage(file="Cold.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()
button = Button(window,text="Submit",command=submit)
button.pack()
window.mainloop()