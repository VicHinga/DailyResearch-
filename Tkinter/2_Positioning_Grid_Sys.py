from tkinter import *

# Everything is a widget

# You first create the window
root = Tk()

# Creating a text label
myLabel1 = Label(root, text="Second Tkinter code")
myLabel2 = Label(root, text="Third Tkinter code")
myLabel3 = Label(root, text=" Forth Tkinter code")

# Shovimg it onto a screen
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=2, column=3)

root.mainloop()