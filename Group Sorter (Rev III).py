from tkinter import *  # tkinter lib
from tkinter import ttk  # tkinter lib
import random # random lib
import os # windows cmd commands lib

### UI Theme Colours
BaseBG  = "grey16"
BG      = "grey30"
FG      = "grey80"
FONT    = "Calibri"
##‽TREY‽NUMA‽##

root = Tk()
root.title("Group Sorter [Rev. III]") # window title
root.resizable(False, False) # disable window resizing
root.geometry("720x960") # window size (3:4 aspect-ratio [3]x240,[4]x240)
root.configure(bg=BaseBG) # background colour
border = Label(bg=BG).place(height=922,width=3,relx=0.52,rely=0.5,anchor="center") # (off) center line

global names
names=[]

def Add(): # Add name to names list func
    adding=str(addinput.get())
    addinput.delete(0, "end")
    if len(adding) == 0:
        print("input empty")
        return
    elif len(adding) not in range(2,21):
        os.system('msg "%username%" Invalid input length, enter between 2-20')
    elif len(names) >=24:
        os.system('msg "%username%" Maximum names reached (24)')
    elif adding not in names:
        names.append(adding)
        print("input added")
        print(len(names),names)
        RenderNames()
    else:
        print("Error; unable to add input to names")
        os.system('''msg "%username%" Name '{}' already exists'''.format(adding))

def ClearInput(): # Clear name input func
    addinput.delete(0, "end")
    print("input cleared")

def ClearList(): # Clear entire names list func
    names.clear()
    print("clear list")

def RenderNames(): # Render names onto screen from names list func
    try:
        for name in range(len(names)):
            globals()["name{}".format(name)].destroy()
            globals()["namedel{}".format(name)].destroy()
            print("destroyed ({}):{}".format(name+1,names[name]))
    except:
        pass
    for name in range(len(names)):
        globals()["name{}".format(name)] = Label(font=(FONT,"22"), text=names[name], fg=FG, bg=BaseBG,)
        globals()["name{}".format(name)].place(anchor="w",relx=0.075,rely=(0.2+0.04*name))

        globals()["namedel{}".format(name)] = Button(font=(FONT,"18"), text=X, fg=FG, bg="maroon", bd=0, width=3, )
        globals()["namedel{}".format(name)].place(anchor="w",relx=0.02,rely=(0.2+0.04*name))

def ClearSort(): # Clear groups value input func
    shuffleinput.delete(0, "end")
    print("clear sort")

def ClearGroups(): # Clear groups render func
    print("clear groups")

def EnterKey(): # Enter key event func
    if addinput.get() != "":
        Add()
        print("[enter] ADD")
    elif shuffleinput.get() != "":
        Sort()
        print("[enter] SORT")

def EscapeKey(): # Escape key event func
    if addinput.get() != "":
        addinput.delete(0, "end")
        print("[esc] CLEAR ADD")
    elif shuffleinput.get() != "":
        shuffleinput.delete(0, "end")
        print("[esc] CLEAR SORT")
    #elif  != "":
        #print("[esc] CLEAR GROUPS")

def Sort(): # Sort names list into groups func
    try:
        groups = int(shuffleinput.get())
        shuffleinput.delete(0, "end")
    except:
        shuffleinput.delete(0, "end")
        print("groups input not int")
        os.system('msg "%username%" Please enter a valid integer')
        return
    if groups > len(names):
        os.system('msg "%username%" Groups is greater than amount of names')
        print("groups > list")
        return
    print("sort",groups)

    NameToGroupList = []  # Clear list
    AmtPerGroup = (len(names) // groups)
    Remainder = (len(names) - AmtPerGroup * groups)
    # Add sufficient base amounts of group numbers into NameToGroupList
    for i in range(0, AmtPerGroup):
        for z in range(0, groups):
            NameToGroupList.append(z + 1)
    # Add remaining amount of group numbers to NameToGroupList
    for u in range(0, Remainder):
        NameToGroupList.append(u + 1)

    # Shuffle Groups list 10-50 times (just for added randomness)
    for i in range(0, random.randint(10, 50)):
        random.shuffle(NameToGroupList)

    # Display groups and corresponding players
    for i in range(0, groups):
        print("─" * 8)
        print("Group {}: ({})".format(i + 1, NameToGroupList.count(i + 1)))
        for p in range(0, len(NameToGroupList)):
            if NameToGroupList[p] == i + 1:
                print(names[p])
    print("─" * 8)




# LEFT SECTION
addinput          = Entry   (font=(FONT,"16"),fg=FG,bg=BG,bd=0); addinput.place(height=48,width=220,relx=0.01,rely=0.02,anchor="nw")
addbutton         = Button  (font=(FONT,"14","bold"),text="Add",fg=FG,bg="forestgreen",bd=0,command=Add).place(height=48,width=60,relx=0.32,rely=0.02,anchor="nw")
clearinputbutton  = Button  (font=(FONT,"14","bold"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearInput).place(height=48,width=60,relx=0.408,rely=0.02,anchor="nw")

nameslabel        = Label   (font=(FONT,"14","bold"),text="Names:",fg=FG,bg=BG,bd=8).place(height=48,width=120,relx=0.01,rely=0.11,anchor="w")
clearnamesbutton  = Button  (font=(FONT,"14","bold"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearList).place(height=48,width=72,relx=0.185,rely=0.11,anchor="w")

# RIGHT SECTION
shuffleinput      = Entry   (font=(FONT,"32"),justify="center",fg=FG,bg=BG,bd=0); shuffleinput.place(height=48,width=72,relx=0.55,rely=0.02,anchor="nw")
shufflebutton     = Button  (font=(FONT,"24","bold"),text="SHUFFLE",fg=FG,bg="blue4",bd=0,command=Sort).place(height=48,width=168,relx=0.6545,rely=0.02,anchor="nw")
clearsortbutton   = Button  (font=(FONT,"14","bold"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearSort).place(height=48,width=60,relx=0.895,rely=0.02,anchor="nw")

groupslabel       = Label   (font=(FONT,"14","bold"),text="Groups:",fg=FG,bg=BG,bd=8).place(height=48,width=120,relx=0.55,rely=0.11,anchor="w")
cleargroupsbutton = Button  (font=(FONT,"14","bold"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearList).place(height=48,width=72,relx=0.725,rely=0.11,anchor="w")


root.bind('<Return>', lambda event:EnterKey()) # ENTER key functionality
root.bind('<Escape>', lambda event:EscapeKey()) # ESC key functionality

RenderNames()


root.mainloop() # end of tk
