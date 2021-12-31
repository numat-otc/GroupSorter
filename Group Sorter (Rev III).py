from tkinter import *  # tkinter library
from tkinter import messagebox

root = Tk()
root.title("Group Sorter [Rev. III]") # window title
root.geometry("720x960") # window size (3:4 aspect-ratio [3]x240,[4]x240)
root.configure(bg='black') # background colour

add_text            = Label(text="Initial investment:").place(relx=0.5,rely=0.1,anchor="center")
add_input           = Entry(); add_input.place(relx=0.5,rely=0.2,anchor="center")
descinput           = Text(font=("Calibri 24"), height=1, width=24, ).place(relx=0.5,rely=0.3,anchor="center")



calculate_button = Button(text="Calculate").place(relx=0.5,rely=0.4,anchor="center") # calculate button





















root.mainloop()