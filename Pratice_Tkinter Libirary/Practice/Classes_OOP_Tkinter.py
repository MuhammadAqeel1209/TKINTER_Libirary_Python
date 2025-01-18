from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    def Status(self):
        self.var = StringVar()
        self.var.set('Ready')   
        self.statusBar = Label(self,textvariable=self.var,relief=SUNKEN,anchor="w") 
        self.statusBar.pack(side=BOTTOM,fill=X)
    
    def Update(self):
        self.var.set("Click Button")

    def ClickButton(self,text):
        Button(self,text=text,command=self.Update).pack()
if __name__ == "__main__":
    window = GUI()
    window.Status()
    window.ClickButton("Click it")
    window.mainloop() 
