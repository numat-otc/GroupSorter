from tkinter import * # This imports the module that creates the interface
import random # This imports the needed modules
##‽TREY‽NUMA‽##


def MainPage():
    global AddNameEntry
    global AddButton
    global NameList
    global RecentSorts
    AddNameEntry = Text(root, width = 14, font = (DefFont, 27), bg=SecBack, fg=SecFore, bd=0, height = 1); AddNameEntry.place(relx=0.02, rely=0.8, anchor = W)
    AddNameEntry.focus()

    root.bind("<Return>", lambda event: AddNameEnter(AddNameEntry.get("1.0","end")))
    AddButton = Button(root, text="Add", font = (DefFont, 30), bg=SecBack, fg="hot pink", bd=0, width=12, command = lambda: AddName(AddNameEntry.get("1.0","end"))); AddButton.place(relx=0.02, rely=0.88, anchor = W)
    SortButton = Button(root, text="Sort", font = (DefFont, 35), bg=SecBack, fg='steel blue', bd=0, width=15, command = SortTeams, height = 2); SortButton.place(relx=0.18, rely=0.85, anchor = W)
    AddTeamButton = Button(root, text="+", font = (DefFont + "Bold", 45), bg=DefBack, fg="forest green", bd=0, width=3, command = CreateTeam, height = 1, activeforeground="forest green", activebackground = DefBack); AddTeamButton.place(relx=0.4, rely=0.86, anchor = W)
    MinusTeamButton = Button(root, text="-", font = (DefFont + "Bold", 45), bg=DefBack, fg='orangered1', bd=0, width=3, command = DeleteTeam, height = 1, activeforeground="orangered1", activebackground = DefBack); MinusTeamButton.place(relx=0.45, rely=0.8575, anchor = W)
    RecentSorts = Label(root, text="0 Recent Sorts", font = (DefFont, 30), bg=DefBack, fg=DefFore); RecentSorts.place(relx=0.9, rely=0.88, anchor = CENTER)
    ExportButton = Button(root, text="Export to .html", font = (DefFont, 24), bg=SecBack, fg='yellow', bd=0, command = SortTeams); ExportButton.place(relx=0.82, rely=0.79, anchor = NW)

def Export():
    print("Do Later")

def AddNameEnter(Name):
    Name = Name[0: -1]
    if len(Name) == 1:
        AddNameEntry.delete("1.0","end")
        SortTeams()
        return
    AddName(Name)


def AddName(Name):
    global NameList
    global PlayerList
    AddNameEntry.delete("1.0","end")
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
    global PlayerVerticalCoordinates
    PlayerVerticalCoordinates = []
    AddTo = 0.06
    for i in range(len(NameList)):
        PlayerVerticalCoordinates.append(0.1 + ( i * AddTo ))
        CreateName(i)
        NamesShowing += 1

def ClearDropDownPlayerList():
    for i in range(NamesShowing):
        globals()["PlayerNameButton" + str(i)].destroy()


def CreateName(i):
    globals()["PlayerNameButton" + str(i)] = Button(root, text=(NameList[i] + "\n"), font=(DefFont, 30), bg=DefBack, fg=DefFore, takefocus=False, activeforeground=SecFore, activebackground=DefBack, bd=0, command = lambda: RemovePlayer(i), width=10, anchor = W, height = 1)
    globals()["PlayerNameButton" + str(i)].place(relx=0.02, rely=PlayerVerticalCoordinates[i], anchor = W)
    globals()["PlayerNameButton" + str(i)].bind("<Enter>", lambda event: HighlightPlayerName(i))
    globals()["PlayerNameButton" + str(i)].bind("<Leave>", lambda event: UnHighlightPlayerName(i))


def RemovePlayer(i):
    global NameList
    NameList.pop(i)
    DropDownPlayerList()


def HighlightPlayerName(i):
    globals()["PlayerNameButton" + str(i)].config(fg="orangered1")

def UnHighlightPlayerName(i):
    globals()["PlayerNameButton" + str(i)].config(fg=SecFore)


def SortTeams():
    global TeamCount
    global NameList
    global NameShuffle
    global HasSorted
    global Sorts
    global RecentSorts
    if TeamCount == 1:
        CreateTeam()
    elif TeamCount == 0:
        for i in range(2):
            CreateTeam()
    if len(NameList) < 2:
        return
    HasSorted = True
    Sorts += 1
    RecentSorts.config(text=(str(Sorts) + " Recent Sorts"))
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
        if b + 1 == TeamCount:
            b = 0
        else:
            b += 1
        if a + 1 == len(NameShuffle):
            break
        else:
            a += 1
    for i in range(TeamCount):
        UsedList = globals()["Team" + str(i)]
        PrintedNames = ""
        for x in range(len(UsedList)):
            PrintedNames +=  "\n" + str(UsedList[x])
        globals()["TeamLabel" + str(i)].config(text=str(PrintedNames))


def CreateTeam():
    global TeamCount
    global NameList
    if TeamCount < 2:
        pass
    elif TeamCount == len(NameList):
        return
    TeamHorizontal = []
    TeamVertical = []
    for a in range(3):
        for b in range(2):
            TeamHorizontal.append(0.18 + (a * 0.2375))
    for i in range(3):
        TeamVertical.append(0.2)
        TeamVertical.append(0.55)
    globals()["TeamLabel" + str(TeamCount)] = Label(root, text=(""), font=(DefFont, 30), bg=DefBack, fg=DefFore, width = 18, height=7, anchor = N, bd=2, relief='groove'); globals()["TeamLabel" + str(TeamCount)].place(relx=TeamHorizontal[TeamCount], rely=TeamVertical[TeamCount], anchor = W)
    TeamCount += 1


def DeleteTeam():
    global TeamCount
    if TeamCount == 1:
        return
    globals()["TeamLabel" + str(TeamCount - 1)].destroy()
    TeamCount -= 1


def Initialise():
    global root # This makes the main window a global variable so that any function outside of Initialise can access and change it
    global DefBack
    global DefFore
    global DefFont
    global SecBack
    global SecFore
    global TeamCount
    global NameList
    global HasSorted
    global Sorts

    DefBack = "grey11"
    DefFore = "grey92"
    DefFont = "Verdana®"
    SecBack = "grey19"
    SecFore = "grey85"

    root = Tk() # This creatse the initial window
    root.state("zoomed") # This starts it in zoom mode
    root.config(bg=DefBack) # This makes the background equal to the previously set up variable
    root.title("Team Generator") # This changes the title
    MainPage() # This actives the function that starts up the first page

    TeamCount = 0
    NameList = []
    HasSorted = False
    Sorts = 0
    for i in range(2):
        CreateTeam()
    root.mainloop()
Initialise()
