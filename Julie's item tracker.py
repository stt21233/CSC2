from tkinter import *
root = Tk()



# quit program



# print details of all items
def print_camp_details():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, font='bold', text="Customer full name").grid(column=0, row=7)
    Label(main_window, font='bold', text="receipt number").grid(column=1, row=7)
    Label(main_window, font='bold', text="hired item").grid(column=2, row=7)
    Label(main_window, font='bold', text="number of hired items").grid(column=3, row=7)


mainloop()