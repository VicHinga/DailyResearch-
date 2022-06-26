from tkinter import *
import random
# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Dev_DesktopRelated/Tkinter/installer/Clown.ico')
root.geometry("900x500")
root.configure(background='green')

# Shuffle cards
def shuffle():
	# Define deck
	suits = ["Diamonds","Clubs","Hearts","Spades"]
	values = range(2,15)
	
	global deck
	deck = []

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	# Create Player & Dealer
	global player, dealer
	dealer = []
	player = []

	# Get random card (Dealer)
	card = random.choice(deck)
	# remove from deck
	deck.remove(card)
	# apend card todealer list
	dealer.append(card)
	# Output
	dealer_label.config(text=card) 


	# Get random card (Player)
	card = random.choice(deck)
	# remove from deck
	deck.remove(card)
	# apend card todealer list
	player.append(card)
	# Output
	player_label.config(text=card) 


# deal the cards
def deal_cards():
	try:
		# Get random card (Dealer)
		card = random.choice(deck)
		# remove from deck
		deck.remove(card)
		# apend card todealer list
		dealer.append(card)
		# Output
		dealer_label.config(text=card)

		# Get random card (Player)
		card = random.choice(deck)
		# remove from deck
		deck.remove(card)
		# apend card todealer list
		player.append(card)
		# Output
		player_label.config(text=card) 

		root.title(f'There are {len(deck)} Cards in deck')
	except:
		root.title(f'No Cards in deck')

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Card Frames
dealer_frame= LabelFrame(my_frame, text='Dealer', font=('Helvetica', 9))
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame= LabelFrame(my_frame, text='Player', font=('Helvetica', 9))
player_frame.grid(row=0, column=1, ipadx=20)

# Place the carda in the frame
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# Shuffle & Buttons
shuffle_btn = Button(root, text='Shullfe', font=('Helvetica', 15), command=shuffle)
shuffle_btn.pack(pady=20)

card_btn = Button(root, text='Get Cards', font=('Helvetica', 15), command=deal_cards)
card_btn.pack(pady=20)

root.mainloop()