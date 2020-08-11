# Library imports and variable setups
from tkinter import *
PlayerList = []

WINDOW = Tk()
WINDOW.title("Team Generator")

# Easily changable font variable
FONT1 = 'Verdana®'


def sort():
    print("TBD")


def addtextname(PlayerList):
    AddPlayer = AddInput.get()


def namesprintout():
    print("TBD")


lbl = Label(WINDOW, text="Team Generator!", fg='purple', bg='turquoise', font=('Verdana®', 60))
lbl.place(relx=0.5, anchor=N)

exit = Button(WINDOW, text="X", fg="red", width=3, height=1, font=(FONT1, 18), command=WINDOW.destroy)
exit.place(relx=0.005, rely=0.01, anchor=NW)

AddInput = Entry()
AddInput.place(relx=0.5, rely=0.8, anchor=CENTER)


addplayer = Button(WINDOW, text="ADD", fg="red", width=5, height=1, font=(FONT1, 32), command=addtextname(PlayerList=PlayerList))
addplayer.place(relx=0.5, rely=0.9, anchor=CENTER)

WINDOW.state('zoomed')

WINDOW.mainloop()
