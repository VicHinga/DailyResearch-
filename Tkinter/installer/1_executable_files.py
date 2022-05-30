from tkinter import *


# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("300x200")

def myclick():
	hello = 'Hello ' + e.get()
	mylabel = Label(root, text=hello)
	e.delete(0, 'end')
	mylabel.pack(pady=10)

e = Entry(root, width=50, font=('Helvetica',30))
e.pack(padx=10, pady=10)
 
myButton = Button(root, text='Enter Your Name', command=myclick)
myButton.pack(pady=10) 

root.mainloop()