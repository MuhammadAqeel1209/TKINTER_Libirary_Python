from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("List Box Tutorial")

def Add():
    global i
    listItem = ["Bread","Pizza","Burger","Sandwich","IceCream"]
    lbx.insert(ACTIVE,listItem[i])
    i += 1
def GetValue():
    index = lbx.curselection()
    print(lbx.get(index))

i = 0
lbx = Listbox(root)
lbx.grid(row=0,column=1)
lbx.insert(END,"First Item Of List Box")

Button(text="Add Item",command=Add).grid(row=2,column=1)
Button(text="Print value",command=GetValue).grid(row=3,column=2)


root.mainloop()