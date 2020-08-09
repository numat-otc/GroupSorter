#Library imports and variable setups
import tkinter as tk
WINDOW = tk.Tk()
WINDOW.title("Team Generator")

def sort():
    print("TBD")


def addtextname():
    print("TBD")

def namesprintout():
    print("TBD")

lbl=tk.Label(WINDOW, text="Team Generator!", fg='purple', bg='turquoise', font=('Verdana', 60)).place(anchor='center')
exit = tk.Button(WINDOW, text="X", fg="red", width=2, height=1,font=('Verdana', 18), command=WINDOW.destroy).grid(row=0, column=0)

addplayer = tk.Button(WINDOW, text="ADD", command=addtextname())


WINDOW.state('zoomed')
addplayer.grid()
WINDOW.mainloop()
