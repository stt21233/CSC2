#############################################################
############   **** JULIES ITEM TRACKER ****   ##############
#############################################################
from tkinter import *

main_window = Tk()


# entry boxes details and buttons
def setup_buttons():
    global customer_details, entry_name, entry_receipt, entry_hired_item, entry_number_of_hired_item, entry_delete_row, total_entries
    Label(main_window, text="Customer full name", font=("Helvetica bold", 9)).grid(row=4, column=1)
    entry_name = Entry(main_window)
    entry_name.grid(row=5, column=1)
    Label(main_window, text="Receipt number", font=("Helvetica bold", 9)).grid(row=6, column=1)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(row=7, column=1)
    Label(main_window, text="Item hired", font=("Helvetica", 9)).grid(row=8, column=1)
    entry_hired_item = Entry(main_window)
    entry_hired_item.grid(row=9, column=1)
    Label(main_window, text="Number of hired items", font=("Helvetica", 9)).grid(row=10, column=1)
    entry_number_of_hired_item = Entry(main_window)
    entry_number_of_hired_item.grid(row=11, column=1)
    Label(main_window, text="Delete row #", font=("Helvetica", 9)).grid(row=13, column=1)
    entry_delete_row = Entry(main_window)
    entry_delete_row.grid(row=14, column=1)
    # Create buttons
    Button(main_window, text="Append details", font=("Helvetica bold", 8),
           command=check_inputs).grid(row=12, column=1)
    Button(main_window, text="Print details", font=("Helvetica bold", 8),
           command=print_tracker_details).grid(row=12, column=2)
    Button(main_window, text="Delete", font=("Helvetica bold", 8),
           command=delete_row).grid(row=14, column=2)
    Button(main_window, text="Quit program", font=("Helvetica bold", 8),
           command=quit).grid(row=0, column=60)


# Check Inputs
def check_inputs():
    global customer_details, entry_name, entry_receipt, entry_hired_item, entry_number_of_hired_item, total_entries
    input_check = 0
    Label(main_window, text="                        ").grid(column=2, row=5)
    Label(main_window, text="                        ").grid(column=2, row=7)
    Label(main_window, text="                        ").grid(column=2, row=9)
    Label(main_window, text="                        ").grid(column=2, row=11)
    # Check that Customer full name is not blank, set error text if blank
    if len(entry_name.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=5)
        input_check = 1
    # Check the number of receipt number is not blank and is a integer, set error text if blank
    if (entry_receipt.get().isdigit()):
        Label(main_window, fg="red", text="                 ").grid(column=2, row=4)
    else:
        Label(main_window, fg="red", text="Number Only").grid(column=2, row=7)
        input_check = 1

     # Check that Item hired is not blank, set error text if blank
    if len(entry_hired_item.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=9)
        input_check = 1
        # Check that number of hired is not blank and is between 1-500, set error text if blank
    if (entry_number_of_hired_item.get().isdigit()):
        if int(entry_number_of_hired_item.get()) < 1 or int(entry_number_of_hired_item.get()) > 500:
            Label(main_window, fg="red", text="between 1-500").grid(column=2, row=11)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Between 1-500").grid(column=2, row=11)
        input_check = 1
    if input_check == 0:
        append_detail()


# Print Tracker Details
def print_tracker_details():
    # Variables that are used
    global j_name, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Row").grid(column=11, row=4)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer Full Name").grid(column=12, row=4)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Receipt Number").grid(column=13, row=4)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item Hired").grid(column=13, row=4)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of Hired Items").grid(column=14, row=4)
    Label(main_window, font=("Helvetica 10 bold"))


# add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=13, row=name_count + 5)
        Label(main_window, text=(customer_details[name_count][0])).grid(
            column=14, row=name_count+5)
        Label(main_window, text=(customer_details[name_count][1])).grid(
            column=15, row=name_count+5)
        Label(main_window, text=(customer_details[name_count][2])).grid(
            column=16, row=name_count+5)
        Label(main_window, text=(customer_details[name_count][3])).grid(
            column=17, row=name_count+5)
        name_count += 1


def append_detail():
    # these are the global variables that are used
    global customer_details, entry_name, entry_receipt, entry_hired_item, entry_number_of_hired_item, total_entries
    # append each item to its own area of the list
    customer_details.append([entry_name.get(), entry_receipt.get(),
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
    del customer_details[int(entry_delete_row.get())]
    total_entries = total_entries - 1
    entry_delete_row.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="                 ").grid(column=12, row=name_count + 2)
    Label(main_window, text="                 ").grid(column=13, row=name_count + 2)
    Label(main_window, text="                 ").grid(column=14, row=name_count + 2)
    Label(main_window, text="                 ").grid(column=15, row=name_count + 2)
    Label(main_window, text="                 ").grid(column=16, row=name_count + 2)
    # print all the items in the list
    print_tracker_details()




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







