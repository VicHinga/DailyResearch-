from tkinter import *
import pyttsx3 


# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("300x200")

def talk():
	engine = pyttsx3.init()
	# engine.setPrototype('rate', 130)
	voices = engine.setPrototype('voice', voices[1].id)
	engine.say(my_entry.get())
	engine.runAndWait()
	my_entry.delete(0,END)

my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20, padx=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)

root.mainloop()