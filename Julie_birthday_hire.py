from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

win = Tk()
win.configure(bg="grey")


# Functions Start

def focused(event, msg):
    if event.widget.get() == msg:
        event.widget.delete(0, "end")
        event.widget.configure(fg="black")

def unfocused(event, msg):
    if event.widget.get() == "":
        event.widget.configure(fg="grey")
        event.widget.insert(0, msg)

def submit():
    customer_name = customer_name_entry.get()
    recipt_number = recipt_number_entry.get()
    item_hired = item_hired_entry.get()
    number_of_items = num_of_item_hired_entry.get()

    submittion_list = []
    submittion_list.append(customer_name)
    submittion_list.append(recipt_number)
    submittion_list.append(item_hired)
    submittion_list.append(number_of_items)

    if customer_name == "Enter Your Name":
        messagebox.showerror(title="Name Error", message="Please enter your full name")

    elif recipt_number == "Enter Your Receipt Number":
        messagebox.showerror(title="Receipt Number Error", message="Please Enter a receipt number")

    elif item_hired == "Enter The Item Hired":
        messagebox.showerror(title="Item Error", message="Please Enter the item hired")

    elif number_of_items == "Enter The Amount Of Items Hired":
        messagebox.showerror(title="No. of Item Error", message="Please Enter the amount of items hired")

    

    print(customer_name, recipt_number, item_hired, number_of_items)

def new_window():
    global win2
    try:

        if win2.winfo_exists():
            win2.deiconify()
        else:
            win2 = Toplevel()
            set_up(win2)

    except:
        win2 = Toplevel()
        set_up(win2)


def set_up(window):
    pass


# Functions End




### Font Configuration Start

title_font = tkFont.Font(family="Helvetica",size=24,weight="bold")
normal_font = tkFont.Font(family="Helvetica",size=10,weight="bold")
button_font = tkFont.Font(family="Helvetica", size=16, weight="bold")

### Font Configuration End



### Frame Creation Start

win.columnconfigure(0, weight=1)
win.rowconfigure(2, weight=1)

title_frame = Frame(win, padx=15, pady=15, bg="grey")
entries_frame = Frame(win, padx=15, pady=15, bg="grey")
buttons_frame = Frame(win, padx=15, pady=15, bg="grey")

title_frame.grid(column=0, row=0, sticky="ew")
entries_frame.grid(column=0, row=1, sticky="ew")
buttons_frame.grid(column=0, row=2, sticky="news")

### Frame Creation End


### Title Start

title_frame.columnconfigure((0, 2), weight=1)
title = Label(title_frame, text="Julie Birthday Hire", font=title_font, bg="grey")
title.grid(row=0, column=1, sticky="nsew")

### Title Start


### Entries Boxes Start
entries_frame.columnconfigure((0, 4), weight=1)
entries_frame.columnconfigure(2, weight=2)

customer_name_entry = Entry(entries_frame, font=normal_font, fg="grey", width=30)
customer_name_entry.insert(0, "Enter Your Name")
customer_name_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Your Name"))
customer_name_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Your Name"))
customer_name_entry.grid(row=0, column=1)


recipt_number_entry = Entry(entries_frame, font=normal_font, fg="grey", width=30)
recipt_number_entry.insert(0, "Enter Your Receipt Number")
recipt_number_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Your Receipt Number"))
recipt_number_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Your Receipt Number"))
recipt_number_entry.grid(row=0, column=3)


item_hired_entry = Entry(entries_frame, font=normal_font, fg="grey", width=30)
item_hired_entry.insert(0, "Enter The Item Hired")
item_hired_entry.bind('<FocusIn>', lambda e: focused(e, "Enter The Item Hired"))
item_hired_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter The Item Hired"))
item_hired_entry.grid(row=1, column=1, pady=(15, 0))


num_of_item_hired_entry = Entry(entries_frame, font=normal_font, fg="grey", width=30)
num_of_item_hired_entry.insert(0, "Enter The Amount Of Items Hired")
num_of_item_hired_entry.bind('<FocusIn>', lambda e: focused(e, "Enter The Amount Of Items Hired"))
num_of_item_hired_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter The Amount Of Items Hired"))
num_of_item_hired_entry.grid(row=1, column=3, pady=(15, 0))


### Entries Boxes End


### Buttons Start

buttons_frame.columnconfigure((0,2,4,6), weight=1)
buttons_frame.rowconfigure((0,2), weight=1)


quit_button = Button(buttons_frame, text="Quit", font=button_font, command=win.quit)
quit_button.grid(row=1, column=1)

submit_entries = Button(buttons_frame, text="Submit", font=button_font, command=submit)
submit_entries.grid(row=1, column=3)

view_entries = Button(buttons_frame, text="View Entries", font=button_font, command=new_window)
view_entries.grid(row=1, column=5)

### Buttons End


### Tkinter Window Configuration Start
screen_x, screen_y = win.winfo_screenwidth(), win.winfo_screenheight() #Grabs device resolution


# Window Geometry Calculations
win_x = int(screen_x / 3) # Deciding window width based on screen size, so no matter what display, window will always take up 33.333%
win_y = int(screen_y / 4) # Deciding window height based on screen size, so no matter what display, window will always take up 33.333%


margin_x = int(screen_x / 2 - win_x / 2) # Adding padding so window will always appear in the middle
margin_y = int(screen_y / 2 - win_y / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

win.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}")
### Tkinter Window Configuration End


mainloop()