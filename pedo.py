from tkinter import *
import tkMessageBox

from tkinter import filedialog

def import_image():
    global filename
    filename = filedialog.askopenfilename ()
    print("Selected: ", filename)


root = Tk()

root.mainloop()

print("Merge")