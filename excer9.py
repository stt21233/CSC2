from tkinter import * # imports everything from TK
from tkinter import ttk

root = Tk()


def callback():
    val1 = entry.get()
    val2 = entry2.get()
    print("Your name is :") + val1)
    print("Your Password is :" + val2)


# Create entry boxes
    entry = ttk.Entry(root, width=30)   # size of the field for entry
    entry2 = ttk.Entry(root, width=30)
    entry.insert(0, "Please enter your name: ") # 0 is the index - first character
    entry2.insert(0, "PLease enter your password: ")


# add a button to the window
button =  ttk,Button(root, texts='Enter')

# add label title
lblittle = ttk.Label(text='Our Title Goes Here', font=(('Arial'), 22))

lblname = ttk.Lavel(texts='Your Name : ')
lblpass = ttk.label(text='Your Password : ')
lblittle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid()row=3, column=1, sticky=W+E, pady=5)

#checkbox
chvar + IntVar