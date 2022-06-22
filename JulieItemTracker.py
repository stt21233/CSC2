#############################################################
############   **** JULIES ITEM TRACKER ****   ##############
#############################################################
from tkinter import *

main_window = Tk()

# entry boxes details and buttons
def setup_buttons():
    global entry_name, entry_receipt, entry_hired_item, entry_number_of_hired_item, entry_delete_row, total_entries
    Label(main_window, text="Customer full name", font=("Helvetica bold", 9)).grid(row=1, column=1)
    entry_name = Entry(main_window)
    entry_name.grid(row=2, column=1)
    Label(main_window, text="Receipt number", font=("Helvetica bold", 9)).grid(row=3, column=1)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(row=4, column=1)
    Label(main_window, text="Item hired", font=("Helvetica", 9)).grid(row=5, column=1)
    entry_hired_item = Entry(main_window)
    entry_hired_item.grid(row=6, column=1)
    Label(main_window, text="Number of hired items",font=("Helvetica", 9)).grid(row=7, column=1)
    entry_number_of_hired_item = Entry(main_window)
    entry_number_of_hired_item.grid(row=8, column=1)
    Label(main_window, text="Delete row #", font=("Helvetica", 9)).grid(row=11, column=1)
    entry_delete_row = Entry(main_window)
    entry_delete_row.grid(row=12, column=1)
    # Create buttons
    Button(main_window, text="Append details", font=("Helvetica bold", 8),
           command=check_inputs).grid(row=9,column=1)
    Button(main_window, text="Print details", font=("Helvetica bold", 8),
           command=print_tracker_details()).grid(row=9, column=2)
    Button(main_window, text="Delete", font=("Helvetica bold", 8),
           command=delete_row).grid(row=12, column=2)
    Button(main_window, text="Quit program", font=("Helvetica bold", 8),
           command=quit).grid(row=0, column=40)

# Append details
def check_inputs():
    global entry_name, entry_receipt, entry_hired_item, entry_number_of_hired_item, entry_delete_row, total_entries
    input_check = 0
    Label(main_window, text="               ").grid(column=2, row=2)
    Label(main_window, text="               ").grid(column=2, row=4)
    Label(main_window, text="               ").grid(column=2, row=6)
    Label(main_window, text="               ").grid(column=2, row=8)
    # Check that Customer full name is not blank, set error text if blank
    if len(entry_name.get()) == 0:
        Label(main_window, fg="red", text="Requiredc1").grid(column=2, row=2)
        input_check = 1
    # Check the number of receipt number is not blank and is a integer, set error text if blank
    if (entry_receipt.get().isdigit()):
        if int(entry_receipt.get()) < 100000000 or int(entry_receipt.get()) > 999999999:
            Label(main_window, fg="red", text="numerical only").grid(column=2, row=4)
            input_check = 1
    else:
        Label(main_window, fg="red", text="required").grid(column=2, row=4)
        input_check = 1
     # Check that Item hired is not blank, set error text if blank
    if len(entry_hired_item.get()) == 0:
        Label(main_window, fg="red", text="Requiredc1").grid(column=2, row=6)
        input_check = 1
    # Check that number of hired is not blank and is between 1-500, set error text if blank
    if (entry_number_of_hired_item.get().isdigit()):
        if int(entry_number_of_hired_item.get()) < 1 or int(entry_number_of_hired_item()) > 500:
            Label(main_window, fg="red", text="Required Between 1-500").grid(column=2, row=8)
        input_check = 1



def append_name():
    # these are the global variables that are used
    global entry_name, entry_receipt, entry_hired_item, entry_number_of_hired_item, total_entries
    # append each item to its own area of the list
    total_entries.append([entry_name.get(), entry_receipt.get(),
                         entry_hired_item.get(), entry_number_of_hired_item.get()])
    # clear the boxes
    entry_name.delete(0, 'end')
    entry_receipt.delete(0, 'end')
    entry_hired_item.delete(0, 'end')
    entry_number_of_hired_item.delete(0, 'end')
    total_entries += 1

def delete_row():
    # these are the global variables that are used
    global print_tracker_details, delete_item, total_entries, name_count
    # find which row is to be deleted and delete it
    del print_tracker_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7)
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    # print all the items in the list
    print_tracker_details()

# Print Tracker Details
def print_tracker_details():
    # Variables that are used
    global j_name, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer Full Name").grid(column=11, row=2)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Receipt Number").grid(column=12, row=2)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item Hired").grid(column=13, row=2)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of Hired items").grid(column=14, row=2)
    Label(main_window, font=("Helvetica 10 bold"))

# add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(print_tracker_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(print_tracker_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(print_tracker_details[name_count][2])).grid(
            column=3, row=name_count+8)
        Label(main_window, text=(print_tracker_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1


# Create GUI and make sure entry boxes and button are appearing
def main():
    # the global variables that are used
    global main_window
    global main_window, customer_details, total_entries
    # create empty list for camp details and empty variable for entries in the list
    customer_details = []
    total_entries = 0
    setup_buttons()
    # create the GUI and start it up
    main_window.mainloop()


main()







