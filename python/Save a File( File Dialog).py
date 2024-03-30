from tkinter import *
from tkinter import filedialog

def SaveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All file", ".*"),
                                    ])
    if file is None:
        return
    #filetext = str(text.get(1.0,END))
    filetext = input("Enter the text: ")
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text='Save',command=SaveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()