from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.geometry("733x566")
root.title("Slider Tutorial")

# def getDollar():
#     tmsg.showinfo("Winning Dollar",f"We have credited {mySlider2.get()} dollar to your bank account")

# # mySlider = Scale(root,from_= 0, to=100)
# # mySlider.pack()

# Label(text="How many dollar you want?").pack()

# mySlider2 = Scale(root,from_= 0, to=100,orient=HORIZONTAL)
# mySlider2.set(35)
# mySlider2.pack()
# Button(text="Get Dollars",command=getDollar,padx=20,pady=8).pack()


def Rating():
    if(nameVar.get() == ""):
        tmsg.showerror("Error","Plz Enter Your Name")
    else:    
        with open("Rate_File.txt","a") as File: 
            #  -->data write in the file 👇👇👇
            File.write(f"Thank You for Your Rating\n {nameVar.get()} Shab has {ratingSlides.get()} % Rate us\n")
           # --> show the msg box  👇👇👇
        tmsg.showinfo("Rating",f"Thank You for Your Rating\n {nameVar.get()} Shab has {ratingSlides.get()} % Rate us")
        name.delete(0,END)
    

Label(root,text="Rate us at our hotel").pack()
Label(root,text= "Name").pack()
nameVar = StringVar()
name = Entry(root,textvariable=nameVar)
name.pack()
name.focus_set()


ratingSlides = Scale(root,from_=0,to=10,orient=HORIZONTAL)
ratingSlides.pack()
Button(text= "Rate us",command=Rating).pack()

root.mainloop()