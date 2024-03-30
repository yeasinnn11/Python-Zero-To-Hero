from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='yeasin.png')

label = Label(window,
              text="Yeasin Arafat",
              font=('Arial',40,'bold'),
              fg='#ff086b',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=10,
              pady=10,
              image=photo,
              compound='bottom')

label.pack()

#label.place(x=100,y=100)

window.mainloop()