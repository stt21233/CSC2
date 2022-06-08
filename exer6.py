from tkinter import * # imports everything from TK
from tkinter import ttk

import main

root=Tk()x
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is :"  + val2)

# Create entry boxes
entry= ttk.Entry(root, width=30)   # size of the field for entry
entry2 = ttk.Entry(root, width=30)
entry.insert(0,"Please enter your name") #0 is the index - first echacater
entry2.config(show='*')    #this will hide the password ofr the text entered

#add a button to the window
button=ttk.Button(root,text='Click ME!', command=callback)
# when you put in a command you need to write a function under root
entry.pack()
entry2.pack()
button.pack()

root.mainloop()

