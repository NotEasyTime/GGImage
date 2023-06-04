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

root = tkinter.Tk()
root.geometry('500x200')
B = tkinter.Button(root, text = "Import Image", command = import_image)
B.pack()
root.mainloop()

print("Merge")