from tkinter import *
import tkintermapview
# Everything is a widget

# You first create the window
root = Tk()
root.title("Learning Tkinter")
root.iconbitmap('D:/DEV/Dev_DesktopRelated/Tkinter/installer/Clown.ico')
root.geometry("900x900")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=700, height=600)
map_widget.pack()

root.mainloop()