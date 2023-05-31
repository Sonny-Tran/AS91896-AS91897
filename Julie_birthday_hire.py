from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askyesno
import json
import re

# Set up the main window
win = Tk()
win.configure(bg="#F8B195")
win.title("Julie Birthday Hire")


# Functions Start

# Function to take data and write it to the json file
def write_json (data, filename="entry_saves.json"):
    with open (filename, 'w') as f:
        json.dump(data, f, indent=4)

# Function for when entries are clicked on 
def focused(event, msg): 
    if event.widget.get() == msg:
        event.widget.delete(0, "end")
        event.widget.configure(fg="black") 

# Functions for when entries are clicked off
def unfocused(event, msg): 
    if event.widget.get() == "":
        event.widget.configure(fg="grey")
        event.widget.insert(0, msg)

# Function to delete the window
def quit_win():
    answer = askyesno(title='Confirmation',
                message='Are you sure that you want to quit?')
    if answer:
        win.quit()

# Function for when the submit button is pressed
def submit():
    # Confirms if user wants to submit
    answer = askyesno(title='Confirmation',
                    message='Are you sure that you want to submit?')
    if answer: # If Yes...
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

            # Take all the entries and make a dictionary
            submission_dict = {"Fullname" : customer_name, "Receipt Number" : receipt_number, "Item Hired" : item_hired, "Number Of Items" : number_of_items}

            # Checks characters in customer_name is a digit or numeric
            num_in_name = 0
            for char in customer_name:
                if char.isdigit() or char.isnumeric():
                    num_in_name = 1
                else:
                    pass
            # Customer Name Entry Vaildation Checks
            if customer_name == "Enter Your Full Name" or customer_name.isspace() or " ": # Checks if the entry is still the placeholder, is only whitespace, or is empty
                messagebox.showerror(title="Full Name Error", message="Please enter your full name") 
                break 

            elif 0 < len(re.findall(r'\w+', customer_name)) < 2: # Checks if theres a space and a second word inside the entry
                messagebox.showerror(title="Full Name Error", message="Please enter your first name and surname")
                break
                
            elif num_in_name == 1: # Checks if there are any numbers in the entry
                messagebox.showerror(title="Full Name Error", message="There can only be letters in your name") 
                break 


            # Receipt Number Entry Vaildation Checks
            elif receipt_number == "Enter Your Receipt Number" or "": # Checks if the entry text is still the placeholder or is empty
                messagebox.showerror(title="Receipt Number Error", message="Please enter a receipt number")
                break

            elif receipt_number.isnumeric() == False: # If the entry isn't a integer
                messagebox.showerror(title="Receipt Number Error", message="Your receipt number can only contain numbers")
                break


            # Item Hired Entry Vaildation Checks
            elif item_hired == "Enter The Item Hired" or "": # Checks if the entry text is still the placeholder or is empty
                messagebox.showerror(title="Item Error", message="Please enter the item hired")
                break

            
            # Number of items Entry Vaildation Checks
            elif number_of_items == "Enter Amount Of Items Hired : 1 - 500" or "": # Checks if placeholder text is still there or if it's blank
                messagebox.showerror(title="No. of Item Error", message="Please enter the amount of items hired")
                break
            
            elif number_of_items.isnumeric() == False: # Checks if the entry isn't a integer
                messagebox.showerror(title="No. of Item Error", message="Your hired amount of items can only contain integers (Whole Numbers)")
                break

            elif int(number_of_items) < 0 or int(number_of_items) > 501: # Checks if the entry is between 1 and 500
                messagebox.showerror(title="No. of Item Error", message="The amount of items hired must be between 1 and 500") # Shows Error Box with the text "Please enter the amount of items hired"
                break # Breaks out of While True Loop

            
            # Opens the json file and appends the new data to the list
            with open ("entry_saves.json") as json_file:
                data = json.load(json_file)
                data.append(submission_dict)

            write_json(data)

            # Updates the entries window if entries window exists
            try:
                if win2:
                    entries_set_up()
            except:
                pass

            messagebox.showinfo(title="Success!", message="You've successfully sumbitted your results")

            # Set all the text in the entry boxes in the main window to grey
            for widget in entries_frame.winfo_children():
                widget.delete(0, "end")
                widget.configure(fg="grey")

            # Insert placeholder text into entry boxes
            customer_name_entry.insert(0, "Enter Your Full Name")
            receipt_number_entry.insert(0, "Enter Your Receipt Number")
            item_hired_entry.insert(0, "Enter The Item Hired")
            num_of_item_hired_entry.insert(0, "Enter Amount Of Items Hired : 1 - 500")

            break # Stops While Loop


def new_window(): # Function to check open password window
    try: 
        if password_win.winfo_exists(): # Checks if password window already exists
            messagebox.showerror(title="Password Window Error", message="You already have the password window open")
            password_win.lift()
        else:
            password_checker()
    except:
        password_checker() # Activates password_checker function

        
def password_checker():
    global password_win
    def password_check(): # Function to check if password entered is correct, destroy password window and set up entry window
        password = password_entry.get()
        if password == "password":
            password_win.destroy() 
            set_up()
        else:
            messagebox.showerror(title="Incorrect Password", message="The password you've entered is incorrect") # Show error if password is incorrect
            password_win.lift() # Lifts password window up so it's not behind the main window
    try:
        if win2:
            messagebox.showerror(title="Entries Window Error", message="The entries window is already open")
            return
    except:
        pass

    # Creates a new Window for passwords
    password_win = Toplevel()
    password_win.title("Password")
    

    password_label = Label(password_win, font=normal_font, text="Password:") # Creates a text label with the text "Password:"
    password_entry = Entry(password_win, font=normal_font, show="*") # Creates a entry box that shows user entries as "*"

    password_label.grid(row=0,column=0)
    password_entry.grid(row=0, column=1)


    # Creates a button that checks if password is correct when clicked
    submit_button = Button(password_win, text="Submit", font=normal_font, command=password_check) 
    submit_button.grid(row=1, column=0, columnspan=2)


    # Calculate window geometry to always be in the centre and for the window to always be 33.33% of display horizontally and 25% display vertically
    pass_win_x = int(win_x / 3)
    pass_win_y = int(win_y / 4) 
    
    pass_margin_x = int(screen_x / 2 - pass_win_x/ 2) 
    pass_margin_y = int(screen_y / 2 - pass_win_y / 2)

    password_win.geometry(f"{pass_win_x}x{pass_win_y}+{pass_margin_x}+{pass_margin_y}")


def set_up():
    global win2

    # Set up a new window for entries
    win2 = Toplevel()
    win2.title("Julie Birthday Hire Entries") # Sets the title of win2 window to "Julie Birthday Hire Entries"
    win2.configure(bg="#355c7d")
    win2.columnconfigure((4,6), weight=1)
    win2.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}") # sets the geometry of the window, uses the same values as the main window so it'll be the same size as the main window
    
    entries_set_up()    


# Function to delete a entry
def delete_row(id):
    answer = messagebox.askyesno(message="Do you want to delete this Entry?", title="Delete Confirmation")
    
    if answer:
        with open ("entry_saves.json") as json_file:
            data = json.load(json_file)
            del data[id]
            write_json(data)
            entries_set_up()
    win2.lift()
    
def entries_set_up():
    for widget in win2.winfo_children():
        if isinstance(widget, Widget):
            widget.destroy()

    # Create headings for entries table
    name_label = Label(win2, font=normal_font, text="Full Name", bg="#f79256")
    receipt_num_label = Label(win2, font=normal_font, text="Receipt Number", bg="#f79256")
    item_hired_label = Label(win2, font=normal_font, text="Item Hired", bg="#f79256")
    num_of_item_hired_label = Label(win2, font=normal_font, text="Number of Items Hired", bg="#f79256")


    name_label.grid(row=0, column=0, sticky="ew", ipadx=20, ipady=3)
    receipt_num_label.grid(row=0, column=1, sticky="ew", ipadx=20, ipady=3)
    item_hired_label.grid(row=0, column=2, sticky="ew", ipadx=20, ipady=3)
    num_of_item_hired_label.grid(row=0, column=3, sticky="ew", ipadx=20, ipady=3)

    # Create teh entires from the json file
    row = 1
    with open ("entry_saves.json") as json_file:
        data = json.load(json_file)
        length = len(data)
        for i in range(0, length):
            Label(win2, font=normal_font, bg="#f79256", text=data[i]["Fullname"]).grid(column=0, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Label(win2, font=normal_font, bg="#f79256", text=data[i]["Receipt Number"]).grid(column=1, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Label(win2, font=normal_font, bg="#f79256", text=data[i]["Item Hired"]).grid(column=2, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Label(win2, font=normal_font, bg="#f79256", text=data[i]["Number Of Items"]).grid(column=3, row=row, sticky="ew", ipady=3, pady=(5, 0))
            Button(win2, font=normal_font, bg="#f79256", text="Delete Row", command=lambda d=i: delete_row(d)).grid(column=5, row=row, sticky="ew", pady=(5, 0),)
            row += 1    


# Functions End



### Font Configuration Start

title_font = tkFont.Font(family="Helvetica",size=28,weight="bold") # Makes a preset font that is of the Helvetica style, size 28 and bold
button_font = tkFont.Font(family="Helvetica", size=16, weight="bold") # Makes a preset font that is of the Helvetica style, size 16 and bold
normal_font = tkFont.Font(family="Helvetica",size=14,weight="bold",slant="italic") # Makes a preset font that is of the Helvetica style, size 13 and bold

### Font Configuration End



### Frame Creation Start

win.columnconfigure(0, weight=1) # Makes Column 0 take up all the space it can
win.rowconfigure(2, weight=1) # Makes Row 2 take up all the space it can

title_frame = Frame(win, padx=15, bg="#F8B195") # Creating a frame to keep the title, basically dividing the main window up into individual boxes that can contain widgets
entries_frame = Frame(win, padx=15, pady=15, bg="#F8B195") # Creating a frame inside the main window to keep the entrie boxes
buttons_frame = Frame(win, padx=15, pady=15, bg="#F8B195") # Creating a frame inside the main window to keep the buttons

title_frame.grid(column=0, row=0, sticky="ew") # Layout the frames in the main window using a grid format, since column = 0 and row = 0 so it'll be the highest element and positioned to the left
entries_frame.grid(column=0, row=1, sticky="ew") # Layout the frames in the main window using a grid format, sticky="ew" stands for east and west, filling out the frame to the left and right
buttons_frame.grid(column=0, row=2, sticky="news") # Layout the frames in the main window using a grid format, sticky="news" stands for north, south, east and west, filling out the frame horizontally and vertically

### Frame Creation End


### Title Start

title_frame.columnconfigure((0, 2), weight=1) # Configures columns 0 and 2 to take up as much space as possible whlist being equal to each other
title = Label(title_frame, text="Julie Birthday Hire", font=title_font, bg="#F8B195") # Creates a Labal that has the text "Julie Birthday Hire" using the font preset title_font with a background colour of grey
title.grid(row=0, column=1, sticky="nsew", pady=(15, 0)) # Creates the title label in the GUI and makes it fill out the frame

### Title Start


### Entries Boxes Start
entries_frame.columnconfigure((0,4), weight=1) # Makes columns 2 take up as much space as possible
entries_frame.columnconfigure(2, weight=2) # Makes columns 2 take up as much space as possible

customer_name_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33,  highlightbackground="black", highlightthickness=3) # Configures a entry box that shows inputted text as grey and uses the font preset normal font (Ln.125)
customer_name_entry.insert(0, "Enter Your Full Name") # Inserts the text "Enter Your Full Name" into the entry box
customer_name_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Your Full Name")) # When entry box is clicked on, execute function focused (Ln.12)
customer_name_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Your Full Name")) # When entry box is clicked off, execute function unfocused (Ln.17)
customer_name_entry.grid(row=0, column=1) # Creates the entry box in the actual GUI


receipt_number_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33,  highlightbackground="black", highlightthickness=3) # Configures a entry box that shows inputted text as grey and uses the font preset normal font (Ln.125)
receipt_number_entry.insert(0, "Enter Your Receipt Number") # Inserts the text "Enter Your Receipt Number" into the entry box
receipt_number_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Your Receipt Number")) # When entry box is clicked on, execute function focused (Ln.12)
receipt_number_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Your Receipt Number")) # When entry box is clicked off, execute function unfocused (Ln.17)
receipt_number_entry.grid(row=0, column=3) # Creates the entry box in the actual GUI


item_hired_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33,  highlightbackground="black", highlightthickness=3) # Configures a entry box that shows inputted text as grey ad uses the font preset normal font (Ln.125)
item_hired_entry.insert(0, "Enter The Item Hired") # Inserts the text "Enter The Item Hired" into the entry box
item_hired_entry.bind('<FocusIn>', lambda e: focused(e, "Enter The Item Hired")) # When entry box is clicked on, execute function focused (Ln.12)
item_hired_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter The Item Hired")) # When entry box is clicked off, execute function unfocused (Ln.17)
item_hired_entry.grid(row=1, column=1, pady=(20, 0)) # Creates the entry box in the actual GUI


num_of_item_hired_entry = Entry(entries_frame, font=normal_font, fg="grey", width=33,  highlightbackground="black", highlightthickness=3) # Configures a entry box that shows inputted text as grey ad uses the font preset normal font (Ln.125)
num_of_item_hired_entry.insert(0, "Enter Amount Of Items Hired : 1 - 500") # Inserts the text "Enter Amounut Of Items Hired : 1 - 500" into the entry box
num_of_item_hired_entry.bind('<FocusIn>', lambda e: focused(e, "Enter Amount Of Items Hired : 1 - 500")) # When entry box is clicked on, execute function focused (Ln.12)
num_of_item_hired_entry.bind('<FocusOut>', lambda e: unfocused(e, "Enter Amount Of Items Hired : 1 - 500")) # When entry box is clicked off, execute function unfocused (Ln.17)
num_of_item_hired_entry.grid(row=1, column=3, pady=(20, 0)) # Creates the entry box in the actual GUI

 
### Entries Boxes End


### Buttons Start

buttons_frame.columnconfigure((0,2,4,6), weight=1) # Makes columns 0, 2, 4, 6 take up as much space as they can while being equal, pushes widgets in columns 1, 3 and 5 to the centre
buttons_frame.rowconfigure((0,2), weight=1) # Makes rows 0 and 2 take up as much space as they can while being equal, pushes widgets in row 1 to the centre


quit_button = Button(buttons_frame, text="Quit", font=button_font, command=quit_win, width=10) # Creates button with the text "Quit" which quits the program when clicked
quit_button.grid(row=1, column=1) # Creates the button in the GUI

submit_entries = Button(buttons_frame, text="Submit", font=button_font, command=submit, width=10) # Creates button with the text "Submit" which gets entries and checks if they're vaild when clicked (Ln.23)
submit_entries.grid(row=1, column=3) # Creates the button in the GUI

view_entries = Button(buttons_frame, text="View Entries", font=button_font, command=new_window, width=10) # Creates a button with the text "View Entries" which will open up the password window in order to access entries (Ln.63)
view_entries.grid(row=1, column=5) # Creates the button in the GUI

### Buttons End


### Tkinter Window Configuration Start
screen_x, screen_y = win.winfo_screenwidth(), win.winfo_screenheight() #Grabs device resolution


# Window Geometry Calculations
win_x = int(screen_x / 2) # Deciding window width based on screen size, so no matter what display, window will always take up 50%
win_y = int(screen_y / 4) # Deciding window height based on screen size, so no matter what display, window will always take up 25%


margin_x = int(screen_x / 2 - win_x / 2) # Adding padding so window will always appear in the middle
margin_y = int(screen_y / 2 - win_y / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

win.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}")
### Tkinter Window Configuration End


mainloop()