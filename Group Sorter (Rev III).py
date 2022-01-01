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

global names
names=[]

def Add():
    adding=addinput.get()
    addinput.delete(0, "end")
    if len(adding) == 0:
        return
    elif len(adding) not in range(2,21):
        os.system('msg "%username%" Invalid input length, enter between 2-20')
    else:
        names.append(adding)
        print("added")
        print(names)

def Clear():
    addinput.delete(0, "end")
    print("cleared")



addinput            = Entry(root, font=(FONT,"18"),textvariable="enter",fg="grey80",bg="grey30",bd=0); addinput.place(height=32,width=242,relx=0.01,rely=0.05,anchor="w")
addbutton           = Button(root, font=(FONT,"13"),text="Add",bg="green2",bd=0,command=Add).place(relx=0.35,rely=0.05,anchor="w")
clearbutton         = Button(root, font=(FONT,"13"),text="Clear",bg="brown2",bd=0,command=Clear).place(relx=0.405,rely=0.05,anchor="w")

list_text           = Label(font=("Calibri 14"),text="Names:",justify="left",fg="grey80",bg="grey30",bd=8).place(relx=0.01,rely=0.08,anchor="nw")

list_text           = Label(font=("Calibri 14"),text="Groups:",justify="left",fg="grey80",bg="grey30",bd=8).place(relx=0.6,rely=0.05,anchor="w")


root.bind('<Return>', lambda event:Add()) # calculate when press ENTER

#####add_input           = Entry(); add_input.place(relx=0.5,rely=0.2,anchor="center")










root.mainloop()