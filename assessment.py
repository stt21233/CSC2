from tkinter import *

#create main window

def quit():
    main_window.destroy()

# variable that's use

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

# check if input are within the range
def check_inputs():
    # these are the global variables that are used
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)
    # Check that leader is not blank, set error text if blank
    if len(entry_leader.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    # Check that location is not blank, set error text if blank
    if len(entry_location.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1
    # Check the number of campers is not blank and between 5 and 10, set error text if blank
    if (entry_campers.get().isdigit()):
        if int(entry_campers.get()) < 5 or int(entry_campers.get()) > 10:
            Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
        input_check = 1
    # Check that weather is not blank, set error text if blank
    if len(entry_weather.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_name()

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