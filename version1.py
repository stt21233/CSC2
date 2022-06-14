from tkinter import *
root = Tk()



# Button: Quit Program





# Program Titles
title = Label(root, text="Julie's Item Tracker",
              font=(("verdana"), 15))
title.place(x=100, y=20)
subh1 = Label(root, text="Data Collection",
              font=(("verdana"), 13))
subh1.place(x=20, y=60)



# Customer Full name
name_txt = Label(root, text="full name :")
name_input = Entry(root,width=30)

# Receipt Number
receipt_txt = Label(root, text="Receipt number :")
receipt_input = Entry(root,width=30)

# Hired Items
hireditem_txt = Label(root, text="Hired item :")
hireditem_input = Entry(root,width=30)

# number of hired item
total_txt = Label(root, text="Number of hired item :")
total_input = Entry(root,width=30)

# Placement of Components
     # Program Title
title.place(x=100, y=17)
     # Subheading - Data Collection
subh1.place(x=25, y=60)
     # customer full name - Component.1
name_txt.place(x=20, y=80)
name_input.place(x=15, y=100)
     # Receipt number - Component.2
receipt_txt.place(x=20, y=120)
receipt_input.place(x=15, y=140)
     # Hired item - Component.3
hireditem_txt.place(x=20, y=160)
hireditem_input.place(x=15, y=180)
  # Number of hired item - Component.4
total_txt.place(x=20, y=200)
total_input.place(x=15, y=220)





# create button
button = Button(root, text='Save')

root.geometry("500x300")

root.mainloop()