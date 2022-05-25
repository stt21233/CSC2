from tkinter import *
root = Tk()

root.title("Frames")

# create frame using fame construction method
# to make frame visible - use background colour(bg)
frame = Frame(root, height=300, width=300, bg='red', bd=7, relief=SUNKEN) # relief can be raised
frame.pack(fill=X) # using geometry mangager for frame

button1=Button(frame,text='Button1')
button1.pack()
button2=Button(frame,text='Button2')
button2.pack()
button1.pack(side=LEFT, padx=20, pady=50)
button2.pack(side=LEFT, padx=20, pady=50)

searchBox = LabelFrame(root, text='Search Box', padx=10, pady=20)
searchBox.pack()

searchBar = Entry(searchBox, width=30)
searchBar.pack(padx=10)

title = Label(searchBox, text="title",
              font=(("verdana"), 15))
title.pack()

root.geometry('650x650+450+200')
root.mainloop()