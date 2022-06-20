from tkinter import *
from tkinter import filedialog
import os

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("500x500")

def payment():
	if amount_entry.get() and interest_entry.get() and terms_entry.get():
		
	# Convert Entry to number
		year = int(terms_entry.get())
		months = year * 12
		rate = float(interest_entry.get())
		loan = int(amount_entry.get())

	# Calculate Loan (Montly interest rate)
		monthly_rate = rate / 100 / 12

	# Get Payement
		payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
		payment = f'KSH{payment:,.2f}'
	# Output payment
		payment_label.config(text=f'Monthly Payement is: {payment}' )

	else:
		payment_label.config(text='You forgot to enter a value')


# Define the frame
label_frame = LabelFrame(root, text='Mortgage Calculator')
label_frame.pack(pady=40)

my_frame = Frame(label_frame)
my_frame.pack(pady=20, padx=10)

# Labels and Entries
amount_label = Label(my_frame, text='Loan Amount')
amount_entry = Entry(my_frame, font=('Helvetica', 15))

interest_label = Label(my_frame, text='Interest Rates')
interest_entry = Entry(my_frame, font=('Helvetica', 15))

terms_label = Label(my_frame, text='Terms (years)')
terms_entry = Entry(my_frame, font=('Helvetica', 15))

# Organise L & E in frame
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20)

terms_label.grid(row=2, column=0)
terms_entry.grid(row=2, column=1)

# Button
my_button = Button(label_frame, text='Calculate Payement', command=payment)
my_button.pack(pady=20)

# Output Label
payment_label = Label(root, text='', font=('Helvetica', 20))
payment_label.pack(pady=20)

root.mainloop()