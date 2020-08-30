### IMPORTS AND SETUP VARIABLES
from tkinter import * # Python User interface library
import time # Used for time sequences
import random # Used for random number generation and list shuffling
FullState = False
PlayerList = [FIRST]
AddPlayerRelX = 0.49 # Default ADD button Rel X variable in windowed
SortPlayerRelX = 0.51 # Default SORT button Rel X variable in windowed
ScreenBottom = 0.90 # Lowest interface level Y variable
Version = 2.1

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


def sort(PlayerList):
    while True:
        # Get amount of teams
        print("> Type the number of teams you would like to sort {} people into ".format(len(PlayerList)))
        print("> Type 'cancel' to go back to the main screen")
        #NumTeams = (input("|> "))
        NumTeams = str(2)
        if NumTeams.lower() == "cancel" or NumTeams.lower() == "":
            break
        # Account for errors
        try:
            # Try to make NumTeams an integer
            NumTeams = int(NumTeams)
            # solve empty teams or errors
            if NumTeams > len(PlayerList):
                print("Error; You entered a higher amount of teams than there is players")
                print("Automatically changed amount of teams to {} (maximum amount of teams)".format(len(PlayerList)))
                NumTeams = len(PlayerList)
                time.sleep(4)
            elif NumTeams < 2:
                if NumTeams == 1:
                    print("Error; Cannot sort into 1 team.")
                else:
                    print("Error; Cannot sort into {} teams.".format(NumTeams))
                time.sleep(2)
                break

            # SORTING ALGORITHM 2.0
            NameToTeamList = []
            AmtPerTeam = (len(PlayerList) // NumTeams)
            Remainder = (len(PlayerList) - AmtPerTeam * NumTeams)
            # Add sufficient base amounts of team numbers into NameToTeamList
            for k in range(0, AmtPerTeam):
                for z in range(0, NumTeams):
                    NameToTeamList.append(z + 1)
            # Add remaining amount of team numbers to NameToTeamList
            for u in range(0, Remainder):
                NameToTeamList.append(u + 1)

            # Shuffle Teams list 10 times
            for p in range(0, 10):
                random.shuffle(NameToTeamList)

            for i in range(0, NumTeams):
                print("_" * 8)
                print("Team {}: ({})".format(i + 1, NameToTeamList.count(i + 1)))
                for p in range(0, len(NameToTeamList)):
                    if NameToTeamList[p] == i + 1:
                        print(PlayerList[p])
            print("_" * 8)
            break
        # Error if integer not given
        except ValueError:
            print("Error; Please enter a valid number (e.g. '{}')".format(random.randint(2, 7)))
            time.sleep(2)
            break

def addtextname(PlayerList):
    global AddPlayer # Make Input availble anywhere in code (mostly for testing)
    AddPlayer = Input.get()
    # TESTING
    print(AddPlayer)
    PlayerList.append(AddPlayer) # Add input to PlayerList
    print(PlayerList)
    print("INPUT: {}".format(AddPlayer))



    PlayersLbl.place(relx=0.5, rely=0.2, anchor=N) # Update label PlayersLbl
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

Maximize = Button(WINDOW, text="☐", fg="black", width=3, height=1, font=(FONT1, 18), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), activeforeground=('black'), command=lambda: FullscreenToggle("event"))
Maximize.place(x=61, y=10, anchor=NW)

PlayersLbl = Label(WINDOW, text=("PLAYERS\n {}".format(PlayerList)), fg=('black'), bg=(ButtonColour), border=(ButtonBorder), font=('Verdana®', 32))
PlayersLbl.place(relx=0.5, rely=0.2, anchor=N)

Input = Entry(WINDOW, font=('Verdana®', 52), bg=(ButtonColour), border=(8))
Input.place(relx=0.5, rely=0.75, anchor=CENTER)

AddPlayer = Button(WINDOW, text="ADD", fg="green", width=13, height=1, font=(FONT1, 36), activeforeground=('dark green'), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), command=lambda:addtextname(PlayerList=PlayerList))
AddPlayer.place(relx=AddPlayerRelX, rely=ScreenBottom, anchor=E)

SortPlayers = Button(WINDOW, text="SORT", fg=("RoyalBlue2"), width=13, height=1, font=(FONT1, 36), activeforeground=('RoyalBlue4'), bg=(ButtonColour), border=(ButtonBorder), activebackground=(ButtonPressedColour), command=sort(PlayerList=PlayerList))
SortPlayers.place(relx=SortPlayerRelX, rely=ScreenBottom, anchor=W)

w = Scrollbar(WINDOW,)

### ADDITIONAL TKINTER SETUP AND KEY BINDINGS
WINDOW.bind("<F11>", FullscreenToggle)
WINDOW.bind("<Escape>", WINDOW.destroy)
WINDOW.mainloop()
