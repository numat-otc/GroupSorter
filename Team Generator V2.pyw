import tkinter as tk

WINDOW = tk.Tk()


def helloCallBack():
    print("TBD")


def addtextname():
    print("bruh")


exit = tk.Button(WINDOW, text="EXIT", fg="red", command=WINDOW.destroy)
addplayer = tk.Button(WINDOW, text="ADD", command=addtextname())


WINDOW.state('zoomed')
exit.pack()
addplayer.pack()
WINDOW.mainloop()
