from tkinter import *
root = Tk()



# Button: Quit Program
def quit():
    main.window.destroy()




# Program Titles
title = Label(root, text="Julie's Item Tracker",
              font=(("verdana"), 15))
title.place(x=100, y=20)
subh1 = Label(root, text="Data Collection",
              font=(("verdana"), 13))
subh1.place(x=20, y=60)



# Customer Full name
name_txt = Label(root, text="full name :")
name_input = Entry(root,width=30)

# Receipt Number
receipt_txt = Label(root, text="Receipt number :")
receipt_input = Entry(root,width=30)

# Hired Items
hireditem_txt = Label(root, text="Hired item :")
hireditem_input = Entry(root,width=30)

# number of hired item
total_txt = Label(root, text="Number of hired item :")
total_input = Entry(root,width=30)

# delete row #
delete_txt = Label(root, text="Delete row #")
delete_input = Entry(root, width=30)

# Placement of Components
     # Program Title
title.place(x=100, y=13)
     # Subheading - Data Collection
subh1.place(x=35, y=60)
     # customer full name - Component.1
name_txt.place(x=20, y=80)
name_input.place(x=15, y=100)
     # Receipt number - Component.2
receipt_txt.place(x=20, y=120)
receipt_input.place(x=15, y=140)
     # Hired item - Component.3
hireditem_txt.place(x=20, y=160)
hireditem_input.place(x=15, y=180)
     # Number of hired item - Component.4
total_txt.place(x=20, y=200)
total_input.place(x=15, y=220)
     # Delete row # -
delete_txt.place(x=20, y=240)
delete_input.place(x=15, y=260)




# create button
button = Button(root, text='Save')
#-----

# print details of all the camps
def print_camp_details():
    global name_input, receipt_input, hireditem_input, total_input
    name_count = 0
    Label(main_window, font='bold', text="Customer Full Name").grid(x=100, y=15)
    Label(main_window, font='bold', text="Receipt Number").grid(x=120, y=7)
    Label(main_window, font='bold', text="Hired item").grid(x=140, y=19)
    Label(main_window, font='bold', text="Total hired items").grid(x=150, y=70)


    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count + 8)
        Label(main_window, text=(camp_details[name_count][0])).grid(column=1, row=name_count + 8)
        Label(main_window, text=(camp_details[name_count][1])).grid(column=2, row=name_count + 8)
        Label(main_window, text=(camp_details[name_count][2])).grid(column=3, row=name_count + 8)
        Label(main_window, text=(camp_details[name_count][3])).grid(column=4, row=name_count + 8)
        name_count += 1


# add the next camper to the list
def append_name():
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, total_entries
    if len(entry_leader.get()) != 0:
        camp_details.append([entry_leader.get(), entry_location.get(), entry_campers.get(), entry_weather.get()])
        entry_leader.delete(0, 'end')
        entry_location.delete(0, 'end')
        entry_campers.delete(0, 'end')
        entry_weather.delete(0, 'end')
        total_entries += 1



#julie button
def setup_buttons():
    global camp_details, name_input, receipt_input,total_input, delete_input
    Button(main_window, text="Quit program", command=quit.grid(x=5, y=200))
    Button(main_window, txt="Append Details", command=append_name).grid(x=40, y=100)
    Label(main_window, text="Delete Row #").grid(x=100, y=200)
    delete_item = Entry(main_window)
    delete_item.grid(column=1, row=6)
    Button(main_window, text="Delete", command=delete_row).grid(column=2, row=6)

#delete a row from the list
def delete_row():
    global camp_details, delete_item, total_entries, name_count
    del camp_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    Label(main_window, text="       ").grid(column=0, row=name_count + 7)
    Label(main_window, text="       ").grid(column=1, row=name_count + 7)
    Label(main_window, text="       ").grid(column=2, row=name_count + 7)
    Label(main_window, text="       ").grid(column=3, row=name_count + 7)
    Label(main_window, text="       ").grid(column=4, row=name_count + 7)
    print_camp_details()

# start the program running
def main():
    global main_window
    global camp_details, entry_name, entry_age, entry_gender, total_entries
    camp_details = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()



root.geometry("660x300")

root.mainloop()