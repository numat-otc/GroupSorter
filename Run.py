import os
import time
from random import randint
import string

ListYesKey = ["y", "ye", "yes", "yo", "yea", "ya"]
LowerAlphabet = list(string.ascii_lowercase)
ListPlayers = []
AlphabetFound = False


def TeamSort():
    while True:
        # Account for errors
        try:
            # Get amount of teams
            print("Sort {} people into how many teams?".format(len(ListPlayers)))
            NumTeams = int(input("|> "))
            # solve empty teams or errors
            if (NumTeams > len(ListPlayers)):
                print("Error, You entered a higher amount of teams than there is players")
                print("Automatically changed amount of teams to {} (maximum amount of teams)".format(len(ListPlayers)))
                NumTeams = len(ListPlayers)
                time.sleep(4)
            elif (NumTeams < 1):
                print("Error, Cannot have {} teams.".format(NumTeams))
                time.sleep(2)
                break

            # SORTING ALGORITHM
            NameToTeamList = []
            AmtPerTeam = (len(ListPlayers) // NumTeams)
            Remainder = (len(ListPlayers) - AmtPerTeam * NumTeams)
            for i in range(0,1):
                for i in range(0, len(ListPlayers)):
                    while True:
                        Random = randint(1, NumTeams)
                        if (NameToTeamList.count(Random) != AmtPerTeam):
                            NameToTeamList.append(Random)
                            break



                # for i in range(0,NumTeams):
                # print(NameToTeamList.count(i+1))
            print(ListPlayers)
            print(NameToTeamList)

            # x=46
            # y=6
            # z=(x//y)
            # print(z)
            # remainder=(x-y*z)
            # print(remainder)
            # for i in range(1,):
            #    randint(0,)
            # print(len(ListPlayers)/NumTeams)
            # print(ListPlayers)
            # print(NameToTeamList)

            # End (hold screen until reset/enter pressed)
            input("\nPress ENTER to return. ")
            break

        # Error if integer not given
        except ValueError:
            print("Error, Please enter a valid number (e.g. '{}')".format(randint(2, 7)))
            time.sleep(2)
            break


# If removing player desired (function 2)
def RemovePlayer(ListPlayers):
    os.system('cls')
    print("_" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print("{}- {}".format(i + 1, ListPlayers[i]))
    print("_" * 8)
    while True:
        try:
            print("Which numbered player name would you like to delete?")
            delete = int(input("|> "))
            if delete <= len(ListPlayers) and delete > 0:
                ListPlayers.pop(delete - 1)
            else:
                print("Error, name {} does not exist.".format(delete))
                time.sleep(2)
            break
        except ValueError:
            print("Error, invalid input.")
            time.sleep(2)
            break


# Forever Looping base UI
while True:
    # Clear (tidy up) screen (command prompt only)
    os.system('cls')
    # Formatting list, easier to read
    print("_" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print(ListPlayers[i])
    # Separate sections
    print("_" * 8)
    print("Type a name and press enter to add a player to sort.")
    if len(ListPlayers) > 0:
        print("OR type SORT to generate teams")
        print("OR type CLEAR to delete all player names")
        print("OR type REMOVE to delete a specific player")
    addplayer = str(input("|> "))

    # Check to see if an actual name is input
    # (or at least english alphabet characters)
    # So that keeping track of names is easier, also avoid printing errors and such
    for i in range(0, 26):
        if LowerAlphabet[i] in addplayer.lower():
            AlphabetFound = True
    # if name is valid:
    if AlphabetFound is True:
        AlphabetFound = False
        # Check if name is already present in list
        ListPlayersLOWER = list(map(lambda x: x.lower(), ListPlayers))
        # Check if wanting to sort
        if addplayer.lower() == "sort":
            # call sorting func
            TeamSort()

        # Check if wanting to clear
        elif addplayer.lower() == "clear":
            # reset list to nul
            ListPlayers.clear()

        # Check if wanting to delete a single name
        elif addplayer.lower() == "remove" or addplayer.lower() == "delete":
            # call remove player func
            RemovePlayer(ListPlayers=ListPlayers)

        # Check if name already exists
        elif ListPlayersLOWER.count(addplayer.lower()) != 0:
            print("Error, player already found")
            time.sleep(2)

        # Fix unaccounted for printing mess ups
        elif len(addplayer) > 24:
            print("Please enter 24 or less characters.")
            time.sleep(2)

        # Additional commands that arent required or as useful

        # Delete last player name
        elif addplayer.lower() == "dellast":
            if len(ListPlayers) > 0:
                ListPlayers.pop(-1)
                print("Last position deleted")
                time.sleep(1)
            else:
                print("Unable to delete last position")
                time.sleep(1)

        elif addplayer.lower() == "delfirst":
            if len(ListPlayers) > 0:
                ListPlayers.pop(0)
                print("First position deleted")
                time.sleep(1)
            else:
                print("Unable to delete first position")
                time.sleep(1)
        elif addplayer.lower() == "preset1":
            ADDPRESET = ["Trey", "Pedro", "Dom", "Alex", "Sam", "Gref", "David", "Ben", "Finn", "Connor", "Griffin",
                         "Luka", "Tyrone", "Erik"]
            ListPlayers.extend(ADDPRESET)

        # otherwise...
        else:
            # add addplayer input to player list
            ListPlayers.append(addplayer)
    # If no english characters present in input
    else:
        print("Please use at least one character from the English alphabet.")
        time.sleep(2)

# Return to start of While True statement
