from tkinter import *
import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image

def import_image():
    global filename
    filename = filedialog.askopenfilename ()
    print("Selected: ", filename)
    global image
    image = ImageTk.PhotoImage(Image.open(filename))
    place_image()

def place_image():
    label1 = tkinter.Label(image=image)
    label1.pack()
def save_image():
    print("Saved")
def save_image_as(new_file_name):
    print("Saved As " + new_file_name)
def button_command():
    print("This button works")
root = tkinter.Tk()
#menus at top of program
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Import', command = import_image)
file_menu.add_command(label='Save', command= save_image)
file_menu.add_command(label='Save As', command= save_image_as("x"))
file_menu.add_separator()
file_menu.add_command(label='Exit', command= root.destroy,)
menubar.add_cascade(label="File", menu=file_menu,underline=0,)
edit_menu = Menu(menubar)
edit_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu = edit_menu,underline = 0)
view_menu = Menu(menubar)
view_menu = Menu(menubar, tearoff =False)
menubar.add_cascade(label="View", menu = view_menu, underline = 0)

frame = Frame(root)
frame.grid()

#slider 
Slider = Scale(from_=0, to=10 ,orient=HORIZONTAL)
Slider.grid(column = 9,columnspan=10, row = 0, rowspan = 10)

#canvas
canvas = Canvas(frame,bg='blue', width = 192,height = 108)
canvas.pack_configure(padx = 0,pady=(0,0))

#buttons
But = tkinter.Button(frame, text ="Hello", command = button_command)






root.geometry('500x300')
root.mainloop()

print("Merge")