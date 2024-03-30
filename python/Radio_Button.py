from tkinter import *

food = ["Pizza","Hamburger","Hotdog"]

def order():
    if(x.get()==0):
        print("you Order pizza")
    elif(x.get()==1):
        print("You Order a hamburger")
    elif(x.get()==2):
        print("You Order a hotdog")
    else:
        print("huh?")


window = Tk()
pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodIamge = [pizzaImage,hamburgerImage,hotdogImage]
x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=20,
                              font=("Impact",23,),
                              image=foodIamge[index],
                              compound='left',
                              indicatoron=0,
                              width=210,
                              command=order,
                              )
    radiobutton.pack(anchor=W)
window.mainloop()