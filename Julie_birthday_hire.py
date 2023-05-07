from tkinter import *
import tkinter.font as tkFont

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


# Functions End




### Font Configuration Start

title_font = tkFont.Font(family="Helvetica",size=24,weight="bold")
normal_font = tkFont.Font(family="Helvetica",size=10,weight="bold")

### Font Configuration End



### Frame Creation Start

win.columnconfigure(0, weight=1)
title_frame = Frame(win, padx=15, pady=15, bg="grey")
entries_frame = Frame(win, padx=15, pady=15, bg="grey")
buttons_frame = Frame(win, padx=15, pady=15, bg="grey")

title_frame.grid(column=0, row=0, sticky="ew")
entries_frame.grid(column=0, row=1, sticky="ew")
buttons_frame.grid(column=0, row=2, sticky="ew")

### Frame Creation End


### Title Start

title_frame.columnconfigure((0, 2), weight=1)
title = Label(title_frame, text="Julie_Birthday_Hire", font=title_font, bg="grey")
title.grid(row=0, column=1, sticky="nsew")

### Title Start


### Entries Boxes Start
entries_frame.columnconfigure((0, 4), weight=1)
entries_frame.columnconfigure(2, weight=2)

customer_name_entry = Entry(entries_frame, font=normal_font, fg="grey", width=24)
customer_name_entry.insert(0, "Please Enter Your Name")
customer_name_entry.bind('<FocusIn>', lambda e: focused(e, "Please Enter Your Name"))
customer_name_entry.bind('<FocusOut>', lambda e: unfocused(e, "Please Enter Your Name"))
customer_name_entry.grid(row=0, column=1)


recipt_number_entry = Entry(entries_frame, font=normal_font, fg="grey", width=24)
recipt_number_entry.insert(0, "Please Enter Your Receipt Number")
recipt_number_entry.bind('<FocusIn>', lambda e: focused(e, "Please Enter Your Receipt Number"))
recipt_number_entry.bind('<FocusOut>', lambda e: unfocused(e, "Please Enter Your Receipt Number"))
recipt_number_entry.grid(row=0, column=3)


### Entries Boxes End



### Tkinter Window Configuration Start
screen_x, screen_y = win.winfo_screenwidth(), win.winfo_screenheight() #Grabs device resolution


# Window Geometry Calculations
win_x = int(screen_x / 3) # Deciding window width based on screen size, so no matter what display, window will always take up 33.333%
win_y = int(screen_y / 3) # Deciding window height based on screen size, so no matter what display, window will always take up 33.333%


margin_x = int(screen_x / 2 - win_x / 2) # Adding padding so window will always appear in the middle
margin_y = int(screen_y / 2 - win_y / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

win.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}")
### Tkinter Window Configuration End

mainloop()