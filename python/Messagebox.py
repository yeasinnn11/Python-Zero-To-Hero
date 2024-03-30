from tkinter import *
from tkinter import messagebox
def click():
    #messagebox.showinfo(title='This is an info messagebox',
                        #message='You are a human')
    #messagebox.showwarning(title='Warning!',
                        #message='You have a virus!!!')
    #messagebox.showerror(title='Error!',
                        #message='something went wrong')
    #if messagebox.askokcancel(title='ok or cancel',
                                #message='Do you want to marry her'):
        #print("Congratulation")
    #else:
        #print("May ALLAH bless you with someone else")
    #if messagebox.askretrycancel(title='retry or cancel',
                                 #message='Do you want to marry her'):
         #print("Congratulation")
    #else:
         #print("May ALLAH bless you with someone else")
    #if messagebox.askyesno(title='yes or no',
                                 #message='Do you lick yeasinnn'):
         #print("Yeasinnn also lick you")
    #else:
         #print("Yeasinnn deserve better then you")

    #answer = messagebox.askquestion(title='Ask Question',
                                    #message='Do you lick me')
    #if (answer == 'yes'):
        #print("I lick you too")
    #else:
        #print("why do you not lick me")
    answer = messagebox.askyesnocancel(title='yes , no ro cancel',
                                    message='Do you lick me')
    if (answer == 'yes'):
        print("I lick you too")
    elif(answer == 'no'):
        print("why do you not lick me")
    else:
        print("you have lost a golden chance")
window = Tk()

button = Button(window,command=click,text='click me')
button.pack()
window.mainloop()