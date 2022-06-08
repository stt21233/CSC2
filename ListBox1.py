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

root.geometry("650x650+650+200")
root.mainloop()