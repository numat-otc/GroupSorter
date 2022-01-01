# Imports
import os
import sys
import time
import random
import string

# Setup
VerType = "" # Unused
Version = "[V2.2]"  # Current Version (Displayed in window title bar to easily recognise different editions)
os.system("title Group Sorter {}{} - A project by Trey".format(VerType, Version))  # Set the window title bar name

global LowerCaseAlphabet  # Make LowerCaseAlphabet accessible anywhere in the code
global timeout  # Make timeout accessible anywhere in the code
global ListPlayers  # Make ListPlayers accessible anywhere in the code
global GoBackList # Make GoBackList accessible anywhere in the code
global Themes # Make Themes accessible anywhere in the code
global ThemesCode # Make ThemesCode accessible anywhere in the code

LowerCaseAlphabet = list(string.ascii_lowercase)  # lowercase alphabet to reference input to, to prevent invalid input
timeout = 1  # The timeout value (in seconds) for when a pause is called
ListPlayers = []  # Declare empty list of players
GoBackList = ["back","return","escape","cancel"]
IllegalInput = ["\\n","back","back","return","escape","cancel","\\","/","all"] # Values that the user cannot add to ListPlayers
Themes=["Classic","Dark","Light","Yellow","Blue","Red","Green","LightBlue"]
ThemesCode=["07","0F","F0","06","01","04","02","09"]
##‽TREY‽NUMA‽##


def Settings(): # Settings Menu Function
    SettingsTitlePrint=str(("─"*48)+"\n"+("─"*17)+"|| SETTINGS ||"+("─"*17)+"\n"+("─"*48))
    os.system("title Group Sorter {}{} - Settings".format(VerType,Version))
    global Theme
    global AutoSaveBool
    while True:
        AutoSave() # call autosave function
        # Main menu
        while True:
            os.system("cls")
            if AutoSaveBool == True:
                AutoSaveBoolPrint ="On"
            elif AutoSaveBool == False:
                AutoSaveBoolPrint ="Off"
            print(SettingsTitlePrint)
            print("")
            print("1- Change Theme     (Currently: {})".format(Theme))
            print("2- Autosave On/Off  (Currently: {})".format(AutoSaveBoolPrint))
            print("─"*8)
            print("> Type the number that corresponds to the")
            print("  setting that you would you like to change")
            print("> Type 'RETURN' to go back")
            SettingsInput=input("|> ")
            try:
                SettingsInput=int(SettingsInput)
                break
            except:
                if SettingsInput.lower() in GoBackList: return
                print("Error; invalid input.")
                TimeOut()
        if SettingsInput == 1: # Change theme
            while True: # Loop until valid value received or cancelled
                os.system("cls")
                print(SettingsTitlePrint)
                print("")
                print("Change Theme to:")
                for i in range(0,len(Themes)):
                    print("{}- {} Mode".format(i+1,Themes[i]))
                print("─"*8)
                print("> Type the number that corresponds to the")
                print("  option that you would you like to set")
                print("> Type 'RETURN' to go back")
                SettingsInput=input("|> ")
                try:
                    SettingsInput=int(SettingsInput)
                except:
                    if SettingsInput.lower() in GoBackList:
                        break
                    print("Error; invalid input.")
                    TimeOut()
                if SettingsInput > 0 and SettingsInput < len(Themes)+1:
                    os.system("color {}".format(ThemesCode[SettingsInput-1]))
                    Theme =str(Themes[SettingsInput-1]+" Mode")
                    break
                else:
                    print("Error; invalid input.")
                    TimeOut()

        elif SettingsInput == 2: # Toggle autosave
            while True: # Loop until valid value received or cancelled
                os.system("cls")
                print(SettingsTitlePrint)
                print("")
                print("Change Autosave to:")
                print("1- On")
                print("2- Off")
                print("─"*8)
                print("> Type the number that corresponds to the")
                print("  option that you would you like to set")
                print("> Type 'RETURN' to go back")
                SettingsInput=input("|> ")
                try:
                    SettingsInput=int(SettingsInput)
                except:
                    if SettingsInput.lower() in GoBackList:
                        break
                    print("Error; invalid input.")
                    TimeOut()
                if SettingsInput ==1:
                    AutoSaveBool = True
                    break
                elif SettingsInput ==2:
                    AutoSaveBool = False
                    break
                else:
                    print("Error; invalid input.")
                    TimeOut()



def AutoLoad(): # Automatic loading of names and settings upon opening the program function
    global Theme
    global AutoSaveBool
    # Create Directory if it doesnt exist
    try:
        os.mkdir("C:\\Users\{}\AppData\Roaming\GroupSorter\\".format(os.getlogin()))
    except:
        pass
    # LOAD PLAYERS
    try:
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"r")
    except:
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"w")
        AutoSaveTXT.close()
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"r")
    FileRead = AutoSaveTXT.readlines()
    # Read each line properly and avoid placement/read/write errors
    if len(FileRead) > 1:
        for i in range(0, len(FileRead)):
            if i == len(FileRead) - 1:
                ListPlayers.append(str(FileRead[i]))
            else:
                ListPlayers.append(str(FileRead[i])[0:-1])
    else:
        ListPlayers.extend(FileRead)

    # LOAD SETTINGS
    try:
        SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\settings.txt".format(os.getlogin()),"r")
    except:
        SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\settings.txt".format(os.getlogin()),"w")
        SettingsTXT.close()
        SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"r")
    FileRead = SettingsTXT.readlines()
    Theme = str("Dark Mode") # Set Default
    # Read each line properly and avoid placement/read/write errors
    if len(FileRead) > 1:
        y = 5
    else:
        y = 4
    if len(FileRead) > 0:
        for i in range(0,len(Themes)):
            if (str(FileRead[0])[6:-y]) == Themes[i]:
                Theme=str((Themes[i])+" Mode") # get theme mode into program memory
                os.system("color {}".format(ThemesCode[i])) # perform theme change
    try:
        if (str(FileRead[1])[9:]) == "False":
            AutoSaveBool = False
        else:
            AutoSaveBool = True
    except:
        AutoSaveBool = True # Set Default

    # Close files (avoid association with text file after it is finished with)
    AutoSaveTXT.close()
    SettingsTXT.close()


def AutoSave(): # Automatic saving of names and settings upon calling (when an update to either occurs) function
    try:
        os.remove("C:\\Users\{}\AppData\Roaming\GroupSorter\\Latest.txt".format(os.getlogin()))
    except:
        pass

    if AutoSaveBool == True:
    # SAVE PLAYERS
        AutoSaveTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\Latest.txt".format(os.getlogin()),"w")
        for i in range(0, len(ListPlayers)):
            if i == len(ListPlayers) - 1:
                AddLine = str(ListPlayers[i])
            else:
                AddLine = str(ListPlayers[i] + "\n")
            AutoSaveTXT.write(AddLine)
        AutoSaveTXT.close()

    # SAVE SETTINGS
    SettingsTXT = open(r"C:\Users\{}\AppData\Roaming\GroupSorter\settings.txt".format(os.getlogin()),"w")
    ThemeSave=str(Theme)[:-5]
    AddLine = str("Theme="+ThemeSave+"Mode")
    SettingsTXT.write(AddLine)
    AddLine = str("\nAutoSave="+str(AutoSaveBool))
    SettingsTXT.write(AddLine)
    SettingsTXT.close() # Close file (avoid association with text file after it is finished with)


def TimeOut():  # Normal Pause (Cleans up code and allows continuity between all normal length pauses)
    time.sleep(timeout)


def TimeOutLong(): # Long Pause (Cleans up code and allows continuity between all long length pauses)
    time.sleep(timeout + 2)


def GroupSort(): # Sorting Function
    os.system("title Group Sorter {}{} - Sorting {} players into groups".format(VerType,Version,len(ListPlayers))) # Change title
    while True:
        print("> Type the number of groups you would like to sort {} people into ".format(len(ListPlayers)))
        print("> Type 'RETURN' to go back to the main screen")
        NumGroups = (input("|> ")) # get user input
        if NumGroups.lower() == "cancel":
            break
        AlphabetFound = False
        for i in range(0, 26): # check for all 26 characters in the lowercase alphabet
            if LowerCaseAlphabet[i] in NumGroups.lower():
                AlphabetFound = True
                break
        if AlphabetFound == True: # find error if
            print("Error; invalid input, only integers allowed")
            TimeOut()
            return
        try: # Account for errors
            # Try to make NumGroups an integer
            NumGroups = int(NumGroups)
            # solve empty groups or errors
            if NumGroups > len(ListPlayers):
                print("Error; You entered a higher amount of groups than there is players")
                print("Automatically changed amount of groups to maximum amount of groups ({})".format(len(ListPlayers)))
                NumGroups = len(ListPlayers)
                TimeOutLong()
            elif NumGroups < 2:
                if NumGroups == 1:
                    print("Error; Cannot sort into 1 group.")
                else:
                    print("Error; Cannot sort into {} groups.".format(NumGroups))
                TimeOut()
                return

            # SORTING ALGORITHM
            os.system("title Group Sorter {}{} - Sorting...".format(VerType,Version))  # say sorting, user will only see if the sorting is taking extra long
            NameToGroupList = [] # Clear list
            AmtPerGroup = (len(ListPlayers) // NumGroups)
            Remainder = (len(ListPlayers) - AmtPerGroup * NumGroups)
            # Add sufficient base amounts of group numbers into NameToGroupList
            for i in range(0, AmtPerGroup):
                for z in range(0, NumGroups):
                    NameToGroupList.append(z + 1)
            # Add remaining amount of group numbers to NameToGroupList
            for u in range(0, Remainder):
                NameToGroupList.append(u + 1)

            # Shuffle Groups list 10-50 times (just for added randomness)
            for i in range(0, random.randint(10,50)):
                random.shuffle(NameToGroupList)

            # Display groups and corresponding players
            os.system("title Group Sorter {}{} - Sorted {} players into {} groups".format(VerType, Version, len(ListPlayers),NumGroups))
            os.system('cls')
            for i in range(0, NumGroups):
                print("─" * 8)
                print("Group {}: ({})".format(i + 1, NameToGroupList.count(i + 1)))
                for p in range(0, len(NameToGroupList)):
                    if NameToGroupList[p] == i + 1:
                        print(ListPlayers[p])
            print("─" * 8)

            # End of GroupSort, press ENTER to go back to main screen
            input("[ENTER] to go back")
            return

        # Error if integer not given
        except ValueError:
            print("Error; Please enter a valid number (e.g. '{}')".format(random.randint(2, 7)))
            TimeOut()
            return


def RemovePlayer(ListPlayersLOWER): # Removing a player function
    os.system('cls')
    print("─" * 8)
    print("Players: ({})".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print("{}- {}".format(i + 1, ListPlayers[i]))
    print("─" * 8)
    # Which name or name order number would you like to delete sequence
    print("> Type the number that corresponds to the player that you would you like to delete")
    print("> Type the name of the player that you would like to delete")
    print("> Type 'RETURN' to go back to the main screen")
    delete = (input("|> "))
    # Check if user wants to cancel
    if delete.lower() in GoBackList:
        return
    # Check if value is a string and valid in ListPlayers
    elif delete.lower() in ListPlayersLOWER:
        for i in range(0, len(ListPlayers)):
            if delete.lower() in ListPlayersLOWER[i]:
                ListPlayers.pop(i)
    else:
        # Check if value given is an integer and is valid to delete
        while True:
            try:
                delete = int(delete)

                if delete <= len(ListPlayers) and delete > 0:
                    ListPlayers.pop(delete - 1)
                else:
                    print("Error; name {} does not exist.".format(delete))
                    TimeOut()
                break
            # if input is not valid in either way
            except ValueError:
                print("Error; invalid input.")
                TimeOut()
                break


def DeleteEndOrStart(p): # Delete last or first position (from hidden command)
    if len(ListPlayers) > 0:
        ListPlayers.pop(p)
        print("position deleted")
        TimeOut()
    else:
        print("Error; Unable to delete position")
        TimeOut()


AutoLoad() # Startup load settings and ListPlayers
while True: # Forever looping program
    AutoSave()
    if len(ListPlayers) == 1:
        os.system("title Group Sorter {}{} - {} Player".format(VerType, Version, len(ListPlayers))) # Set the window title bar name (if 1 player)
    else:
        os.system("title Group Sorter {}{} - {} Players".format(VerType, Version, len(ListPlayers))) # Set the window title bar name (any other amount of players)
    # Clear (tidy up) screen (command prompt only)
    os.system('cls')
    # Formatting list, easier to read
    print("─" * 8)
    print("Players: [{}]".format(len(ListPlayers)))
    for i in range(0, len(ListPlayers)):
        print(ListPlayers[i])
    print("─" * 8) # Separate sections
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
            TimeOut()
            break
    # if name input is valid:
    if AlphabetFound is True and IllegalInputFound is False:
        AlphabetFound = False  # Reset variable
        ListPlayersLOWER = list(map(lambda x: x.lower(), ListPlayers))  # Get a more convenient lowercase copy of input to compare with

        # Check if wanting to sort
        if addplayer.lower() =="sort":
            if len(ListPlayers) > 1:  # Only sort if there are 2 or more names
                GroupSort()  # call sorting function
            else:
                print("Error; There are not enough players to sort.")
                TimeOut()

        # Check if wanting to change settings
        elif addplayer.lower() =="settings" or addplayer.lower() =="options":
            Settings() # call settings function

        # Check if wanting to clear
        elif addplayer.lower() =="clear":
            ListPlayers.clear()  # reset list to nul

        # Check if wanting to delete a single name
        elif addplayer.lower() =="remove" or addplayer.lower() =="rem" or addplayer.lower() =="delete":
            RemovePlayer(ListPlayersLOWER=ListPlayersLOWER)  # call remove player function

        # Check if name already exists
        elif ListPlayersLOWER.count(addplayer.lower()) != 0:
            print("Error; player already found")
            TimeOut()

        # Require name input to be between 3-24 characters
        elif len(addplayer) < 3 or len(addplayer) > 24:
            print("Error; Please enter between 2 and 24 characters.")
            TimeOut()

        ### Additional commands that aren't required or as useful, therefore not mentioned to the user

        # Delete last player name
        elif addplayer.lower() == "dellast":
            DeleteEndOrStart(p=-1)

        # Delete first player name
        elif addplayer.lower() == "delfirst":
            DeleteEndOrStart(p=0)

        # Close/End program (helpful during debugging)
        elif addplayer.lower() =="close" or addplayer.lower() =="esc" or addplayer.lower() =="escape" or addplayer.lower() =="exit":
            break

        else:  # Else (if input is not a command and not an error)
            ListPlayers.append(addplayer)  # add user input to the player list

    else:  # Else (If no english characters present in input)
        if IllegalInputFound is False:
            print("Error; Please use at least one character from the English alphabet.")
            TimeOut()

# Return to start of While True statement
