from tkinter import *
from tkinter import filedialog
import PyPDF2 

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/installer/Clown.ico')
root.geometry("300x300")

# Text Box
my_text = Text(root, height=30, width=60)
my_text.pack(pady = 10)

# Clear Text Box
def clear_box():
	my_text.delete(1.0, END)

# Oped PDF
def open_pdf():
	open_file = filedialog.askopenfilename(
		initialdir="C:",
		title = "Open PDF File",
		filetypes = (
			("PDF Files", "*.pdf"),
			("All Files", "*.*")))

	# Cehck if open file is PDF
	if open_file:
		pdf_file = PyPDF2.PdfFileReader(open_file)
		# Set the PDF page to read(First Page)
		page = pdf_file.getPage(0)
		# Extract the text from PDF
		page_detailes = page.extractText()
		# Add Text to Text Box
		my_text.insert(1.0, page_detailes)

# Menu
my_menu = Menu(root)
root.config(menu = my_menu)

# Dropdown Menu
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_box)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()