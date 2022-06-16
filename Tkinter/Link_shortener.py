from tkinter import *
import pyshorteners

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("600x500")

def shorten():
	if short_entry.get():
		short_entry.delete(0, END)
	if my_entry.get():
		url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
		short_entry.insert(END, url)


my_label = Label(root, text="Enter Link to shorten", font=('Helvetica', 34))
my_label.pack(pady=20)

my_entry = Entry(root, font=('Helvetica', 20))
my_entry.pack(pady=20)

my_button = Button(root, text="Shorten a URL", command=shorten, font=('Helvetica', 15))
my_button.pack(pady=20)

short_label = Label(root, text="Shortened URL", font=('Helvetica',15))
short_label.pack(pady=40)

short_entry = Entry(root, font=('Helvetica', 10), justify=CENTER, width=50)
short_entry.pack(pady=10)

root.mainloop() 