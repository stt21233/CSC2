# This program shows Grid Manager - which helps us to organize our widgets easily

from tkinter import*
from tkinter import ttk


root=Tk()


def callback():
    val1 = entry.get()
    val2 = entry2.get()
    print("your name is :" + val1)
    print("Your Password is :" + val2)
    if chvar.get() == 1:  # means the checkbox is checked
        print("Remember me selected")
    else:
        print("not selected")
    print(gender.get()) # this is where to get our gender value to show when
    # this is where to get our gender value to show when we run the program
    print("Gender is: " +gender.get())
    print(months.get())
    print('Year is: ' + year.get())
    print(year.get())
    #we run the program


# create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

# create placeholder
entry.insert(0, 'Please enter your name')
entry2.insert(0, 'Please enter your password')

# create button and labels
button = ttk.Button(root, text='Enter', command=callback)
lbltittle = ttk.Label(text='Our Title here', font=(('Arial'),22))
lblname = ttk.Label(text='Your Name: ')
lblpass = ttk.Label(text='Your Password: ')

# position of the buttons, label s and entries as outcome
lbltittle.grid(row=0, column=0)
lblname.grid(row=1, column=0)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
# button.grid(row=3, column=1, sticky=E+W) # E+W spans it across the cell in that column
# button,grid(row=3, column=1, sticky=E) # will have the button on the right
# button.grid(row=3, column=1, sticky=W) # will put button on left side
# gives you a bit of a gap between the two rows
button.grid(row=3, column=1, sticky=E, pady=5)

chvar = IntVar()
chvar.set(0)

cbox = Checkbutton(root, text="Remember me", variable=chvar, font='Arial 10').grid(row=4, column=0, sticky=E, columnspan=2)



#create another variable
gender = StringVar()

#create radio button
# to get the value from our radio button - in the callback function
ttk.Radiobutton(root, text='Female', value='Female', var=gender).grid(row=5,column=0)
ttk.Radiobutton(root, text='male', value='male', var=gender).grid(row=5,column=1)

"""create combobox where our first parameter will be root
and for the second will be textvariable(months) and use grid geometry..
for the Combobox (where it will beon the window)
When the application is run the combo box is empty
need to create variables for our combo box which we will 
do now"""
months = StringVar() # StringVar is my function
ComboBox=ttk.Combobox(root, textvariable=months,
                      values=('Jan', 'Feb', 'Mar', 'Apr')).grid(row=6, column=0)

#there is a problem that when we run the program and click on a month
# we can actually write over it or delete it

"""ComboBox = ttk.Combobox(root,textvariable=months,
                        values=('Jan', 'Feb', 'Mar', 'Apr'), state='readonly').grid(row=6, column=0)"""

# create spinbox - 'from' is a special keyword for Python -
# so we need to use _after it.
year = StringVar()
Spinbox(root,from_=1990, to=2022,textvariable=year).grid(row=6,column=1)
#use grid geometry Manager to our window
# but we are able to edit the values in the spinbox
# so you need to add the 'readonly' function for spin box
#Spinbox(root,from_=1990, to= 2022, textvariable=year,
#states='readonly').grid(row=6,column=1)
# to get the value to print out when program is run add a print statement in function
# print(year.get())


root.geometry('500x450') # the size of the window
root.mainloop()

