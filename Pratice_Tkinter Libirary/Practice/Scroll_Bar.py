from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Scroll Bar Tutorial")

#For Scroll bar connecting to widget
# 1) widget(yscrollbarCommand= scrollbar.set) # --> Widget = listbox,text,label etc 
# 2) scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set) -->1
# for i in range(344):
#      listbox.insert(END, f"Item {i}")

# listbox.pack(fill="both",padx=22,pady=22)
# text = Text(root, yscrollcommand = scrollbar.set) -->1
# text.pack(fill=BOTH)
# scrollbar.config(command=listbox.yview) -->2
# scrollbar.config(command=text.yview) -->2


root.mainloop()