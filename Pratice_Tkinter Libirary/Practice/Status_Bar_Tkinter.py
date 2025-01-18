from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Status Bar Tutorial")

# def Update():
#     statusVar.set("Busy..")
#     sbar.update()
#     import time
#     time.sleep(2)
#     statusVar.set("Ready Again")

# # --> 👇👇👇 Single Element in status bar 
# statusVar = StringVar()
# statusVar.set("Ready")
# sbar = Label(root,textvariable=statusVar,relief=SUNKEN,anchor="w")
# sbar.pack(side=BOTTOM,fill=X)

# Button(root,text="Upload",command=Update).pack()

def Update():
    statusVar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusVar.set("Ready Again")
    statusVar2.set("Rest")
#  --> 👇👇👇 Multiple Element in status bar 
    
statusVar = StringVar()
statusVar2 = StringVar()
statusVar.set("Ready")
statusVar2.set("Working")

statusFrame = Frame(root,bd=1,relief=SUNKEN)
statusFrame.pack(side=BOTTOM,fill=X)


sbar = Label(statusFrame,textvariable=statusVar,relief=SUNKEN)
sbar.pack(side=LEFT)

sbar2 = Label(statusFrame,textvariable=statusVar2,relief=SUNKEN)
sbar2.pack(side=LEFT)

Button(root,text="Upload",command=Update).pack()

root.mainloop()