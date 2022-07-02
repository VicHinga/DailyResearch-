from tkinter import *
import pybase64
from tkinter import messagebox

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Dev_DesktopRelated/Tkinter/installer/Clown.ico')
root.geometry("500x500")

def clear():
	# Clear boxes
	my_text.delete(1.0, END)
	my_entry.delete(0, 	END)

def encrypt():
	# Get text from the text box
	secret = my_text.get(1.0, END)
	
	# Password
	if my_entry.get() == "endec":
		my_text.delete(1.0, END)
		# Clear Screen
		my_entry.delete(0, END)
		# Convert to byte
		secret = secret.encode("ascii")
		# Convert to base64
		secret = pybase64.b64encode(secret)
		# Convert to ascii
		secret = secret.decode("ascii")
		# Print text box
		my_text.insert(END, secret)

	else:
		messagebox.showwarning("Incorect Password!")


def decrypt():
	# Get text from the text box
	secret = my_text.get(1.0, END)
	my_text.delete(1.0, END)
	# Password
	if my_entry.get() == "endec":

		# Clear Screen
		my_entry.delete(0, 	END)
		# Convert to byte
		secret = secret.encode("ascii") 
		# Convert to base64
		secret = pybase64.b64decode(secret)
		# Convert to ascii
		secret = secret.decode("ascii")
		# Print text box
		my_text.insert(END, secret)		

	else:
		messagebox.showwarning("Incorect Password!")
		
	


my_frame = Frame(root)
my_frame.pack(pady=20)  

enc_button = Button(my_frame, text="Encrypt", font=("Helvetica", 18), command=encrypt)
enc_button.grid(row=0, column=0)

dec_button = Button(my_frame, text="Decrypt", font=("Helvetica", 18), command=decrypt)
dec_button.grid(row=0, column=1)

clear_button = Button(my_frame, text="Clear", font=("Helvetica", 18), command=clear)
clear_button.grid(row=0, column=2)

enc_label = Label(root, text="Encrypt or Decrypt text...", font=("Helvetica", 15))
enc_label.pack()

my_text = Text(root, width=57, height=10)
my_text.pack(pady=10)

pas_label = Label(root, text="Enter Password...\n Hint(endec)", font=("Helvetica", 15))
pas_label.pack()

my_entry = Entry(root, font=("Helvetica", 15), width=35, show="*")
my_entry.pack(pady=10)

root.mainloop()