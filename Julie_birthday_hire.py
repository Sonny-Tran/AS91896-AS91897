from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import json

win = Tk()
win.configure(bg="SkyBlue1")
win.title("Julie Birthday Hire")



# Functions Start

def write_json (data, filename="AS91896_AS91897/entry_saves.json"):
    with open (filename, 'w') as f:
        json.dump(data, f, indent=4)

def focused(event, msg): # Function for when entries are clicked on
    if event.widget.get() == msg: # Get entry from entry box and checks if they're the default placeholder message
        event.widget.delete(0, "end") # If entries from entry box is the default placeholder message, clear the entry box out
        event.widget.configure(fg="black") # Set entry box foreground to black, which makes the text black instead of the placeholder grey

def unfocused(event, msg): # Functions for when entries are clicked off
    if event.widget.get() == "": # Get entry from entry box and check if they're blank
        event.widget.configure(fg="grey") # If entry from entry box is black, make the foreground grey, making the text grey
        event.widget.insert(0, msg) # Insert placeholder message back into entry box


def submit(): 
    while True:
        # Obtain all user entries from entry boxes
        customer_name = customer_name_entry.get()
        receipt_number = receipt_number_entry.get()
        item_hired = item_hired_entry.get()
        number_of_items = num_of_item_hired_entry.get()

        # Appends all results to "submission_list"
        submission_list = []
        submission_list.append(customer_name)
        submission_list.append(receipt_number)
        submission_list.append(item_hired)
        submission_list.append(number_of_items)
        

        # Checks if user entries fit the conditions

        if customer_name == "Enter Your Full Name" or "": # Checks if placeholder text is still there or if it's blank
            messagebox.showerror(title="Name Error", message="Please enter your full name") # Shows Error Box with the text "Please enter your full name"
            break # Breaks out of While True Loop

        elif receipt_number == "Enter Your Receipt Number" or "": # Checks if placeholder text is still there or if it's blank
            messagebox.showerror(title="Receipt Number Error", message="Please enter a receipt number") # Shows Error Box with the text "Please Enter a receipt number"
            break # Breaks out of While True Loop

        elif item_hired == "Enter The Item Hired" or "": # Checks if placeholder text is still there or if it's blank
            messagebox.showerror(title="Item Error", message="Please enter the item hired") # Shows Error Box with the text "Please enter the item hired"
            break # Breaks out of While True Loop

        elif number_of_items == "Enter Amount Of Items Hired : 1 - 500" or "": # Checks if placeholder text is still there or if it's blank
            messagebox.showerror(title="No. of Item Error", message="Please enter the amount of items hired") # Shows Error Box with the text "Please enter the amount of items hired"
            break # Breaks out of While True Loop
        
        elif int(number_of_items) < 0 or int(number_of_items) > 500:
            messagebox.showerror(title="No. of Item Error", message="The amount of items hired must be between 0 and 500") # Shows Error Box with the text "Please enter the amount of items hired"
            break # Breaks out of While True Loop

        keys_list = ["Fullname", "Receipt Number", "Item Hired", "Number of items"]
        submission_dict = {}
        for key in keys_list:
            for value in submission_list:
                submission_dict[key] = value
                submission_list.remove(value)
                break

        with open ("AS91896_AS91897/entry_saves.json") as json_file:
            data = json.load(json_file)
            data.append(submission_dict)

        write_json(data)
        try:
            if win2:
                entries_set_up()
                print("Setup Attempted")
            else:
                print("Else Passed")
                pass
        except:
            print("Except Passed")
            pass


        messagebox.showinfo(title="Success!", message="You've successfully sumbitted your results")

        customer_name_entry.delete(0, "end")
        receipt_number_entry.delete(0, "end")
        item_hired_entry.delete(0, "end")
        num_of_item_hired_entry.delete(0, "end")

        customer_name_entry.insert(0, "Enter Your Full Name")
        receipt_number_entry.insert(0, "Enter Your Receipt Number")
        item_hired_entry.insert(0, "Enter The Item Hired")
        num_of_item_hired_entry.insert(0, "Enter Amount Of Items Hired : 1 - 500")

        item_hired_entry.configure(fg="grey"), num_of_item_hired_entry.configure(fg="grey"), receipt_number_entry.configure(fg="grey"), customer_name_entry.configure(fg="grey")

        break # Stops While Loop


def new_window(): # Function to make new window
    try: # Using try since if the variable "password_win" or "win2" doesn't exist yet it'll return an exception
        if password_win.winfo_exists() == 0: # Only Execute code below if password_win doesn't exist
            if win2.winfo_exists() == 0: # Only Execute code below if win2 doesn't exist
                win2.deiconify() # deiconify them if they're withdrawn or iconified
            else:
                password_checker() # Activates password_checker function
    except:
        password_checker() # Activates password_checker function

        
def password_checker():
    global password_win
    def password_check(): # Function to check password
        password = password_entry.get() # Get entry from password entry box
        if password == "password": # If the entry is equal to "password" then execute the following
            password_win.destroy() # Destroy the password window
            set_up() # Run set_up function
        else:
            messagebox.showerror(title="Incorrect Password", message="The password you've entered is incorrect") # Show error if password is incorrect
            password_win.lift() # Lifts password window up so it's not behind the main window

    password_win = Toplevel() # Creates new Toplevel() Window
    password_win.title("Password") # Set Title of "password_win" window to "password"
    

    password_label = Label(password_win, font=normal_font, text="Password:") # Creates a text label with the text "Password:"
    password_entry = Entry(password_win, font=normal_font, show="*") # Creates a entry box that shows user entries as "*"

    password_label.grid(row=0,column=0) # Creates the password label in an actual visual way, actually allows the user to see the label.
    password_entry.grid(row=0, column=1) # Creates the password entry to the right of the password label since column = 1


    submit_button = Button(password_win, text="Submit", font=normal_font, command=password_check) # Creates a button that checks if password is correct when clicked
    submit_button.grid(row=1, column=0, columnspan=2) # Creates the button in the password window GUI, row = 1 so it's below the password label/entry and stretch across 2 columns


    pass_win_x = int(win_x / 3) # Makes Password Window 33% of the main window
    pass_win_y = int(win_y / 4) # Makes Password Window 25% of the main window
    
    pass_margin_x = int(screen_x / 2 - pass_win_x/ 2) # Calculates margin required to have the password window in the centre horizontally
    pass_margin_y = int(screen_y / 2 - pass_win_y / 2) # Calculates margin required to have the password window in the centre vertically

    password_win.geometry(f"{pass_win_x}x{pass_win_y}+{pass_margin_x}+{pass_margin_y}") # Takes all the values above and actually set those parameters


def set_up():
    global win2
    win2 = Toplevel() # Creates a new window linked to the variable win2
    win2.title("Julie Birthday Hire Entries") # Sets the title of win2 window to "Julie Birthday Hire Entries"
    win2.configure(bg="bisque")
    win2.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}") # sets the geometry of the window, uses the same values as the main window so it'll be the same size as the main window
    
    entries_set_up()    

    
def entries_set_up():
    for widget in win2.winfo_children():
        if isinstance(widget, Widget):
            widget.destroy()
    
    name_label = Label(win2, font=normal_font, text="Full Name", bg="bisque3")
    receipt_num_label = Label(win2, font=normal_font, text="Receipt Number", bg="bisque3")
    item_hired_label = Label(win2, font=normal_font, text="Item Hired", bg="bisque3")
    num_of_item_hired_label = Label(win2, font=normal_font, text="Number of Items Hired", bg="bisque3")


    name_label.grid(row=0, column=0, sticky="ew", ipadx=20, ipady=3)
    receipt_num_label.grid(row=0, column=1, sticky="ew", ipadx=20, ipady=3)
    item_hired_label.grid(row=0, column=2, sticky="ew", ipadx=20, ipady=3)
    num_of_item_hired_label.grid(row=0, column=3, sticky="ew", ipadx=20, ipady=3)


    row = 1
    with open ("AS91896_AS91897/entry_saves.json") as json_file:
        data = json.load(json_file)
        length = len(data)
        for i in range(0, length):
            Label(win2, font=normal_font, bg="bisque3", text=data[i]["Fullname"]).grid(column=0, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Label(win2, font=normal_font, bg="bisque3", text=data[i]["Receipt Number"]).grid(column=1, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Label(win2, font=normal_font, bg="bisque3", text=data[i]["Item Hired"]).grid(column=2, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Label(win2, font=normal_font, bg="bisque3", text=data[i]["Number of items"]).grid(column=3, row=row, sticky="ew", ipady=3, pady=(5, 0))
            row += 1    


# Functions End



### Font Configuration Start

title_font = tkFont.Font(family="Helvetica",size=28,weight="bold") # Makes a preset font that is of the Helvetica style, size 28 and bold
button_font = tkFont.Font(family="Helvetica", size=16, weight="bold") # Makes a preset font that is of the Helvetica style, size 16 and bold
normal_font = tkFont.Font(family="Helvetica",size=13,weight="bold",slant="italic") # Makes a preset font that is of the Helvetica style, size 13 and bold


### Font Configuration End



### Frame Creation Start

win.columnconfigure(0, weight=1) # Makes Column 0 take up all the space it can
win.rowconfigure(2, weight=1) # Makes Row 2 take up all the space it can

title_frame = Frame(win, padx=15, bg="cyan4") # Creating a frame to keep the title, basically dividing the main window up into individual boxes that can contain widgets
entries_frame = Frame(win, padx=15, pady=15, bg="cyan4") # Creating a frame inside the main window to keep the entrie boxes
buttons_frame = Frame(win, padx=15, pady=15, bg="cyan4") # Creating a frame inside the main window to keep the buttons

title_frame.grid(column=0, row=0, sticky="ew") # Layout the frames in the main window using a grid format, since column = 0 and row = 0 so it'll be the highest element and positioned to the left
entries_frame.grid(column=0, row=1, sticky="ew") # Layout the frames in the main window using a grid format, sticky="ew" stands for east and west, filling out the frame to the left and right
buttons_frame.grid(column=0, row=2, sticky="news") # Layout the frames in the main window using a grid format, sticky="news" stands for north, south, east and west, filling out the frame horizontally and vertically

### Frame Creation End


### Title Start

title_frame.columnconfigure((0, 2), weight=1) # Configures columns 0 and 2 to take up as much space as possible whlist being equal to each other
title = Label(title_frame, text="Julie Birthday Hire", font=title_font, bg="cyan4") # Creates a Labal that has the text "Julie Birthday Hire" using the font preset title_font with a background colour of grey
title.grid(row=0, column=1, sticky="nsew", pady=(15, 0)) # Creates the title label in the GUI and makes it fill out the frame

### Title Start


### Entries Boxes Start
entries_frame.columnconfigure((0,4), weight=1) # Makes columns 2 take up as much space as possible
entries_frame.columnconfigure(2, weight=2) # Makes columns 2 take up as much space as possible

customer_name_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33) # Configures a entry box that shows inputted text as grey and uses the font preset normal font (Ln.125)
customer_name_entry.insert(0, "Enter Your Full Name") # Inserts the text "Enter Your Full Name" into the entry box
customer_name_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Your Full Name")) # When entry box is clicked on, execute function focused (Ln.12)
customer_name_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Your Full Name")) # When entry box is clicked off, execute function unfocused (Ln.17)
customer_name_entry.grid(row=0, column=1) # Creates the entry box in the actual GUI


receipt_number_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33) # Configures a entry box that shows inputted text as grey and uses the font preset normal font (Ln.125)
receipt_number_entry.insert(0, "Enter Your Receipt Number") # Inserts the text "Enter Your Receipt Number" into the entry box
receipt_number_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Your Receipt Number")) # When entry box is clicked on, execute function focused (Ln.12)
receipt_number_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Your Receipt Number")) # When entry box is clicked off, execute function unfocused (Ln.17)
receipt_number_entry.grid(row=0, column=3) # Creates the entry box in the actual GUI


item_hired_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33) # Configures a entry box that shows inputted text as grey ad uses the font preset normal font (Ln.125)
item_hired_entry.insert(0, "Enter The Item Hired") # Inserts the text "Enter The Item Hired" into the entry box
item_hired_entry.bind('<FocusIn>', lambda e: focused(e, "Enter The Item Hired")) # When entry box is clicked on, execute function focused (Ln.12)
item_hired_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter The Item Hired")) # When entry box is clicked off, execute function unfocused (Ln.17)
item_hired_entry.grid(row=1, column=1, pady=(20, 0)) # Creates the entry box in the actual GUI


num_of_item_hired_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33) # Configures a entry box that shows inputted text as grey ad uses the font preset normal font (Ln.125)
num_of_item_hired_entry.insert(0, "Enter Amount Of Items Hired : 1 - 500") # Inserts the text "Enter Amounut Of Items Hired : 1 - 500" into the entry box
num_of_item_hired_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Amount Of Items Hired : 1 - 500")) # When entry box is clicked on, execute function focused (Ln.12)
num_of_item_hired_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Amount Of Items Hired : 1 - 500")) # When entry box is clicked off, execute function unfocused (Ln.17)
num_of_item_hired_entry.grid(row=1, column=3, pady=(20, 0)) # Creates the entry box in the actual GUI

 
### Entries Boxes End


### Buttons Start

buttons_frame.columnconfigure((0,2,4,6), weight=1) # Makes columns 0, 2, 4, 6 take up as much space as they can while being equal, pushes widgets in columns 1, 3 and 5 to the centre
buttons_frame.rowconfigure((0,2), weight=1) # Makes rows 0 and 2 take up as much space as they can while being equal, pushes widgets in row 1 to the centre


quit_button = Button(buttons_frame, text="Quit", font=button_font, command=win.quit, width=10) # Creates button with the text "Quit" which quits the program when clicked
quit_button.grid(row=1, column=1) # Creates the button in the GUI

submit_entries = Button(buttons_frame, text="Submit", font=button_font, command=submit, width=10) # Creates button with the text "Submit" which gets entries and checks if they're vaild when clicked (Ln.23)
submit_entries.grid(row=1, column=3) # Creates the button in the GUI

view_entries = Button(buttons_frame, text="View Entries", font=button_font, command=new_window, width=10) # Creates a button with the text "View Entries" which will open up the password window in order to access entries (Ln.63)
view_entries.grid(row=1, column=5) # Creates the button in the GUI

### Buttons End


### Tkinter Window Configuration Start
screen_x, screen_y = win.winfo_screenwidth(), win.winfo_screenheight() #Grabs device resolution


# Window Geometry Calculations
win_x = int(screen_x / 2.5) # Deciding window width based on screen size, so no matter what display, window will always take up 33.333%
win_y = int(screen_y / 4) # Deciding window height based on screen size, so no matter what display, window will always take up 33.333%


margin_x = int(screen_x / 2 - win_x / 2) # Adding padding so window will always appear in the middle
margin_y = int(screen_y / 2 - win_y / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

win.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}")
### Tkinter Window Configuration End


mainloop()