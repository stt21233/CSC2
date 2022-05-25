from msilib.schema import Icon
from tkinter import *
from tkinter import ttk
# if we do not import we cannot use message box for application
from tkinter import messagebox

root = Tk()

def callback():
    # 1st parameter will be title and then the text
    mbox = messagebox.askquestion("Delete", "Are you Sure", icon='warning')
    # can change icon by adding, icon='warning')
    if mbox != 'yes':
        print("Deleted")
    else:
        print('Deleted')


def callback2():
    messagebox.showinfo('Sucess', "Well Done!")
    print("You clicked OK!")

button1 = ttk.Button(root,text='Delete', command=callback).grid(row=0, column=0) # command will be definition name but need function
button2 = ttk.Button(root, text='Info', command=callback2).grid(row=0, column=1)

root.geometry('350x250')
mainloop()