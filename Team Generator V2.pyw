# Library imports and variable setups
from tkinter import *
FullState = False

PlayerList = []

WINDOW = Tk()
WINDOW.title("Team Generator")
Fullscreen = False

# Easily changable font variable
FONT1 = 'Verdana®'



def FullscreenToggle(event):
    global FullState
    FullState = not FullState  # Just toggling the bool
    WINDOW.attributes("-fullscreen", FullState)

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

def sort():
    print("TBD")


def addtextname():
    AddPlayer = AddInput.get()


def namesprintout():
    print("TBD")


TitleLbl = Label(WINDOW, text="Team Generator!", fg='purple', bg='turquoise', font=('Verdana®', 60))
TitleLbl.place(relx=0.5, anchor=N)

exit = Button(WINDOW, text="X", fg="red", width=3, height=1, font=(FONT1, 18), activeforeground=('dark red'), command=WINDOW.destroy)
exit.place(x=10, y=10, anchor=NW)

togglezoom = Button(WINDOW, text="🢄", fg="chocolate1", width=3, height=1, font=(FONT1, 18), bg=("yellow"), activeforeground=('chocolate3'), command=lambda: FullscreenToggle("event"))
togglezoom.place(x=70, y=10, anchor=NW)

PlayersLbl = Label(WINDOW, text="z", fg='black', bg='yellow', font=('Verdana®', 60))
PlayersLbl.place(relx=0.5, rely=0.2, anchor=N)

AddInput = Entry(font=('Verdana®', 60))
AddInput.place(relx=0.5, rely=0.75, anchor=CENTER)

addplayer = Button(WINDOW, text="ADD", fg="green", width=8, height=1, font=(FONT1, 32), activeforeground=('light green'), command=addtextname())
addplayer.place(relx=0.442, rely=0.9, anchor=CENTER)

sortplayer = Button(WINDOW, text="SORT", fg="orange", width=8, height=1, font=(FONT1, 32), activeforeground=('dark orange'), command=addtextname())
sortplayer.place(relx=0.558, rely=0.9, anchor=CENTER)


# Get maximum window size
MAXSIZE = WINDOW.maxsize()
ResizeBool = False
WINDOW.resizable(ResizeBool, ResizeBool)
print(MAXSIZE)

WINDOW.bind("<F11>", FullscreenToggle)



WINDOW.geometry("1280x720")
z = WINDOW.grab_status()
print(z)
# Fullscreen
WINDOW.mainloop()
