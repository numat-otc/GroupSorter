# Library imports and variable setups
from tkinter import *
FullState = False
FullScreenBool = FullState
PlayerList = []
AddPlayerRelX = 0.4
SortPlayerRelX = 0.6
ButtonColour = "Grey70"

WINDOW = Tk() # Set WINDOW as tkinter command name
WINDOW.title("Team Generator") # Set title name
MAXSIZE = WINDOW.maxsize() # Get maximum window size
WINDOW.resizable(False, False); print("Screen Resolution:", MAXSIZE) # Disable window resizing (account for )
FONT1 = 'Verdana®' # Easily changable font string
WINDOW.geometry("1280x720") # Set window size to 720p (a good size for common 1080p monitors)
WINDOW.overrideredirect(0)
ButtonColour = "Grey70" # Button Colour
ButtonPressedColour = "Grey60" # Button Pressed Colour
WINDOW.configure(bg='grey18') # Background Colour

def FullscreenToggle(event,FullScreenBool):
    global FullState
    FullState = not FullState  # opposite bool
    WINDOW.attributes("-fullscreen", FullState) # toggle fullscreen
    FullScreenBool = FullState
    SetToggleWindowXY(FullState=FullState)

def SetToggleWindowXY(FullState):
    global AddPlayerRelX; global SortPlayerRelX # Makes these vars available everywhere in code
    if FullState is True:
        AddPlayerRelX = 0.442
        SortPlayerRelX = 0.558
        print("True")
    if FullState is False:
        AddPlayerRelX = 0.4
        SortPlayerRelX = 0.6
        print("False")


def sort():
    print("TBD")


def addtextname():
    AddPlayer = Input.get()
    #CODE!!!!!!

def namesprintout():
    print("TBD")

def back():
    print("TBD")


TitleLbl = Label(WINDOW, text="Team Generator!", fg='purple', bg='turquoise', font=(FONT1, 60))
TitleLbl.place(relx=0.5, anchor=N)

Exit = Button(WINDOW, text="X", fg="red", width=3, height=1, font=(FONT1, 18), bg=(ButtonColour), activebackground=("white"), activeforeground=('dark red'), command=WINDOW.destroy)
Exit.place(x=10, y=10, anchor=NW)

ToggleZoom = Button(WINDOW, text="☐", fg="black", width=3, height=1, font=(FONT1, 18), bg=(ButtonColour), activebackground=("white"), activeforeground=('black'), command=lambda: FullscreenToggle("event",FullScreenBool=FullScreenBool))
ToggleZoom.place(x=70, y=10, anchor=NW)

PlayersLbl = Label(WINDOW, text="PLAYERS\n"+ str(PlayerList), fg=('black'), bg=(ButtonColour), font=('Verdana®', 32))
PlayersLbl.place(relx=0.5, rely=0.2, anchor=N)

Input = Entry(font=('Verdana®', 48), bg=(ButtonColour), border=8)
Input.place(relx=0.5, rely=0.75, anchor=CENTER)

AddPlayer = Button(WINDOW, text="ADD", fg="green", width=8, height=1, font=(FONT1, 32), activeforeground=('light green'), bg=(ButtonColour), command=addtextname())
AddPlayer.place(relx=AddPlayerRelX, rely=0.9, anchor=CENTER)

SortPlayers = Button(WINDOW, text="SORT", fg="orange", width=8, height=1, font=(FONT1, 32), activeforeground=('dark orange'), bg=(ButtonColour), command=addtextname())
SortPlayers.place(relx=SortPlayerRelX, rely=0.9, anchor=CENTER)



# Key bindings
WINDOW.bind("<F11>", FullscreenToggle)
WINDOW.bind("<Escape>", back)
WINDOW.mainloop()