from tkinter import *
import webbrowser

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("300x300")

# Creating Open Browser Method
def open_browser(e):
	webbrowser.open_new("https://www.google.com/")


# Creating Open Browser Method
def spec_client(e):
	webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open_new("https://www.google.com/")


# Creating a text label
myLabel = Label(root, text="1. Open Default Browser\n2. Open Edge Browser",font=("Helvetica", 20), fg="blue")
myLabel.pack(pady=20)

# Creating a button
mybutton = Button(root, text="Open Web Browser", font=("Helvetica", 20), command=lambda: open_browser(1))
mybutton.pack(pady=20)

# Creating a button
mybutton = Button(root, text="Open Specific Client", font=("Helvetica", 20), command=lambda: spec_client(1))
mybutton.pack(pady=20)


# Shovimg it onto a screen
myLabel.pack()

root.mainloop()