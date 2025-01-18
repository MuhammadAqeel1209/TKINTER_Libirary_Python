from tkinter import *

root = Tk()

root.geometry("644x344")

Label(root,text="Bismillah Travel Agency",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
# --> Label Making Data Write
name        = Label(root,text="Name")
phone       = Label(root,text="Phone")
gender      = Label(root,text="Gender")
emergency   = Label(root,text="Emergency Contact")
paymentMode = Label(root,text="PaymentMode")

# --> grid used to data Show on the GUI Form like Matrix or Excel Sheet
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentMode.grid(row=5,column=2)

# --> Making Varaiable
nameVal = StringVar()
phoneVal = StringVar()
genderVal = StringVar()
emergencyVal = StringVar()
paymentModeVal = StringVar()
foodServices = IntVar()

# --> Making Entry Widget --> Make Table where we write data 
nameentry = Entry(root,textvariable=nameVal).grid(row=1,column=3)
phoneentry = Entry(root,textvariable=phoneVal).grid(row=2,column=3)
genderentry = Entry(root,textvariable=genderVal).grid(row=3,column=3)
emergencyentry = Entry(root,textvariable=emergencyVal).grid(row=4,column=3)
paymentModeentry = Entry(root,textvariable=paymentModeVal).grid(row=5,column=3)

# Check Button In the Form of 1(Yes) or 0(No)
food = Checkbutton(text="Do You want the any meals",variable=foodServices)
food.grid(row=6,column=3)

# --> Making Function Use In Button --> Command
def GetData():
    print(f"Name is {nameVal.get()}")
    print(f"Phone is {phoneVal.get()}")
    print(f"Gender is {genderVal.get()}")
    print(f"EmergencyContact is {emergencyVal.get()}")
    print(f"PaymentMode is {paymentModeVal.get()}")
    print(f"FoodServices is {foodServices.get()}")

# --> Making Button 
ButtonSubmit = Button(text="Submit ",command=GetData).grid(row=8,column=3)

root.mainloop()