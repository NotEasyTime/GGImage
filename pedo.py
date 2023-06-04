from tkinter import *
import tkinter




from tkinter import filedialog

def import_image():
    global filename
    filename = filedialog.askopenfilename ()
    print("Selected: ", filename)


root = tkinter.Tk()
B = tkinter.Button(root, text = "Import Image", command = import_image)

B.pack()
root.mainloop()

print("Merge")