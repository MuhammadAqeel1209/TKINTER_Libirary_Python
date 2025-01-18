from tkinter import *
import tkinter.messagebox  as tmsg

root = Tk()

root.title("Radio Button Tutorial")

def Order():
    # --> Message box
    tmsg.showinfo("Order Received",f"We have received you order for {var.get()}\n Thank For Order")

var = StringVar()


Label(root,text="What would you like to have sir?",font="lucida 18 bold",justify=LEFT,padx=14).pack()

Radiobutton(root,text="Pizza",variable=var,value="Pizza").pack(anchor="w")
Radiobutton(root,text="Burger",variable=var,value="Burger").pack(anchor="w")
Radiobutton(root,text="Paratha",variable=var,value="Parathe").pack(anchor="w")
Radiobutton(root,text="Bar B Q",variable=var,value="Bar B Q").pack(anchor="w")

Button(text="Order Place",command=Order).pack()

root.geometry("455x334")
root.mainloop()