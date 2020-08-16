### IMPORTS AND SETUP VARIABLES
from tkinter import *
FullState = False
PlayerList = []
AddPlayerRelX = 0.49 # Default ADD button Rel X variable in windowed
SortPlayerRelX = 0.51 # Default SORT button Rel X variable in windowed
ScreenBottom = 0.90 # Lowest interface level Y variable

### TKINTER WINDOW & SETUP
WINDOW = Tk()                   # Set WINDOW as tkinter command reference
WINDOW.title("Team Generator")  # Set title name
MAXSIZE = WINDOW.maxsize()      # MAXSIZE var = screen size (usually "1920x1080")
print("Screen Resolution:", MAXSIZE) # Print MAXSIZE var
WINDOW.resizable(False, False)  # Disable window resizing
WINDOW.geometry("1280x720")     # Set window size to 720p (a good size for common 1080p monitors)
WINDOW.overrideredirect(0)      # BORDERLESS WINDOW TESTING (0 = no change, not doing anything)

### TKINTER STYLISING
FONT1 = 'Verdana®'              # Easily changable font string
ButtonColour = "Grey50"         # Button Colour
ButtonPressedColour = "Grey60"  # Button Pressed Colour
ButtonBorder = 0                # Button borders
WINDOW.configure(bg='grey14')   # Background Colour

### FUNCTIONS
def FullscreenToggle(event):
    global FullState
    FullState = not FullState  # opposite bool
    WINDOW.attributes("-fullscreen", FullState) # toggle fullscreen
    SetToggleWindowXY(FullState=FullState)

def SetToggleWindowXY(FullState):
    global AddPlayerRelX; global SortPlayerRelX # Makes these vars available everywhere in code
    if FullState is True:   # if maximized mode
        AddPlayerRelX = 0.495
        SortPlayerRelX = 0.505
        ButtonBottom = 0.95
        print("Fullscreen = True")
    if FullState is False:  # if windowed mode
        AddPlayerRelX = 0.49
        SortPlayerRelX = 0.51
        print("Fullscreen = False")
    AddPlayer.place(relx=AddPlayerRelX, rely=ScreenBottom, anchor=E)
    SortPlayers.place(relx=SortPlayerRelX, rely=ScreenBottom, anchor=W)


def sort():
    print("TBD")


def addtextname():
    AddPlayer = Input.get()
    print(AddPlayer)
    #CODE!!!!!!

def namesprintout():
    print("TBD")

def back():
    print("TBD")

### USER INTERFACE FEATURES
TitleLbl = Label(WINDOW, text="Team Generator!", fg=("deeppink2"), bg=("black"), font=(FONT1, 60))
TitleLbl.place(relx=0.5, anchor=N)

Exit = Button(WINDOW, text="X", fg="red", width=3, height=1, font=(FONT1, 18), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), activeforeground=('dark red'), command=WINDOW.destroy)
Exit.place(x=10, y=10, anchor=NW)

ToggleZoom = Button(WINDOW, text="☐", fg="black", width=3, height=1, font=(FONT1, 18), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), activeforeground=('black'), command=lambda: FullscreenToggle("event"))
ToggleZoom.place(x=70, y=10, anchor=NW)

PlayersLbl = Label(WINDOW, text="PLAYERS\n"+ str(PlayerList), fg=('black'), bg=(ButtonColour), border=(ButtonBorder), font=('Verdana®', 32))
PlayersLbl.place(relx=0.5, rely=0.2, anchor=N)

Input = Entry(font=('Verdana®', 52), bg=(ButtonColour), border=(8))
Input.place(relx=0.5, rely=0.75, anchor=CENTER)

AddPlayer = Button(WINDOW, text="ADD", fg="green", width=13, height=1, font=(FONT1, 36), activeforeground=('dark green'), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), command=addtextname())
AddPlayer.place(relx=AddPlayerRelX, rely=ScreenBottom, anchor=E)

SortPlayers = Button(WINDOW, text="SORT", fg=("RoyalBlue2"), width=13, height=1, font=(FONT1, 36), activeforeground=('RoyalBlue4'), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), command=addtextname())
SortPlayers.place(relx=SortPlayerRelX, rely=ScreenBottom, anchor=W)


### ADDITIONAL TKINTER SETUP AND KEY BINDINGS
WINDOW.bind("<F11>", FullscreenToggle)
WINDOW.bind("<Escape>", WINDOW.destroy)
WINDOW.mainloop()
