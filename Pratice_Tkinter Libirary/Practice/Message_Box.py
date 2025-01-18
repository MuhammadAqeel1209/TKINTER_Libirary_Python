from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

# --> Function --> use as command in button 

# def myFun():
#     print("Hello This is Menus File")
# def Help():
#           # --> Show Some Special Message 👇👇👇
#     tmsg.showinfo("Help","I will help you")   
# def Rate():
#            # --> Msg Box For Asking Question 👇👇👇
#     value = tmsg.askquestion("Was Your expeience good?", "Using this GUI,was your experience good")    
#     if value == "yes":
#         msg = "Great Rate us on App Store"
#     else:
#         msg = "Tell us you problem we resolve your problem " 
#           # --> Show Some Special Message 👇👇👇   
#     tmsg.showinfo("Message",msg)    

root.geometry("733x566")

# --> Main Menus 👇👇👇
# yourmenuBar = Menu(root)
# m1 = Menu(yourmenuBar,tearoff=0)

#  # --> Sub Menus  👇👇👇
# m1.add_command(label="Project",command=myFun)
# m1.add_command(label="Save",command=myFun)
# m1.add_separator() # --> Seperator Line
# m1.add_command(label="Save As",command=myFun)
# m1.add_command(label="Print",command=myFun)
# root.config(menu=yourmenuBar) # --> Display on your GUI Form

# yourmenuBar.add_cascade(label="File",menu=m1)  # --> Name of main menu

# # --> Next Menu 👇👇👇
# m2 = Menu(yourmenuBar,tearoff=0)
# # --> Sub Menus 👇👇👇
# m2.add_command(label="Cut",command=myFun)
# m2.add_command(label="Copy",command=myFun)
# m2.add_separator() # --> Seperator Line
# m2.add_command(label="Paste",command=myFun)
# m2.add_command(label="Find",command=myFun)
# root.config(menu=yourmenuBar) # --> Display on your GUI Form

# yourmenuBar.add_cascade(label="Edit",menu=m2) # --> Name of main menu

# # --> Next Menu 👇👇👇
# m3 = Menu(yourmenuBar,tearoff=0)
# # --> Sub Menus 👇👇👇
# m3.add_command(label="Help",command=Help)
# m3.add_command(label="Rate Us",command=Rate)

# root.config(menu=yourmenuBar) # --> Display on your GUI Form

# yourmenuBar.add_cascade(label="Help",menu=m3)  # --> Name of main menu

def Error():
    # --> Show Error Message 👇👇👇
    tmsg.showerror("Error","Show Error")

def AskOkCANCEL():
     # --> Ask the question 👇👇👇
    tmsg.askokcancel("Move Forward","Fail in  Level")

def YESNO():
    # Show Ask the Question 👇👇👇
    tmsg.askyesnocancel("Message","Do you want go to lahore?")

b1 = Button(text="Error",command=Error)
b1.pack()

b2 = Button(text="Ask OK CANCEL",command=AskOkCANCEL)
b2.pack()

b3 = Button(text="YES NO",command=YESNO)
b3.pack()

root.mainloop()