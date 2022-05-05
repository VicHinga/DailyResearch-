from tkinter import *

# Everything is a widget

# You first create the window
root = Tk()

# Creating a text label
myLabel = Label(root, text="First Tkinter code")

# Shovimg it onto a screen
myLabel.pack()

root.mainloop()