from tkinter import *

#create main window

def quit():
    main_window.destroy()

# create print details of all camps

def print_camp_details():
    # these are the global variables that are used
    global j_names, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Leader").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Location").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="No of Campers").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Weather").grid(column=4, row=7)

# add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][2])).grid(
            column=3, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1

def main():
    # these are the global variables that are used
    global main_window
    global camp_details, entry_name, entry_receipt, entry_number, total_entries
    # create empty list for camp details and empty variable for entries in the list
    camp_details = []
    total_entries = 0
    # create the GUI and start it up
    main_window = Tk()
    main_window.mainloop()


main()