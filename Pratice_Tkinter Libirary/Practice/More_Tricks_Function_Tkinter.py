from tkinter import *

root = Tk()
root.geometry("655x344")
root.title("My GUI")
root.wm_iconbitmap("GUI.ico")
root.configure(background="yellow")


width = root.winfo_width()
heigth = root.winfo_height()

print(f"{width}x{heigth}")
Button(text="close",command=root.destroy).pack()
root.mainloop()