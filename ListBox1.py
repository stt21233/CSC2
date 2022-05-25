# In this program we will create a list box - Useful for listing iteams

from tkinter import *
from tkinter import ttk

root = Tk()

# below we will add single/double or multiple/extended browse mode
# which lets you choose on or multiple items from the list

# single selection from list
listBox = Listbox(root, width=40, height=15)  # variable called listbox
# once you have run the program with single, change the mode to MULTIPLE
# and run it again and select the items of the list
listBox.insert(0, "Python") # 0, 1, 2,...are the index numbers
listBox.insert(1,"C++")
listBox.insert(2, "C#")
listBox.insert(3, "PHP")
listBox.pack(pady=25)

def print_me():

# create buttons
button = Button(root, text='print', command=print_me).place(x=300, y=300)
button2 = Button(root, text='Delete', command=delete_me).place(x=350, y=300)
# for these you need callback function and  want you to figure out
# how to write this out and ensure you are able to Print and also Delete items from the list


root.geometry("650x650+650+200")
root.mainloop