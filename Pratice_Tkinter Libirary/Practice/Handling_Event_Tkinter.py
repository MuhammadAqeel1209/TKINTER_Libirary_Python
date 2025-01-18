from tkinter import *
root = Tk()
root.geometry("644x344")

def Aqeel(event):
    print(f"You Click On the Button at {event.x} and {event.y}")

def Button2(event):
    print("You Click on Button 2") 

def Btn3(event):
    print("You Click on Btn 3")

def Btn4(event):
    print("You Click on Btn 4") 

def Btn5(event):
    print("You Click on Btn 5") 

def key_press(event):
    print("Key Pressed: " + event.char)

def mouse_enter(event):
    print("Mouse Entered!")

def mouse_leave(event):
    print("Mouse Left!")

root.title("Event In Tkinter")

Widget = Button(root,text="Click Here ",bg="Green")
Widget.pack()

Widget.bind('<Button-1>',Aqeel)
Widget.bind('<Double-1>',quit)
root.bind(' <Button-2>',Button2)
root.bind(' <Button-3>',Btn3)
root.bind(' <Button-4>',Btn4)
root.bind(' <Button-5>',Btn5)
# # Bind key events
# Widget.bind("<KeyPress>", key_press)

# # Bind mouse events
# Widget.bind("<Enter>", mouse_enter)
# Widget.bind("<Leave>", mouse_leave)

 
root.mainloop()

#https://www.tutorialspoint.com/list-of-all-tkinter-events
#https://python-course.eu/tkinter/events-and-binds-in-tkinter.php