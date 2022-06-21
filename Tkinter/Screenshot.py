from tkinter import *
from mss import mss
# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Dev_DesktopRelated/Tkinter/installer/Clown.ico')
root.geometry("500x500")

def shot():
	with mss() as sct:
		# Descgnate the file name and its location
		filename = sct.shot(output="D:/DEV/Dev_DesktopRelated/Tkinter/images/T_shot.png")
		my_label.config(text="Screenshot taken")

my_button = Button(root, text="Screen Shot", command=shot)
my_button.pack(pady=30)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()