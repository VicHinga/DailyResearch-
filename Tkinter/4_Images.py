from tkinter import *
from PIL import ImageTk,Image

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/Clown.ico')

img_1 = ImageTk.PhotoImage(Image.open('images/dry_run_B.PNG'))
img_2 = ImageTk.PhotoImage(Image.open('images/CSRF2.PNG'))
img_3 = ImageTk.PhotoImage(Image.open('images/Diwali_1.jpg'))
img_4 = ImageTk.PhotoImage(Image.open('images/dry_run_A.PNG'))
img_5 = ImageTk.PhotoImage(Image.open('images/dry_run_B.PNG'))

img_list = [img_1, img_2, img_3, img_4, img_5]
label = Label(image=img_1)

label.grid(row=0, column=0, columnspan=3)


def fwd(image_number):
	global label
	global button_fwd
	global button_back

	label.grid_forget()
	label = Label(image=img_list[image_number - 1])
	button_fwd = Button(root, text=">>", command=lambda: fwd(image_number + 1))
	button_back = Button(root, text="<<", command=lambda: back(image_number - 1) )

	if image_number == 5:
		button_fwd = Button(root, text=">>", state=DISABLED)

	label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_fwd.grid(row=1, column=2)



def back(image_number):  
	global label
	global button_fwd
	global button_back

	label.grid_forget()
	label = Label(image=img_list[image_number - 1])
	button_fwd = Button(root, text=">>", command=lambda: fwd(image_number + 1))
	button_back = Button(root, text="<<", command=lambda: back(image_number - 1) )

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_fwd.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED )
button_exit = Button(root, text="Exit", command=root.quit)
button_fwd = Button(root, text=">>", command=lambda: fwd(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2)

root.mainloop()