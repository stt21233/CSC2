from tkinter import * # imports everything from tk
from tkinter import ttk # sub module of tkinter with more widgets

root = Tk()


entry = ttk.Entry(root, width=30)   # size of the field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name")  # 0 is the index - first character
entry2.config(show='*')  # this will hide the password or the text entered

entry.pack()
entry2.pack()

root.geometry("300x300") # the size of the window
root.mainloop()