# In this program we will use browse mode for selectrion of itmes in a list

from tkinter import *
from tkinter import ttk

root = Tk()

# below we will add single/double or multiple/extended brose mode
# which lets you choose one or multiple items from the list

# single selectrion from list
listBox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
# once you have run the program with single, change the mode to MULTIPLE
# and run it again and select the items of the list
listBox.insert(0, "Python") # 0, 1, 2,...are the index numbers
listBox.insert(1,"C++")
listBox.insert(2, "C#")
listBox.insert(3, "PHP")
listBox.pack(pady=25)

root.geometry("650x650+650+200")

root.geometry("650x650+650+200")