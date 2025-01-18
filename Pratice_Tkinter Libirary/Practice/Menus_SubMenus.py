from tkinter import *

root = Tk()

def myFun():
    print("Hello This is Menus File")

root.geometry("733x566")

# --> 👇👇👇 Making the non drop down menu
# mymenus = Menu(root)
# mymenus.add_command(label="File",command=myFun)
# mymenus.add_command(label="Exit",command=quit)
# root.config(menu=mymenus)

# --> Main Menus 
yourmenuBar = Menu(root)
m1 = Menu(yourmenuBar,tearoff=0) # --> tearoff = 1 display ------ or tearoff = 0 not display ------ 

# --> Sub Menus 
m1.add_command(label="Project",command=myFun)
m1.add_command(label="Save",command=myFun)
m1.add_separator() # --> Seperator Line
m1.add_command(label="Save As",command=myFun)
m1.add_command(label="Print",command=myFun)
root.config(menu=yourmenuBar) # --> Display on your GUI Form

yourmenuBar.add_cascade(label="File",menu=m1) # --> Name of main menu 

root.mainloop()