from tkinter import *


# entry boxes for customer details and buttons
Label(main_window, text="Customer full name", font=("Helvetica bold"), size=14).grid(row=4, column= 1)
entry_name = Entry(main_window)
entry_name.grid(row=2, column= 1)
Label(main_window, text="Receipt number", font=("Helvetica bold"), size=14).grid(row=4, column=2)
entry_receipt = Entry(main_window)
entry_receipt.grid(row=4, column=2)
Label(main_window, text="Item hired", font=("Helvetica bold"), size=14).grid(row=4, column=4)
entry_hireditem = Entry(main_window)
entry_hireditem.grid(row=5, column=4)
Label(main_window, text="Number of hired items",font=("Helvetica bold"), size=14).grid(row=4, column=5)
entry_number_of_hired_item = Entry(main_window)
entry_hireditem.grid(row=6, column=6)
Label(main_window, text="Delete row #", font=("Helvetica bold"),size=14).grid(row=4, column=6)
entry_delete_row = Entry(main_window)
entry_delete_row.grid(row=7, column=8)
# Create buttons
Button(main_window, text="Append details", font=("Helvetica bold"),size=8).grid(row=4,column=20)
Button(main_window, text="Print details", font=("Helvetica bold"), size=8).grid(row=5, column=21)
Button(main_window, text="Delete button",font=("Helvetica bold"), size=8).grid(row=8, column=29)
Button(main_window, text="Quit program", font=("Helvetica bold"), size=8).grid(row=0, column=21)



# Create GUI and make sure entry boxes and button are appearing
def main():
    # the global variables that are used
    global main_window
    global main_window, customer_details, total_entries
    # create empty list for camp details and empty variable for entries in the list
    customer_details = []
    total_entries = 0
    # create the GUI and start it up
    main_window = Tk()
    main_window.mainloop()












