from tkinter import *
from tkinter import ttk

root = Tk()
frame = Frame(root)
frame.grid(row=1,column=3,sticky="news",padx=25,pady=25)

data = Spinbox(frame,from_=12 ,to = "infinity")
data.grid()

data2 = Spinbox(frame,from_=1 ,to = 30)
data2.grid()

data3 = Spinbox(frame,from_=20 ,to = 70)
data3.grid()


# --> Together padding in frame all widget
for widget in frame.winfo_children():
    widget.grid_configure(padx=20,pady=15)


root.mainloop()