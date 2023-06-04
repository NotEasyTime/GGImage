from tkinter import *
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image

def import_image():
    global filename
    filename = filedialog.askopenfilename ()
    print("Selected: ", filename)
    global image
    image = ImageTk.PhotoImage(Image.open(filename))


root = Tk()

root.mainloop()

print("Merge")
print("Help")