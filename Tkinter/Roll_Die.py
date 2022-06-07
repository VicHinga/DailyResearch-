from tkinter import *
import random 

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("600x400")

def get_number(x):
	if x == '\u2680':
		return(1)
	elif x == '\u2681':
		return(2)
	elif x == '\u2682':
		return(3)
	elif x == '\u2683':
		return(4)
	elif x == '\u2684':
		return(5)
	elif x == '\u2685':
		return(6)

# Roll Die Function
def roll_die():
	d1 = random.choice(my_die)
	d2 = random.choice(my_die)

	# Determine Die Number
	sd1 = get_number(d1)
	sd2 = get_number(d2)

	# Update Labels
	dice_label1.config(text=d1)
	dice_label2.config(text=d2)

	# Update sub Labels
	sb_dice_label1.config(text=sd1)
	sb_dice_label2.config(text=sd2)

	# Get total die roll
	total = sd1 + sd2
	total_label.config(text=f'You Rolled: {total}') 




# Create a dice list
my_die =['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create Die Label
dice_label1 = Label(my_frame, text='', font=("Helvetica", 100))
dice_label1.grid(row=0, column=0, padx=5)
sb_dice_label1 = Label(my_frame, text='')
sb_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=("Helvetica", 100))
dice_label2.grid(row=0, column=2, padx=5)
sb_dice_label2 = Label(my_frame, text='')
sb_dice_label2.grid(row=1, column=2)


# Roll die button
my_button = Button(root, text="Roll Die", command=roll_die)
my_button.pack(pady=20)

# Create Totals Label
total_label = Label(root, text='', font=("Helvetica", 24), fg="grey")
total_label.pack(pady=40)

# Roll the die
roll_die()

root.mainloop() 