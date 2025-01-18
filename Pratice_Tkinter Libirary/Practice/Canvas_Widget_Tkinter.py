from tkinter import * 

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_Widget = Canvas(root,height=canvas_height,width=canvas_width,bg="White")
can_Widget.pack()

                # -->(x1,y1,x2,y2) 
can_Widget.create_line(12,12,12,12,fill="red") # --> Lines Goes from the point x1 , y1 to x2 ,y2
can_Widget.create_line(0,40,800,0,fill="yellow")

# --> For Creation of rectangle specify parameters --> coordination of top left and coordinate of bottom right
can_Widget.create_rectangle(3,5,700,300,fill="blue")
# can_Widget.create_text(200,200,text="I am working in python ")
# can_Widget.create_oval(344,233,244,355)
can_Widget.create_polygon(50, 50, 150, 50, 200, 100, 150, 150, 50, 150,fill="red")

can_Widget.create_arc(102,202,303,405)


root.mainloop()