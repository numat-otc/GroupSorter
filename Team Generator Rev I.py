#Imports
import os
import time
import random
import string

#Setup
VerType =""
Version = "[V1.4]" # Current Version (Displayed in window title bar to easily recognise different editions)
os.system("title Team Generator {}{} - A project by Trey".format(VerType,Version)) # Set the window title bar name
ListYesKey = ["y", "ye", "yes", "yo", "yea", "ya"] # Yes list, check if input is positive response
global LowerCaseAlphabet
LowerCaseAlphabet = list(string.ascii_lowercase) # Alphabet to reference input to prevent invalid input
ListPlayers = [] # Declare empty list of players
##‽TREY‽NUMA‽##

def TeamSort():                                                                                                     # Sorting Function
    os.system("title Team Generator {}{} - Sorting {} players into teams".format(VerType,Version,len(ListPlayers)))     # Change title
    while True:                                                                                                         # While True:
        print("> Type the number of teams you would like to sort {} people into ".format(len(ListPlayers)))                 # Get amount of teams
        print("> Type 'cancel' to go back to the main screen")
        NumTeams = (input("|> "))                                                                                           # Input
        if NumTeams.lower() == "cancel" or NumTeams.lower() == "" or LowerCaseAlphabet in NumTeams.lower():                                                          # If no input
            break
        # Account for errors
        try:
            # Try to make NumTeams an integer
            NumTeams = int(NumTeams)
            # solve empty teams or errors
            if NumTeams > len(ListPlayers):
                print("Error; You entered a higher amount of teams than there is players")
                print("Automatically changed amount of teams to {} (maximum amount of teams)".format(len(ListPlayers)))
                NumTeams = len(ListPlayers)
                time.sleep(4)
            elif NumTeams < 2:
                if NumTeams == 1:
                    print("Error; Cannot sort into 1 team.")
                else:
                    print("Error; Cannot sort into {} teams.".format(NumTeams))
                time.sleep(2)
                break

            # SORTING ALGORITHM 2.0
            os.system("title Team Generator {}{} - Sorting...".format(VerType,Version)) #say sorting, user will only see if the sorting is taking extra long
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
            os.system("title Team Generator {}{} - Sorted {} players into {} teams".format(VerType,Version, len(ListPlayers), NumTeams))
            os.system('cls')
            for i in range(0, NumTeams):
                print("_" * 8)
                print("Team {}: ({})".format(i + 1, NameToTeamList.count(i + 1)))
                for p in range(0, len(NameToTeamList)):
                    if NameToTeamList[p] == i + 1:
                        print(ListPlayers[p])
            print("_" * 8)

            # End of TeamSort, press ENTER to go back to main screen
            input("\nPress ENTER to return. ")
            break

        # Error if integer not given
        except ValueError:
            print("Error; Please enter a valid number (e.g. '{}')".format(random.randint(2, 7)))
            time.sleep(2)
            break


# If removing player desired (function 2)
def RemovePlayer(ListPlayers, ListPlayersLOWER):
    os.system('cls')
    print("_" * 8)
    print("Players: ({})".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print("{}- {}".format(i + 1, ListPlayers[i]))
    print("_" * 8)

    # Which name or name order number would you like to delete sequence
    print("> Type a number that corresponds to a player that you would you like to delete")
    print("> Type a name of a player that you would like to delete")
    print("> Type 'cancel' to go back to the main screen")
    delete = (input("|> "))
    if (delete.lower() == "cancel" or delete.lower() == ""):
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
                    time.sleep(2)
                break
            except ValueError:
                print("Error; invalid input.")
                time.sleep(2)
                break

def DeleteEndOrStart(p,ListPlayers):
    if len(ListPlayers) > 0:
        ListPlayers.pop(p)
        print("position deleted")
        time.sleep(1) # Pause for 1 second
    else:
        print("Unable to delete first position")
        time.sleep(1) # Pause for 1 second


# Forever Looping base UI
while True:
    # Set the window title bar name
    if len(ListPlayers) == 1:
        # Set the window title bar name
        os.system("title Team Generator {}{} - {} Player".format(VerType,Version, len(ListPlayers)))
    else:
        os.system("title Team Generator {}{} - {} Players".format(VerType,Version, len(ListPlayers)))
    # Clear (tidy up) screen (command prompt only)
    os.system('cls')
    # Formatting list, easier to read
    print("_" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print(ListPlayers[i])
    # Separate sections
    print("_" * 8)
    print("> type a name and press enter to add a player to the list")
    if len(ListPlayers) > 0:
        print("> type SORT to generate teams")
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
    # if name is valid:
    if AlphabetFound is True:
        AlphabetFound = False
        # Check if name is already present in list
        ListPlayersLOWER = list(map(lambda x: x.lower(), ListPlayers))
        # Check if wanting to sort
        if addplayer.lower() == "sort":
            # Only sort if there are 2 or more names
            if len(ListPlayers) > 1:
                # call sorting function
                TeamSort()
            else:
                print("Error; There are not enough players to sort.")
                time.sleep(2)

        # Check if wanting to clear
        elif addplayer.lower() == "clear":
            ListPlayers.clear() # reset list to nul

        # Check if wanting to delete a single name
        elif "remove" in addplayer.lower() or "delete" in addplayer.lower():
            RemovePlayer(ListPlayers=ListPlayers, ListPlayersLOWER=ListPlayersLOWER) # call remove player function

        # Check if name already exists
        elif ListPlayersLOWER.count(addplayer.lower()) != 0:
            print("Error; player already found")
            time.sleep(1) # Pause for 1 second

        # Prevent unaccounted for printing mess ups
        elif len(addplayer) > 24:
            print("Please enter 24 or less characters.")
            time.sleep(1) # Pause for 1 second

        # Disallow 'cancel' to be added to the player list
        elif addplayer.lower() == "cancel":
            print("Error; Cannot enter name cancel")
            time.sleep(1) # Pause for 1 second

        ### Additional commands that aren't required or as useful, therefore not mentioned to the user

        # Delete last player name
        elif addplayer.lower() == "dellast":
            DeleteEndOrStart(p=-1,ListPlayers=ListPlayers)

        # Delete first player name
        elif addplayer.lower() == "delfirst":
            DeleteEndOrStart(p=0,ListPlayers=ListPlayers)

        else: # Else (if input is not a command)
            ListPlayers.append(addplayer) # add addplayer userinput to the player list

    else: # Else (If no english characters present in input)
        print("Please use at least one character from the English alphabet.")
        time.sleep(2)

# Return to start of While True statement
