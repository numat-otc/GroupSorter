# Library imports and variable setups
from tkinter import *
PlayerList = []

WINDOW = Tk()
WINDOW.title("Team Generator")

# Easily changable font variable
FONT1 = 'Verdana®'

def ToggleWindowResize():
    print("TBD")
    WINDOW.resizable(False, False)

def sort():
    print("TBD")


def addtextname(PlayerList):
    AddPlayer = AddInput.get()


def namesprintout():
    print("TBD")


TitleLbl = Label(WINDOW, text="Team Generator!", fg='purple', bg='turquoise', font=('Verdana®', 60))
TitleLbl.place(relx=0.5, anchor=N)

exit = Button(WINDOW, text="X", fg="red", width=3, height=1, font=(FONT1, 18), activeforeground=('dark red'), command=WINDOW.destroy)
exit.place(relx=0.005, rely=0.01, anchor=NW)

PlayersLbl = Label(WINDOW, text="z", fg='black', bg='yellow', font=('Verdana®', 60))
PlayersLbl.place(relx=0.5, rely=0.2, anchor=N)

AddInput = Entry(font=('Verdana®', 60))
AddInput.place(relx=0.5, rely=0.75, anchor=CENTER)

addplayer = Button(WINDOW, text="ADD", fg="green", width=8, height=1, font=(FONT1, 32), activeforeground=('light green'), command=addtextname(PlayerList=PlayerList))
addplayer.place(relx=0.442, rely=0.9, anchor=CENTER)

sortplayer = Button(WINDOW, text="SORT", fg="orange", width=8, height=1, font=(FONT1, 32), activeforeground=('dark orange'), command=addtextname(PlayerList=PlayerList))
sortplayer.place(relx=0.558, rely=0.9, anchor=CENTER)

# Get maximum window size
MAXSIZE = WINDOW.maxsize()
print(MAXSIZE)
# Set un maximized window to 1280x720
WINDOW.geometry("1280x720")
# Fullscreen
WINDOW.state('zoomed')
WINDOW.mainloop()
