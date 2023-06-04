from tkinter import *
import tkinter




from tkinter import filedialog
import PIL
from PIL import ImageTk, Image

def import_image():
    global filename
    filename = filedialog.askopenfilename ()
    print("Selected: ", filename)
    global image
    image = ImageTk.PhotoImage(Image.open(filename))


root = tkinter.Tk()
B = tkinter.Button(root, text = "Import Image", command = import_image)

B.pack()
root.mainloop()

print("Merge")