from tkinter import *  # tkinter library
import os

### UI Theme Colours
BaseBG      = "grey16"
BG          = "grey30"
FG          = "grey80"
FONT        = "Calibri"



root = Tk()
root.title("Group Sorter [Rev. III]") # window title
root.resizable(False, False) # disable window resizing
root.geometry("720x960") # window size (3:4 aspect-ratio [3]x240,[4]x240)
root.configure(bg=BaseBG) # background colour
border = Label(bg=BG).place(height=922,width=3,relx=0.52,rely=0.5,anchor="center")


global names
names=[]

def Add():
    adding=addinput.get()
    addinput.delete(0, "end")
    if len(adding) == 0:
        print("input empty")
        return
    elif len(adding) not in range(2,21):
        os.system('msg "%username%" Invalid input length, enter between 2-20')
    elif len(names) >=30:
        os.system('msg "%username%" Maximum names reached')
    else:
        names.append(adding)
        print("input added")
        print(names)

def ClearInput():
    addinput.delete(0, "end")
    print("input cleared")

def ClearList():
    print("")

def Sort():
    print("sort TBD")

def ClearSort():
    print("clear sort TBD")



addinput            = Entry     (font=(FONT,"16"),fg=FG,bg=BG,bd=0); addinput.place(height=48,width=220,relx=0.01,rely=0.02,anchor="nw")
addbutton           = Button    (font=(FONT,"14"),text="Add",fg=FG,bg="forestgreen",bd=0,command=Add).place(height=48,width=60,relx=0.32,rely=0.02,anchor="nw")
clearbutton         = Button    (font=(FONT,"14"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearInput).place(height=48,width=60,relx=0.408,rely=0.02,anchor="nw")

nameslabel          = Label     (font=(FONT,"14"),text="Names:",fg=FG,bg=BG,bd=8).place(height=48,width=120,relx=0.01,rely=0.11,anchor="w")
clearnamesbutton    = Button    (font=(FONT,"14"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearInput).place(height=48,width=72,relx=0.185,rely=0.11,anchor="w")


sortinput           = Entry     (font=(FONT,"32"),justify="center",fg=FG,bg=BG,bd=0); sortinput.place(height=48,width=72,relx=0.55,rely=0.02,anchor="nw")
sortbutton          = Button    (font=(FONT,"24"),text="SORT",fg=FG,bg="blue4",bd=0,command=Sort).place(height=48,width=160,relx=0.66,rely=0.02,anchor="nw")
clearbutton         = Button    (font=(FONT,"14"),text="Clear",fg=FG,bg="maroon",bd=0,command=ClearInput).place(height=48,width=60,relx=0.895,rely=0.02,anchor="nw")

groupslabel         = Label     (font=(FONT,"14"),text="Groups:",fg=FG,bg=BG,bd=8).place(height=48,width=120,relx=0.55,rely=0.11,anchor="w")





root.bind('<Return>', lambda event:Add()) # calculate when press ENTER

#####add_input           = Entry(); add_input.place(relx=0.5,rely=0.2,anchor="center")










root.mainloop()