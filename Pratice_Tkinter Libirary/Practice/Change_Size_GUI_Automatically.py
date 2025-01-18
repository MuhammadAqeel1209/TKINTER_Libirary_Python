from tkinter import *

root = Tk()

root.geometry("634x334")
root.title("Window Resizer Automatically")

def ChangeGUI():
    root.geometry(f"{widthVar.get()}x{heightVar.get()}")
    widthEntry.delete(0,END)
    heightEntry.delete(0,END)

def move_to_next(event): # --> We Click the "Enter" button to move next Entry in the form 
    event.widget.tk_focusNext().focus() 

Label(text="Window Resizer",font="Algerain 12 bold").grid(row=0,column=3)

width = Label(text="Width",pady=10).grid(row=1,column=1)
height = Label(text="Height").grid(row=2,column=1)

widthVar = StringVar()
heightVar = StringVar()

widthEntry = Entry(root,textvariable=widthVar)
widthEntry.grid(row=1,column=2)
widthEntry.focus_set() # Set Cursor at first entry widget 
widthEntry.bind("<Return>",move_to_next)

heightEntry = Entry(root,textvariable=heightVar)
heightEntry.grid(row=2,column=2)
heightEntry.bind("<Return>",move_to_next)


Button(text="Submit Height and Width",command=ChangeGUI).grid(row=3,column=2)

root.mainloop()