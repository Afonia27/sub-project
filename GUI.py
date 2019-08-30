from tkinter import *
import tkinter.font
from PIL import Image
from PIL import ImageTk

def exit(event):
    win.destroy()

win =Tk()
win.title("Main Window")
w,h = win.winfo_screenwidth(), win.winfo_screenheight()
image1 = Image.open("/home/pi/Desktop/Project/sub.jpg")
background_image = ImageTk.PhotoImage(image1)
background_label =tkinter.Label(win,image = background_image)
background_label.place(x=0,y=0, relwidth = 1, relheight = 1)
win.wm_geometry("%dx%d+0+0" % (w,h))
win.bind("<Escape>",exit)
win.mainloop()