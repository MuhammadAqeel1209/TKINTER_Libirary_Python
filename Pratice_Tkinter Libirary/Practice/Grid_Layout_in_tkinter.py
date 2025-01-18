from tkinter import *

def GetInformation():
    print(f"The username is {uservar.get()}")
    print(f"the password is {passvar.get()}")
root = Tk()

root.geometry("655x333")
user = Label(root,text="UserName")
password = Label(root,text="Password")

#Grid is an other method for pack use Like a Excel Sheets and Matrix 
user.grid(row=0,column=0) 
password.grid(row=1,column=0)

#4 Types of Varaiable classes in Tkinter -->1)Bolean var,2)Double var,3)Int Var,4)String Var

uservar = StringVar()
passvar = StringVar()

userentry = Entry(root,textvariable=uservar)
passentry = Entry(root,textvariable=passvar)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

b1 = Button(root,text="Submit",command=GetInformation) # ---> Command Line --> Write Function Name --> Work By Button # ---> Command Line --> Write Function Name() --> Work Automatically , Not work By button 
b1.grid()

root.mainloop()