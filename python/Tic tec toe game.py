from tkinter import *
import random

def next_turn():
    pass

def check_winner():
    pass
def empty_spaces():
    pass
def new_game():
    pass

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o","y"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text=player + " turn", font=("consolas",40))
label.pack(side="top")

reset_button = Button(text="restart", font=("consolas",20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()


window.mainloop()