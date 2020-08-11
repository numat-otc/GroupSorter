# Library imports and variable setups
from tkinter import *

WINDOW = Tk()
WINDOW.title("Team Generator")


def sort():
    print("TBD")


def addtextname():
    print("TBD")


def namesprintout():
    print("TBD")


lbl = Label(WINDOW, text="Team Generator!", fg='purple', bg='turquoise', font=("Verdana", 60))
lbl.place(relx=0.5, rely=0.05, anchor=CENTER)
exit = Button(WINDOW, text="X", fg="red", width=2, height=1, font=('Verdana', 18), command=WINDOW.destroy).grid(row=0, column=0)

addplayer = Button(WINDOW, text="ADD", command=addtextname())

WINDOW.state('zoomed')
addplayer.grid()
WINDOW.mainloop()
