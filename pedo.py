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
root.geometry('500x300')

B = tkinter.Button(root, text = "Import Image", command = import_image)
B.pack()

temp = tkinter.Button(root, text = "Image Array", command = image_to_list)
temp.pack()

root.mainloop()
