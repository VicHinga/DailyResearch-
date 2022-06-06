from tkinter import *
from random import randint
from tkinter import filedialog
import PyPDF2 

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("600x400")

words = [
(("Me llamo"), ("My name is")),
(("Mi Nombre es"),	("My name is")),
(("Hola, soy Hinga"), 	("Hi, I’m Hinga")),
(("¿Cómo te llamas?"), ("What is your name?")),
(("Buenos días"), ("Good morning")),
(("Buenas tardes"), ("Good afternoon")),
(("Buenas noches"),	("Good evening")),
(("¿Cómo está usted?"),	("How are you?")),
(("¿Cómo estás?"), 	("How are you?")),
(("¿Qué tal? "),	("How are you?")),
(("¿Cómo te va?"), ("How’s it going?")),
(("¿Qué haces?"), ("What are you doing?")),
(("¿Qué pasa?"), ("What’s happening?")),
(("Bien, gracias"), ("Good, thank you")),
(("Muy bien"),	("Very well")),
(("Así, así"), ("So, so")),
(("Como siempre"), ("As always")),
(("¿Y tú?"), ("And you?")),
(("¡Gracias!"), ("Thank you!")),
(("¡Muchas gracias!"), ("Thank you very much!")),
(("¡De nada!"), ("You’re welcome!")),
(("Por favor"),	("Please")),
(("¡Perdon!"), ("Excuse me!")),
(("¡Disculpe!"), ("Excuse me!")),
(("¡Lo siento!"), ("Sorry!")),
(("¿Qué…?"), ("What?")),
(("¿Quién…?"), ("Who?")),
(("¿Cuándo…?"), ("When?")),
(("¿Por qué…?"), ("Why?")),
(("¿Cuál?"), ("Which?")),
(("¿Cómo…?"), ("How?")),
(("¿Qué hora tienes?"), ("What time is it?")),
(("¿De dónde viene?"),	("Where are you from?")),
(("¿Dónde vives?"),	("Where do you live?")),
(("¿Puede ayudarme?"), ("Can you help me?")),
(("¿Podría ayudarle?"), ("Can I help you?")),
(("¿Cuánto cuesta eso?"), ("How much does it cost?")),
(("¿Entiende?") ,	("Do you understand?")),
(("¡Puede repetirlo!"),	("Can you say that again?")),
(("¿Qué significa [word]?"),	("What does [word] mean?")),
(("¿Puedes hablar más despacio?"),	("Can you speak slowly?")),
(("¿Dónde puedo encontrar un taxi?"),	("Where can I find a taxi?")),
(("¿Dónde está [hotel’s name] hotel?"),	("Where is [hotel’s name] hotel?")),
(("Sí"), ("Yes")),
(("No"), ("No")),
(("Tal vez"), ("Maybe")),
(("Claro"), ("Of course")) ]


count = len(words)

def next():
	global hinter, hint_count
	# Clear Screen
	ans_label.config(text="")
	entry.delete(0, END)

	# Clear Hint Label
	hint_label.config(text="")

	# Reset hint stuf
	hinter = ""
	hint_count = 0
	
	# Create random selection
	global random_word
	random_word = randint(0, count-1)
	# Upadte label with spanish word
	spanish_word.config(text=words[random_word][0])


def answer():
	if entry.get().capitalize() == words[random_word][1]:
		ans_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
	else:
		ans_label.config(text=f"Incorrect! {words[random_word][0]} is not {entry.get().capitalize()}")

hinter = ""
hint_count = 0

def hint():
	global hinter
	global hint_count
	
	if hint_count < len(words[random_word][1]):
		hinter = hinter + words[random_word][1][hint_count]
		hint_label.config(text=hinter)
		hint_count +=1

# Labels
spanish_word = Label(root,text="", font=("Helvetica", 30))
spanish_word.pack(pady=50)

ans_label = Label(root, text="")
ans_label.pack(pady=20)

entry = Entry(root, font=("Helvetica", 18))
entry.pack(pady=20)

# Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=0)

ans_btn = Button(btn_frame, text="Answer", command=answer)
ans_btn.grid(row=0, column=0, padx=20)

next_btn = Button(btn_frame, text="Next", command=next)
next_btn.grid(row=0, column=1)

hint_btn = Button(btn_frame, text="Hint", command=hint)
hint_btn.grid(row=0, column=2, padx=20)

# Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

root.mainloop()