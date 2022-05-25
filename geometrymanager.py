"""In this program we will learn how to use Place Geometry Manager.
Place Geometry Manager allows us to exact control over the widget
locations and sizes.
We can use absolute position and size for our widgets"""
"""We will create a login form for our application"""

from tkinter import *
root = Tk()

title = Label(root, text="Place Geometry Manager",
              font=(("verdana"), 15))
name_txt = Label(root, text="Name :")
pass_txt = Label(root, text="Password :")
name_input = Entry(root,width=30)
pass_input = Entry(root, width=30)

# create button
button = Button(root, text='Save')

# Use Geometry Manager to show our widgets
title.place(x=100, y=20) # x and y are in pixels - and that
# distance from the edges of the window.
# Run you rapplication to see the placement of the widget.

# placement of other widgets
name_txt.place(x=20, y=80)
name_input.place(x=100, y=80)
pass_txt.place(x=20, y=110)
pass_input.place(x=100, y=110)

# placement of button
button.place(x=250, y=150)

root.geometry("450x450+650+350") # here the 650+350 means that we
# x location is 650 and y location is 350
root.mainloop()