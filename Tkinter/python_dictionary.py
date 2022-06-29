from tkinter import *
from PyDictionary import PyDictionary 
# This app gets system info.

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Dev_DesktopRelated/Tkinter/installer/Clown.ico')
root.geometry("600x600")

def lookup():
	# Clear text inside my text
	my_text.delete(1.0, END)

	# Lookup a word
	dictionary = PyDictionary()
	defination = dictionary.meaning(my_entry.get())

	#Defination comes with keys(Noun, verb) and values(diff use of word)
	for key,value in defination.items():
		my_text.insert(END, f'< {key} >\n\n' )
		
		for values in value:
			my_text.insert(END, f'-> {values}\n\n') 


my_labelframe = LabelFrame(root, text="Enter Word", font=('Helvetica', 25))
my_labelframe.pack(pady=20)

# Grid if object is to appear inside LabelFrame
my_entry = Entry(my_labelframe, font=('Helvetica', 20))
my_entry.grid(row=0, column=0, padx=15, pady=10)

my_button = Button(my_labelframe, text="Look Up", command=lookup)
my_button.grid(row=0, column=1, padx=15, pady=10)

# wrap so that words can move to nest line in readable manner
my_text = Text(root, height=20, width=65, wrap=WORD)
my_text.pack(pady=10)

root.mainloop()