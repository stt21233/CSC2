#############################################################
############   **** JULIES ITEM TRACKER ****   ##############
#############################################################

from tkinter import *

main_window = Tk()
# entry boxes details and buttons
Label(main_window, text="Customer full name", font=("Helvetica bold", 9)).grid(row=1, column=1)
entry_name = Entry(main_window)
entry_name.grid(row=2, column= 1)
Label(main_window, text="Receipt number", font=("Helvetica bold", 11)).grid(row=3, column=1)
entry_receipt = Entry(main_window)
entry_receipt.grid(row=4, column=1)
Label(main_window, text="Item hired", font=("Helvetica", 11)).grid(row=5, column=1)
entry_hireditem = Entry(main_window)
entry_hireditem.grid(row=6, column=1)
Label(main_window, text="Number of hired items",font=("Helvetica", 11)).grid(row=7, column=1)
entry_number_of_hired_item = Entry(main_window)
entry_number_of_hired_item.grid(row=7, column=1)
Label(main_window, text="Delete row #", font=("Helvetica", 11)).grid(row=7, column=1)
entry_delete_row = Entry(main_window)
entry_delete_row.grid(row=8, column=1)
# Create buttons
Button(main_window, text="Append details", font=("Helvetica bold", 8)).grid(row=4,column=20)
Button(main_window, text="Print details", font=("Helvetica bold", 8)).grid(row=5, column=21)
Button(main_window, text="Delete button",font=("Helvetica bold", 8)).grid(row=8, column=29)
Button(main_window, text="Quit program", font=("Helvetica bold", 8)).grid(row=0, column=21)


# Print Tracker Details
def print_tracker_details():
    # Variables that are used
    global j_name, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer Full Name").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Receipt Number").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item Hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of Hired items").grid(column=3, row=7)
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
    # create the GUI and start it up
    main_window.mainloop()


main()







