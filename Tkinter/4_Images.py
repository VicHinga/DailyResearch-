from tkinter import *
from PIL import ImageTk,Image

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/Clown.ico')

img = ImageTk.PhotoImage(Image.open('idtop.jpg'))
label_1 = Label(image=img)
label_1.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()



root.mainloop()