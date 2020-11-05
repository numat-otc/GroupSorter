from tkinter import *  # This imports the module that creates the interface
import random  # This imports the pseudo random module
from tkinter import filedialog  # Import file explorer functionality
VerType = "[Rev. III] "
Version = "[V0.3]"
##‽TREY‽NUMA‽##


def MainPage():
    global AddNameEntry
    global AddPlayerButton
    global NameList
    global RecentTotalSorts

    AddNameEntry = Text(WINDOW, width=14, font=(TkFont, 27), bg=TkBack2, fg=TkFore2, bd=0, height=1); AddNameEntry.place(relx=0.02, rely=0.8, anchor=W)
    AddNameEntry.focus()

    WINDOW.bind("<Return>","<KeyRelease-Return>", lambda e: AddNameEnter(AddNameEntry.get("1.0", "end")))
    AddPlayerButton = Button(WINDOW, text="Add", font=(TkFont, 30), bg=TkBack2, fg="darkviolet", bd=0, width=12,command=lambda: AddName(AddNameEntry.get("1.0", "end"))); AddPlayerButton.place(relx=0.02, rely=0.88, anchor=W)
    SortButton = Button(WINDOW, text="Sort", font=(TkFont, 35), bg=TkBack2, fg="cadetblue2", bd=0, width=15, command=SortTeams, height=2); SortButton.place(relx=0.18, rely=0.85, anchor=W)
    AddTeamButton = Button(WINDOW, text="+", font=(TkFont + "Bold", 45), bg=TkBack, fg="forest green", bd=0, width=3, command=CreateTeam, height=1, activeforeground="forest green", activebackground=TkBack); AddTeamButton.place(relx=0.4, rely=0.86, anchor=W)
    MinusTeamButton = Button(WINDOW, text="-", font=(TkFont + "Bold", 45), bg=TkBack, fg="orangered2", bd=0, width=3, command=DeleteTeam, height=1, activeforeground="orangered1", activebackground=TkBack); MinusTeamButton.place(relx=0.45, rely=0.8575, anchor=W)
    RecentTotalSorts = Label(WINDOW, text="0 Recent TotalSorts", font=(TkFont, 30), bg=TkBack, fg=TkFore); RecentTotalSorts.place(relx=0.9, rely=0.88, anchor=CENTER)
    ExportButton = Button(WINDOW, text="Export to .html", font=(TkFont, 24), bg=TkBack2, fg="yellow", bd=0, command=Export); ExportButton.place(relx=0.82, rely=0.79, anchor=NW)

    Exit = Button(WINDOW, text="X", fg="red", width=3, height=1, font=(TkFont, 18), bg=TkBack, bd=0, activeforeground=("dark red"), command=WINDOW.destroy); Exit.place(x=10, y=10, anchor=NW)
    Maximize = Button(WINDOW, text="☐", fg="black", width=3, height=1, font=(TkFont, 18), bg=TkBack, bd=0, activeforeground=("black"), command=lambda: FullscreenToggle("event")); Maximize.place(x=61, y=10, anchor=NW)
    w = Scrollbar (WINDOW,)
    w.place(relx=0.1, rely=0.1, anchor=NW)
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

def Export():
    savefile = filedialog.asksaveasfilename(initialdir="%username%/desktop", title="Select a File", filetypes=(("Text files", "*.txt"), ("all files", "*.")))


def AddNameEnter(Name):
    Name = Name[0: -1]
    if len(Name) == 1:
        AddNameEntry.delete("1.0", "end")
        SortTeams()
        return
    AddName(Name)


def AddName(Name):
    global NameList
    global PlayerList
    AddNameEntry.delete("1.0", "end")
    Name = Name[0: len(Name) - 1]
    if len(NameList) == 10:
        return

    if len(Name) < 2 or len(Name) > 10:
        return
    try:
        NameList
    except:
        NameList = []
    NameList.append(Name)
    DropDownPlayerList()


def DropDownPlayerList():
    global NamesShowing
    try:
        ClearDropDownPlayerList()
    except:
        pass
    NamesShowing = 0
    global PlayerVerticalCoords
    PlayerVerticalCoords = []
    AddTo = 0.06
    for i in range(len(NameList)):
        PlayerVerticalCoords.append(0.1 + (i * AddTo))
        CreateName(i)
        NamesShowing += 1


def ClearDropDownPlayerList():
    for i in range(NamesShowing):
        globals()["PlayerNameButton" + str(i)].destroy()


def CreateName(i):
    globals()["PlayerNameButton" + str(i)] = Button(WINDOW, text=(NameList[i] + "\n"), font=(TkFont, 30), bg=TkBack, fg=TkFore, takefocus=False, activeforeground=TkFore2, activebackground=TkBack, bd=0, command=lambda: RemovePlayer(i), width=10, anchor=W, height=1)
    globals()["PlayerNameButton" + str(i)].place(relx=0.02, rely=PlayerVerticalCoords[i], anchor=W)
    globals()["PlayerNameButton" + str(i)].bind("<Enter>", lambda e: HighlightPlayerName(i))
    globals()["PlayerNameButton" + str(i)].bind("<Leave>", lambda e: UnHighlightPlayerName(i))


def RemovePlayer(i):
    global NameList
    global AmtTeams
    NameList.pop(i)
    if len(NameList) > AmtTeams:
        DeleteTeam()
    DropDownPlayerList()


def HighlightPlayerName(i):
    globals()["PlayerNameButton" + str(i)].config(fg="orangered1")


def UnHighlightPlayerName(i):
    globals()["PlayerNameButton" + str(i)].config(fg=TkFore2)


def SortTeams():
    global AmtTeams
    global NameList
    global NameShuffle
    global HasSorted
    global TotalSorts
    global RecentTotalSorts
    if AmtTeams == 1:
        CreateTeam()
    elif AmtTeams == 0:
        for i in range(2):
            CreateTeam()
    if len(NameList) < 2:
        return
    HasSorted = True
    TotalSorts += 1
    RecentTotalSorts.config(text=(str(TotalSorts) + " Recent TotalSorts"))
    try:
        for i in range(6):
            globals()["Team" + str(i)] = []
    except:
        pass
    NameShuffle = list(NameList)
    random.shuffle(NameShuffle)
    a = 0
    b = 0
    while True:
        globals()["Team" + str(b)].append(NameShuffle[a])
        if b + 1 == AmtTeams:
            b = 0
        else:
            b += 1
        if a + 1 == len(NameShuffle):
            break
        else:
            a += 1
    for i in range(AmtTeams):
        UsedList = globals()["Team" + str(i)]
        PrintedNames = ""
        for x in range(len(UsedList)):
            PrintedNames += "\n" + str(UsedList[x])
        globals()["TeamLabel" + str(i)].config(text=str(PrintedNames))


def CreateTeam():
    global AmtTeams
    global NameList
    if AmtTeams < 2:
        pass
    elif AmtTeams == len(NameList):
        return
    TeamHorizontal = []
    TeamVertical = []
    for a in range(3):
        for b in range(2):
            TeamHorizontal.append(0.18 + (a * 0.2375))
    for i in range(3):
        TeamVertical.append(0.2)
        TeamVertical.append(0.55)
    globals()["TeamLabel" + str(AmtTeams)] = Label(WINDOW, text=(""), font=(TkFont, 30), bg=TkBack, fg=TkFore, width=18, height=7, anchor=N, bd=2, relief="groove")
    globals()["TeamLabel" + str(AmtTeams)].place(relx=TeamHorizontal[AmtTeams], rely=TeamVertical[AmtTeams], anchor=W)
    AmtTeams += 1


def DeleteTeam():
    global AmtTeams
    if AmtTeams == 2:
        return
    globals()["TeamLabel" + str(AmtTeams - 1)].destroy()
    AmtTeams -= 1


def INIT():
    global WINDOW      # globalise these variables to any module within the program
    global TkBack
    global TkFore
    global TkFont
    global TkBack2
    global TkFore2
    global AmtTeams
    global NameList
    global HasSorted
    global TotalSorts
    global FullState

    TkBack = "grey14"   # Tk Background variable
    TkFore = "grey92"   # Tk Standard Text variable
    TkFont = "Verdana®" # Tk Font variable
    TkBack2 = "grey24"  # Tk Button background variable
    TkFore2 = "grey85"  # SPARE Tk variable

    WINDOW = Tk()  # This creates the tkinter reference name
    WINDOW.state("zoomed")  # This starts it in maximized mode
    WINDOW.config(bg=TkBack)  # This makes the background equal to the previously set up variable
    WINDOW.title("Team Generator - {}{}".format(VerType, Version))  # This changes the title
    WINDOW.iconbitmap(bitmap="Team Generator Logo.ico")
    #DISABLED# WINDOW.overrideredirect(True) # Remove borders
    WINDOW.resizable(False, False)  # Disable window resizing
    WINDOW.geometry("1920x1080")     # Set window size to 720p (a good size for common 1080p monitors)
    MainPage()  # This actives the function that starts up the first page
    WINDOW.bind("<F11>", FullscreenToggle)
    WINDOW.bind("<Escape>", lambda e: WINDOW.destroy())
    FullState = False
    AmtTeams = 0
    NameList = []
    HasSorted = False
    TotalSorts = 0
    for i in range(2):
        CreateTeam()
    WINDOW.mainloop()


INIT()  # Run Initialisation function once code fully loaded through