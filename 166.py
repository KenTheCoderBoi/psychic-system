
from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Working On Canvas Using Functions")
root.geometry("600x600")


color_label=Label(root, text="Enter a Color :")
color_label.place(relx=0.1,rely=0.95, anchor= CENTER)
input_box = Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.3,rely=0.95, anchor= CENTER)

color_label2=Label(root, text="enter starting x")
color_label2.place(relx=0.7,rely=0.85, anchor= CENTER)
input_boxstartx = Entry(root)
input_boxstartx.insert(0,50)
input_boxstartx.place(relx=0.9,rely=0.85, anchor= CENTER)

input_boxwaste = Entry(root)
input_boxwaste.place(relx=0.8,rely=0.95, anchor= CENTER)

color_label3=Label(root, text="enter starting y")
color_label3.place(relx=0.30,rely=0.85, anchor= CENTER)
input_boxstarty = Entry(root)
input_boxstarty.insert(0,50)
input_boxstarty.place(relx=0.52,rely=0.85, anchor= CENTER)

color_label4=Label(root, text="enter end x")
color_label4.place(relx=0.7,rely=0.9, anchor= CENTER)
input_boxendx = Entry(root)
input_boxendx.insert(0,50)
input_boxendx.place(relx=0.9,rely=0.9, anchor= CENTER)

color_label5=Label(root, text="enter end y")
color_label5.place(relx=0.30,rely=0.9, anchor= CENTER)
input_boxendy = Entry(root)
input_boxendy.insert(0,50)
input_boxendy.place(relx=0.52,rely=0.9, anchor= CENTER)

canvas=Canvas(root, width = 590, height=500, bg = "white", highlightbackground="lightgray")
canvas.pack()



oldx=50
oldy=50
newx=50
newy=50
def circle(event):
    global oldx
    global oldy
    global newx
    global newy
    oldy=input_boxstartx.get()
    oldy=input_boxstarty.get()
    newx=input_boxendx.get()
    newy=input_boxendy.get()
    keypress="c"
    draw(oldx,oldy,newx,newy,keypress)
def rectangle(event):
    global oldx
    global oldy
    global newx
    global newy
    oldy=input_boxstartx.get()
    oldy=input_boxstarty.get()
    newx=input_boxendx.get()
    newy=input_boxendy.get()
    keypress="r"
    draw(oldx,oldy,newx,newy,keypress)
def line(event):
    global oldx
    global oldy
    global newx
    global newy
    oldy=input_boxstartx.get()
    oldy=input_boxstarty.get()
    newx=input_boxendx.get()
    newy=input_boxendy.get()
    keypress="lc"
def draw(oldx,oldy,newx,newy,keypress):
    color=input_box.get()
    if(keypress=="c"):
            canvas.create_oval(oldx,oldy,newx,newy,width=3,fill=color)
    if(keypress=="r"):
            canvas.create_rectangle(oldx,oldy,newx,newy,width=3,fill=color)
    if(keypress=="l"):
            canvas.create_line(oldx,oldy,newx,newy,width=3,fill=color)
root.bind("<c>",circle)
root.bind("<l>",line)
root.bind("<r>",rectangle)
root.mainloop()



