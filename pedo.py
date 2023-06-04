from tkinter import *
import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as numpy
from numpy import asarray

list5 = []

def import_image():
    global filename
    filename = filedialog.askopenfilename ()
    print("Selected: ", filename)
    global im
    im = Image.open(filename)
    global wid, hei
    wid, hei = im.size
    print(hei)
    global img
    img = ImageTk.PhotoImage(im)
    place_image()

def place_image():
    label1 = tkinter.Label(image=img)
    label1.pack()
def save_image():
    print("Saved")
def save_image_as(new_file_name):
    print("Saved As " + new_file_name)
def button_command():
    print("This button works")
def image_to_list():
    global whole_image
    global row
    pxl = []
    row = []
    whole_image = []
    for i in range(hei):
        temp = []
        for j in range(wid):
            cor = x, y = j, i
            pixel = im.getpixel(cor)
            temp.append(pixel)
        whole_image.append(temp)
    list_to_array(whole_image)


def list_to_array(list):
    global array_one
    array_one = numpy.array(list, dtype=numpy.uint8)
    #print(array_one)

    filter()

def filter():
    global filtered_array
    filtered_array = array_one
    for i in range(hei):
        for j in range(wid):
            num = array_one[i,j]
            total = 0
            for z in range(3):
                num1 =  num[z]
                total = total + num1
            if total < 300:
                filtered_array[i,j]=(255,255,0)
    #print(filtered_array)
    array_to_image()

def array_to_image():
    new_image = Image.fromarray(array_one)
    new_image.show()
    #label2 = tkinter.Label(image=new_image)
    #label2.pack()


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


temp = tkinter.Button(frame, text = "Image Array", command = image_to_list)
temp.pack_configure(padx = 0,pady=(0,0))

root.mainloop()
