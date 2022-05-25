from tkinter import * # Imports everthing from TK - tkinter
from tkinter import ttk # ttk is a sub module of tkinter

root = Tk() # top level window

#Create a Label Widget
label = Label(root, text="Hello Python") # What you see
#on sceen

# font colour, config is for properties
label.config(text="hello Python", fg="red")
label.config(bg="yellow") # background colour
label.config(font="Times 20")

label.config(text='LOL')
label.config(wraplength='150') #wrap text if long label
label.config(justify='right')

# Showing it on the screen
label.pack()
root.geometry("300x250")

root.mainloop() # GUI is always looping
# when you run your mouse over and you can click on any buttons/labels