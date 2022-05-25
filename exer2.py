from tkinter import * # imports everything from TK

root = Tk() # top level window

# create Label
label = Label(root, text="Hello Python")
label.pack()

# Create button(without command does not do anything)
button = Button(root, text='click Me!')
button.pack()

root.geometry('350x300')
root.mainloop() # this is always at the end of the code