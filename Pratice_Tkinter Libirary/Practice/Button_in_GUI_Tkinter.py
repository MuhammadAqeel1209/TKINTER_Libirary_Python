from tkinter import *

root = Tk()
root.title("Buttons")
def Hello():
    name = input("Enter your name\t")
    print(f"Name is {name}")
root.geometry("655x333")
farme = Frame(root,borderwidth=6,bg="Black",relief=SUNKEN)
farme.pack(side=RIGHT)

b1 = Button(farme,fg="red",text="Enter You Name",command=Hello) # ---> Command Line --> Write Function Name --> Work By Button # ---> Command Line --> Write Function Name() --> Work Automatically , Not work By button 
b1.pack()


root.mainloop()