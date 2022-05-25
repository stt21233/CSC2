from tkinter import *

root = Tk()
root.title("App")
root.geometry("400x300")

def calculate():
    length = int(length_E.get())
    width = int(width_E.get())
    height = int(height_E.get())

    area = length * width
    post = (length + 1) * width
    if height <= 1:
        cement = 1.8
    elif height >= 2:
        cement = 2.4
    bags = area * 2
    joists = area / .4
    decking = area * 11

    a = Label(root, text="Area " + str(area))
    a.grid(row=4, column=0)
    b = Label(root, text="Post " + str(post))
    b.grid(row=5, column=0)
    c = Label(root, text="Cement " + str(cement))
    c.grid(row=6, column=0)
    d = Label(root, text="Bag " + str(bags))
    d.grid(row=7, column=0)
    e = Label(root, text="Joists " + str(joists))
    e.grid(row=8, column=0)
    f = Label(root, text="Decking " + str(decking))
    f.grid(row=9, column=0)



Quit = Button(root, text="Quit", command=root.quit)
Quit.grid(row=0, column=0)

Calculate = Button(root, text="Calculate", command=calculate)
Calculate.grid(row=0, column=1)

length_lbl = Label(root, text="Length")
length_lbl.grid(row=1, column=0)

height_lbl = Label(root, text="height")
height_lbl.grid(row=2, column=0)

width_lbl = Label(root, text="width")
width_lbl.grid(row=3, column=0)

#user entry
length_E = Entry(root, width=25)
length_E.grid(row=1, column=1)

width_E = Entry(root, width=25)
width_E.grid(row=2, column=1)

height_E = Entry(root, width=25)
height_E.grid(row=3, column=1)



root.mainloop()
