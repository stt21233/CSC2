from tkinter import *

root = Tk()
root.title("Using Images")
root.geometry("350x350")

# in order to insert create a folder called 'Icons'
# where your Tkinter files are saved save
# some icons

# create label
lbl_text = Label(root, text="Using Images", font=("Times", 18))
lbl_text.pack()

# insert image
logo = PhotoImage(file="Icons/internet-of-things.png")

# we will create label to store the image
# which acts as a container for our image
lbl_image = Label(root, image=logo)
lbl_image.pack()

root.mainloop()
