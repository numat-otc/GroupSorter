# Imports
import os
import sys
import time
import random
import string

# Setup
VerType = ""
Version = "[V2.1]"  # Current Version (Displayed in window title bar to easily recognise different editions)
os.system("title Group Sorter {}{} - A project by Trey".format(VerType, Version))  # Set the window title bar name
ListYesKey = ["y", "ye", "yes", "yo", "yea", "ya"]  # Yes list, check if input is positive response

global LowerCaseAlphabet  # Make LowerCaseAlphabet accessible anywhere in the code
global timeout  # Make timeout accessible anywhere in the code
global ListPlayers  # Make ListPlayers accessible anywhere in the code
global GoBackList  # Make GoBackList accessible anywhere in the code
global Themes  # Make Themes accessible anywhere in the code
global ThemesCode  # Make ThemesCode accessible anywhere in the code

LowerCaseAlphabet = list(string.ascii_lowercase)  # lowercase alphabet to reference input to, to prevent invalid input
timeout = 1  # The timeout value (in seconds) for when a pause is called
ListPlayers = []  # Declare empty list of players
GoBackList = ["back", "return", "escape", "cancel"]
IllegalInput = ["\\n", "back", "back", "return", "escape", "cancel", "\\", "/",
                "all"]  # Values that the user cannot add to ListPlayers
Themes = ["Classic", "Dark", "Light", "Yellow", "Blue", "Red", "Green", "Cyan"]
ThemesCode = ["07", "0F", "F0", "06", "01", "04", "02", "09"]


##‽TREY‽NUMA‽##

def Settings():
    SettingsTitlePrint = str(("─" * 48) + "\n" + ("─" * 17) + "|| SETTINGS ||" + ("─" * 17) + "\n" + ("─" * 48))
    os.system("title Group Sorter {}{} - Settings".format(VerType,Version))
    global Theme
    global AutoSaveBool
    while True:
        AutoSave()
        while True:
            os.system("cls")
            if AutoSaveBool == True:
                AutoSaveBoolPrint = "On"
            elif AutoSaveBool == False:
                AutoSaveBoolPrint = "Off"
            print(SettingsTitlePrint)
            print("")
            print("1- Change Theme (Currently: {})".format(Theme))
            print("2- Autosave On/Off (Currently: {})".format(AutoSaveBoolPrint))
            print("─" * 8)
            print("> Type the number that corresponds to the")
            print("  setting that you would you like to change")
            print("> Type 'CANCEL' to go back")
            SettingsInput = input("|> ")
            try:
                SettingsInput = int(SettingsInput)
                break
            except:
                if SettingsInput.lower() in GoBackList:
                    return
                print("Error; invalid input.")
                TimeOutNormal()
        if SettingsInput == 1:
            while True:
                os.system("cls")
                print(SettingsTitlePrint)
                print("")
                print("Change Theme to:")
                for i in range(0, len(Themes)):
                    print("{}- {} Mode".format(i + 1, Themes[i]))
                print("─" * 8)
                print("> Type the number that corresponds to the")
                print("  option that you would you like to set")
                print("> Type 'CANCEL' to go back")
                SettingsInput = input("|> ")
                try:
                    SettingsInput = int(SettingsInput)
                except:
                    if SettingsInput.lower() in GoBackList:
                        break
                    print("Error; invalid input.")
                    TimeOutNormal()
                if SettingsInput > 0 and SettingsInput < len(Themes) + 1:
                    os.system("color {}".format(ThemesCode[SettingsInput - 1]))
                    Theme = str(Themes[SettingsInput - 1] + " Mode")
                    break
                else:
                    print("Error; invalid input.")
                    TimeOutNormal()

        elif SettingsInput == 2:
            while True:
                os.system("cls")
                print(SettingsTitlePrint)
                print("")
                print("Change Autosave to:")
                print("1- On")
                print("2- Off")
                print("─" * 8)
                print("> Type the number that corresponds to the")
                print("  option that you would you like to set")
                print("> Type 'CANCEL' to go back")
                SettingsInput = input("|> ")
                try:
                    SettingsInput = int(SettingsInput)
                except:
                    if SettingsInput.lower() in GoBackList:
                        break
                    print("Error; invalid input.")
                    TimeOutNormal()
                if SettingsInput == 1:
                    AutoSaveBool = True
                    break
                elif SettingsInput == 2:
                    AutoSaveBool = False
                    break
                else:
                    print("Error; invalid input.")
                    TimeOutNormal()


# Automatic loading and saving of names and settings upon opening and closing program
def AutoLoad():
    global Theme
    global AutoSaveBool
    # Creat Directory if it doesnt exist
    try:
        os.mkdir("C:\\Users\{}\AppData\Roaming\GroupSorter\\".format(os.getlogin()))
    except:
        pass
    ### LOAD PLAYERS
    try:
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),
                           "r")  # Set document to read and save ListPlayers
    except:
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()), "w")
        AutoSaveTXT.close()
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()), "r")
    FileRead = AutoSaveTXT.readlines()
    if len(FileRead) > 1:  # Fix errors when 2 or more names are saved with a "\n"
        for i in range(0, len(FileRead)):
            if i == len(FileRead) - 1:
                ListPlayers.append(str(FileRead[i]))
            else:
                ListPlayers.append(str(FileRead[i])[0:-1])
    else:
        ListPlayers.extend(FileRead)  # Normal load if 1 name only save in text format

    ### LOAD SETTINGS
    try:
        SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\settings.txt".format(os.getlogin()), "r")
    except:
        SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\settings.txt".format(os.getlogin()), "w")
        SettingsTXT.close()
        SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()), "r")
    FileRead = SettingsTXT.readlines()
    Theme = str("Dark Mode")  # Set Default
    if len(FileRead) > 1:
        y = 5
    else:
        y = 4
    if len(FileRead) > 0:
        for i in range(0, len(Themes)):
            if (str(FileRead[0])[6:-y]) == Themes[i]:
                Theme = str((Themes[i]) + " Mode")
                os.system("color {}".format(ThemesCode[i]))
    try:
        if (str(FileRead[1])[9:]) == "False":
            AutoSaveBool = False
        else:
            AutoSaveBool = True
    except:
        AutoSaveBool = True  # Set Default

    AutoSaveTXT.close()  # Close file (avoid errors as the program does not currently require the association with the text file)
    SettingsTXT.close()


def AutoSave():
    if AutoSaveBool == False:
        try:
            os.remove("C:\\Users\{}\AppData\Roaming\GroupSorter\\Latest.txt".format(os.getlogin()))
        except:
            pass
        return
    AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),
                       "w")  # Set document to read and replace with ListPlayers (even if either are empty)
    for i in range(0, len(ListPlayers)):
        if i == len(ListPlayers) - 1:
            AddLine = str(ListPlayers[i])
        else:
            AddLine = str(ListPlayers[i] + "\n")
        AutoSaveTXT.write(AddLine)

    SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\settings.txt".format(os.getlogin()), "w")
    ThemeSave = str(Theme)[:-5]
    AddLine = str("Theme=" + ThemeSave + "Mode")
    SettingsTXT.write(AddLine)

    AddLine = str("\nAutoSave=" + str(AutoSaveBool))
    SettingsTXT.write(AddLine)

    AutoSaveTXT.close()
    SettingsTXT.close()


def TimeOutNormal():  # When code calls a pause
    time.sleep(timeout)


def TimeOutLong():  # When code calls a longer pause
    time.sleep(timeout + 2)


def TeamSort():  # Sorting Function
    os.system("title Group Sorter {}{} - Sorting {} players into groups".format(VerType, Version,len(ListPlayers)))  # Change title
    while True:  # While True:
        print("> Type the number of groups you would like to sort {} people into ".format(
            len(ListPlayers)))  # Get amount of teams
        print("> Type 'CANCEL' to go back to the main screen")
        NumTeams = (input("|> "))  # Input
        if NumTeams.lower() == "cancel":  # If no input
            break
        AlphabetFound = False
        for i in range(0, 26):
            if LowerCaseAlphabet[i] in NumTeams.lower():
                AlphabetFound = True
                break
        if AlphabetFound == True:
            print("Error; invalid input, only integers allowed")
            TimeOutNormal()
            return

        # Account for errors
        try:
            # Try to make NumTeams an integer
            NumTeams = int(NumTeams)
            # solve empty teams or errors
            if NumTeams > len(ListPlayers):
                print("Error; You entered a higher amount of groups than there is players")
                print("Automatically changed amount of groups to maximum amount of teams ({})".format(len(ListPlayers)))
                NumTeams = len(ListPlayers)
                TimeOutLong()
            elif NumTeams < 2:
                if NumTeams == 1:
                    print("Error; Cannot sort into 1 group.")
                else:
                    print("Error; Cannot sort into {} groups.".format(NumTeams))
                TimeOutNormal()
                break

            # SORTING ALGORITHM
            os.system("title Group Sorter {}{} - Sorting...".format(VerType,Version))  # say sorting, user will only see if the sorting is taking extra long
            NameToTeamList = []
            AmtPerTeam = (len(ListPlayers) // NumTeams)
            Remainder = (len(ListPlayers) - AmtPerTeam * NumTeams)
            # Add sufficient base amounts of team numbers into NameToTeamList
            for i in range(0, AmtPerTeam):
                for z in range(0, NumTeams):
                    NameToTeamList.append(z + 1)
            # Add remaining amount of team numbers to NameToTeamList
            for u in range(0, Remainder):
                NameToTeamList.append(u + 1)

            # Shuffle Teams list 10 times
            for i in range(0, 10):
                random.shuffle(NameToTeamList)

            # Display Teams and corresponding players
            os.system(
                "title Group Sorter {}{} - Sorted {} players into {} groups".format(VerType, Version, len(ListPlayers),NumTeams))
            os.system('cls')
            for i in range(0, NumTeams):
                print("─" * 8)
                print("Team {}: ({})".format(i + 1, NameToTeamList.count(i + 1)))
                for p in range(0, len(NameToTeamList)):
                    if NameToTeamList[p] == i + 1:
                        print(ListPlayers[p])
            print("─" * 8)

            # End of TeamSort, press ENTER to go back to main screen
            input("[ENTER] to skip")
            break

        # Error if integer not given
        except ValueError:
            print("Error; Please enter a valid number (e.g. '{}')".format(random.randint(2, 7)))
            TimeOutNormal()
            break


# If removing player desired
def RemovePlayer(ListPlayersLOWER):
    os.system('cls')
    print("─" * 8)
    print("Players: ({})".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print("{}- {}".format(i + 1, ListPlayers[i]))
    print("─" * 8)
    # Which name or name order number would you like to delete sequence
    print("> Type the number that corresponds to the player that you would you like to delete")
    print("> Type the name of the player that you would like to delete")
    print("> Type 'CANCEL' to go back to the main screen")
    delete = (input("|> "))
    if (delete.lower() in GoBackList):
        return
    elif delete.lower() in ListPlayersLOWER:
        for i in range(0, len(ListPlayers)):
            if delete.lower() in ListPlayersLOWER[i]:
                ListPlayers.pop(i)
    else:
        while True:
            try:
                delete = int(delete)

                if delete <= len(ListPlayers) and delete > 0:
                    ListPlayers.pop(delete - 1)
                else:
                    print("Error; name {} does not exist.".format(delete))
                    TimeOutNormal()
                break
            except ValueError:
                print("Error; invalid input.")
                TimeOutNormal()
                break


def DeleteEndOrStart(p):
    if len(ListPlayers) > 0:
        ListPlayers.pop(p)
        print("position deleted")
        TimeOutNormal()
    else:
        print("Error; Unable to delete position")
        TimeOutNormal()


AutoLoad()  # Startup load
# Forever looping program
while True:
    AutoSave()
    if len(ListPlayers) == 1:
        # Set the window title bar name
        os.system("title Group Sorter {}{} - {} Player".format(VerType, Version, len(ListPlayers)))
    else:
        os.system("title Group Sorter {}{} - {} Players".format(VerType, Version, len(ListPlayers)))
    # Clear (tidy up) screen (command prompt only)
    os.system('cls')
    # Formatting list, easier to read
    print("─" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print(ListPlayers[i])
    # Separate sections
    print("─" * 8)
    print("> Type a name and press [ENTER] to add a player to the list")
    if len(ListPlayers) > 0:
        print("> Type 'SORT' to generate groups")
        print("> Type 'CLEAR' to delete all player names")
        print("> Type 'REMOVE' to delete a specific player")
        print("> Type 'SETTINGS' to adjust preferences")
    addplayer = str(input("|> "))

    # Check to see if an actual name is input
    # (or at least english alphabet characters)
    # So that keeping track of names is easier, also avoid printing errors and such
    AlphabetFound = False
    for i in range(0, 26):
        if LowerCaseAlphabet[i] in addplayer.lower():
            AlphabetFound = True
    # Check if input is invalid (to avoid errors)
    IllegalInputFound = False
    for i in range(0, len(IllegalInput)):
        if IllegalInput[i] in addplayer.lower():
            print("Error; illegal input found")
            AlphabetFound = True
            IllegalInputFound = True
            TimeOutNormal()
            break
    # if name input is valid:
    if AlphabetFound is True and IllegalInputFound is False:
        AlphabetFound = False  # Reset variable
        ListPlayersLOWER = list(map(lambda x: x.lower(), ListPlayers))  # Get a more convenient lowercase copy of input

        # Check if wanting to sort
        if addplayer.lower() == "sort":
            if len(ListPlayers) > 1:  # Only sort if there are 2 or more names
                TeamSort()  # call sorting function
            else:
                print("Error; There are not enough players to sort.")
                TimeOutNormal()

        # Check if wanting to change settings
        elif addplayer.lower() == "settings" or addplayer.lower() == "options":
            Settings()

        # Check if wanting to clear
        elif addplayer.lower() == "clear":
            ListPlayers.clear()  # reset list to nul

        # Check if wanting to delete a single name
        elif addplayer.lower() == "remove" or addplayer.lower() == "rem" or addplayer.lower() == "delete":
            RemovePlayer(ListPlayersLOWER=ListPlayersLOWER)  # call remove player function

        # Check if name already exists
        elif ListPlayersLOWER.count(addplayer.lower()) != 0:
            print("Error; player already found")
            TimeOutNormal()

        # Prevent unaccounted for printing mess ups
        elif len(addplayer) > 24 or len(addplayer) < 3:
            print("Error; Please enter between 2 and 24 characters.")
            TimeOutNormal()

        ### Additional commands that aren't required or as useful, therefore not mentioned to the user

        # Delete last player name
        elif addplayer.lower() == "dellast":
            DeleteEndOrStart(p=-1)

        # Delete first player name
        elif addplayer.lower() == "delfirst":
            DeleteEndOrStart(p=0)

        # Close/End program (helpful during debugging)
        elif addplayer.lower() == "close" or addplayer.lower() == "esc" or addplayer.lower() == "escape" or addplayer.lower() == "exit":
            break

        else:  # Else (if input is not a command)
            ListPlayers.append(addplayer)  # add addplayer userinput to the player list

    else:  # Else (If no english characters present in input)
        if IllegalInputFound is False:
            print("Error; Please use at least one character from the English alphabet.")
            TimeOutNormal()

# Return to start of While True statement
