from tkinter import *

root = Tk()

root.geometry("655x333")
frameOne = Frame(root,bg="yellow",borderwidth=6,relief=SUNKEN) # -->Like as Div Tag In HTML
                                # 👇👇👇 --> Give Space Vertically
frameOne.pack(side=RIGHT,fill=Y,pady=50) # --> Fill --> Move to that Direction where we want --> Like Y Move in Vertically

frameTwo = Frame(root,bg="grey",borderwidth=9,relief=SUNKEN)
frameTwo.pack(side=TOP,fill=X )  # --> Fill --> Move to that Direction where we want --> Like X Move in Horizontal
                                        # 👇👇👇 --> Give Space Horizontal
LabelOne = Label(frameTwo,text="ProjectOne",padx=23)
LabelOne.pack()

labelTwo = Label(frameOne,text="ProjectTwo",pady=23)
labelTwo.pack()
root.mainloop()