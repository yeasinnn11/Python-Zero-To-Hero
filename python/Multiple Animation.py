from tkinter import *
from Ball import *
import time

window = Tk()
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"red")
tennis_ball = Ball(canvas,0,0,50,3,2,"yellow")
basket_ball = Ball(canvas,0,0,70,5,3,"orange")
while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()