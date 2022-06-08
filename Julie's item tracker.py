from tkinter import *
root = Tk()



# Button: Quit Program




#Customer Full name
from tkinter import *
title = Label(root, text="Julie's Item Tracker",
              font=(("verdana"), 15))
name_txt = Label(root, text="Customer full name :")
name_input = Entry(root,width=30)


# create button
button = Button(root, text='Save')

# Use Geometry Manager to show our widgets
title.place(x=100, y=20) # x and y are in pixels - and that
# distance from the edges of the window.
# Run you rapplication to see the placement of the widget.



# Placement of Components
name_txt.place(x=20, y=80)
name_input.place(x=100, y=80)


root.geometry("500x250")

root.mainloop()