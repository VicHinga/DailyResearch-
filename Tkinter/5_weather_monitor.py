from tkinter import *
from PIL import ImageTk,Image
import requests
import json

# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Tkinter/Clown.ico')
root.geometry("300x200")

try:
	# api key in the get method
	api_req = request.get()
	api = json.loads(api_request.content)
	city = api[0]['ReportingArea']
	quality = api[0]['AQI']
	category = api[0]['Category']['Name']
except Exception as e
	api = "Eror..."

myLabel = Label(root, text=city + "Air Quality" + str(quality) + " " + category)
myLabel.pack()

root.mainloop()