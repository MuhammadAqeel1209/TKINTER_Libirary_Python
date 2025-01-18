from tkinter import *


#For PIL First you install --> 👉 "pip install pillow"
from PIL import Image,ImageTk # help to take jpeg file in tkinter

my_Root = Tk()  #👈 instance of Tk class and make basic Graphic user iterface (GUI)

#syntax of my_Root.geometery 👉 -->(widthxheight)
#my_Root.geometry("365x334") #👈 Set the width and height 
# important note 👉-->when we run the progarm window show as a size of geometry

my_Root.title("My GUI") #-->👉Change the title of GUI

#syntax of my_Root.minimsize 👉 -->(widthxheight)
my_Root.minsize(400,150) #👈 Set the width and height for minimum size of window

#syntax of my_Root.maxsize 👉 -->(widthxheight)
#my_Root.maxsize(1200,1500) #👈 Set the width and height for maximum size of window

#Label method 👉 --> for text 
myLabel1 = Label(text="Welcome to VS CODE", font="Cascadia 16 bold", height=1, fg='black') 
myLabel = Label(text="Assalam u alaikum! I am Aqeel",font="Algerain 16 bold",height=5)
myLabel1.pack()
myLabel.pack() #Pack use for 👉 --> write the text on window screen of GUI

# for single png photos 👇👇👇
# photo = PhotoImage(file = "TkinterBasicPic/spider.png") #get the photo from your folder
# photo_Label = Label(image=photo) # label method also use 👉 --> for upload the picture
# photo_Label.pack() #Pack also use for 👉 --> upload the photo on windoe screen of GUI

#For multiple png Photos 👇👇👇
# photopngOne = PhotoImage(file = "TkinterBasicPic/images.png")
# photopngOne_label = Label(image=photopngOne)
# photopngOne_label.pack(side= RIGHT)

# photopngTwo = PhotoImage(file = "TkinterBasicPic/download.png")
# photopngTwo_label = Label(image=photopngTwo)
# photopngTwo_label.pack(side=LEFT)


# for jpg photos 👇👇👇

# pic= Image.open("TkinterBasicPic/two.jpeg") #👉 -->Fist open the image
# picJpg =ImageTk.PhotoImage(pic) #👉 -->using ImageTk module for photo the image
# picJpg_Label = Label(image=picJpg) # label method also use 👉 --> for upload the picture
# picJpg_Label.pack() #Pack also use for 👉 --> upload the photo on windoe screen of GUI

# for multiple jpg photos 👇👇👇

# imageone = Image.open("TkinterBasicPic/Four.jpeg") 
# photoJpg_one =ImageTk.PhotoImage(imageone)
# photo_Jpg_Label_one = Label(image=photoJpg_one) 
# photo_Jpg_Label_one.pack(side=RIGHT) 

# imagetwo = Image.open("TkinterBasicPic/two.jpeg") 
# photoJpg_two =ImageTk.PhotoImage(imagetwo) 
# photo_Jpg_Label_two = Label(image=photoJpg_two) 
# photo_Jpg_Label_two.pack(side=LEFT) 


my_Root.mainloop() #👈 move to event loop and store all logic of your basic GUI