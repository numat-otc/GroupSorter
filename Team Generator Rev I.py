# Imports
import os
import sys
import time
import random
import string

# Setup
VerType = ""
Version = "[V2.0]"  # Current Version (Displayed in window title bar to easily recognise different editions)
os.system("title Group Sorter {}{} - A project by Trey".format(VerType, Version))  # Set the window title bar name
ListYesKey = ["y", "ye", "yes", "yo", "yea", "ya"]  # Yes list, check if input is positive response

global LowerCaseAlphabet  # Make LowerCaseAlphabet accessible anywhere in the code
global timeout  # Make timeout accessible anywhere in the code
global ListPlayers  # Make ListPlayers accessible anywhere in the code

LowerCaseAlphabet = list(string.ascii_lowercase)  # lowercase alphabet to reference input to, to prevent invalid input
timeout = 1  # The timeout value (in seconds) for when a pause is called
ListPlayers = []  # Declare empty list of players
IllegalInput = ["\\n", "back", "cancel","\\"] # Values that the user cannot add to ListPlayers


# Automatic loading and saving of names upon opening and closing program
def AutoLoad():
    AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"r")  # Set document to read and save ListPlayers
    FileRead = AutoSaveTXT.readlines()
    TXTLines = len(FileRead)
    if len(FileRead) > 1:  # Fix errors when 2 or more names are saved with a "\n"
        for i in range(0, len(FileRead)):
            if i == TXTLines - 1:
                ListPlayers.append(str(FileRead[i]))
            else:
                ListPlayers.append(str(FileRead[i])[0:-1])
    else:
        ListPlayers.extend(FileRead)  # Normal load if 1 name only save in text format
    # print("FileReadList",FileRead)
    # print("Text file lines (saves)",TXTLines)
    # print("ListPlayers",ListPlayers)
    AutoSaveTXT.close()  # Close file (avoid errors as the program does not currently require the association with the text file)


def AutoSave():
    AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"w")  # Set document to read and replace with ListPlayers (even if either are empty)
    for i in range(0, len(ListPlayers)):
        if i == len(ListPlayers) - 1:
            AddLine = str(ListPlayers[i])
        else:
            AddLine = str(ListPlayers[i] + "\n")
        AutoSaveTXT.write(AddLine)
    AutoSaveTXT.close()


try:
    AutoLoad()
except:
    os.mkdir("C:\\Users\{}\AppData\Roaming\GroupSorter\\".format(os.getlogin()))


##‽TREY‽NUMA‽##


def TimeOutNormal():  # When code calls a pause
    time.sleep(timeout)


def TimeOutLong():  # When code calls a longer pause
    time.sleep(timeout + 2)


def TeamSort():  # Sorting Function
    os.system("title Group Sorter {}{} - Sorting {} players into groups".format(VerType,Version,len(ListPlayers)))  # Change title
    while True:  # While True:
        print("> Type the number of groups you would like to sort {} people into ".format(
            len(ListPlayers)))  # Get amount of teams
        print("> Type 'cancel' to go back to the main screen")
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
                print("Automatically changed amount of groups to maximum amount of teams ({len(ListPlayers)})")
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
                print("_" * 8)
                print("Team {}: ({})".format(i + 1, NameToTeamList.count(i + 1)))
                for p in range(0, len(NameToTeamList)):
                    if NameToTeamList[p] == i + 1:
                        print(ListPlayers[p])
            print("_" * 8)

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
    print("_" * 8)
    print("Players: ({})".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print("{}- {}".format(i + 1, ListPlayers[i]))
    print("_" * 8)

    # Which name or name order number would you like to delete sequence
    print("> Type the number that corresponds to the player that you would you like to delete")
    print("> Type the name of the player that you would like to delete")
    print("> Type 'cancel' to go back to the main screen")
    delete = (input("|> "))
    if (delete.lower() == "cancel" or delete.lower() == "back" or delete.lower() == ""):
        pass
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


# Forever Looping base UI
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
    print("_" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print(ListPlayers[i])
    # Separate sections
    print("_" * 8)
    print("> type a name and press [ENTER] to add a player to the list")
    if len(ListPlayers) > 0:
        print("> type SORT to generate groups")
        print("> type CLEAR to delete all player names")
        print("> type REMOVE to delete a specific player")
    addplayer = str(input("|> "))

    # Check to see if an actual name is input
    # (or at least english alphabet characters)
    # So that keeping track of names is easier, also avoid printing errors and such
    AlphabetFound = False
    for i in range(0, 26):
        if LowerCaseAlphabet[i] in addplayer.lower():
            AlphabetFound = True
    # if name input is valid:
    if AlphabetFound is True:
        AlphabetFound = False  # Reset variable
        ListPlayersLOWER = list(map(lambda x: x.lower(), ListPlayers))  # Get a more convenient lowercase copy of input

        # Check if input is invalid (to avoid errors)
        for i in range(0, len(IllegalInput)):
            if IllegalInput[i] in addplayer.lower():
                print("Error; illegal input found")
                TimeOutNormal()

        # Check if wanting to sort
        if addplayer.lower() == "sort":
            if len(ListPlayers) > 1:  # Only sort if there are 2 or more names
                TeamSort()  # call sorting function
            else:
                print("Error; There are not enough players to sort.")
                TimeOutNormal()

        # Check if wanting to clear
        elif addplayer.lower() == "clear":
            ListPlayers.clear()  # reset list to nul

        # Check if wanting to delete a single name
        elif "remove" in addplayer.lower() or "delete" in addplayer.lower():
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
        print("Error; Please use at least one character from the English alphabet.")
        TimeOutNormal()

# Return to start of While True statement
