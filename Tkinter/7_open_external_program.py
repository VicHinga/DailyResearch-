from tkinter import *
from tkinter import filedialog
import os

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("300x200")

def open_program():
 	my_prog = filedialog.askopenfilename()
 	my_label.config(text=my_prog)
 	os.system('"%s"' % my_prog)

my_button = Button(root, text="Open Program", command= open_program)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=40)

root.mainloop()