from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.configure(bg="grey")


### Font Configuration Start

title_font = tkFont.Font(family="Helvetica",size=24,weight="bold")

### Font Configuration End



### Frame Creation Start


title_frame = Frame(root, padx=15, pady=15)
entries_frame = Frame(root, padx=15, pady=15)
buttons_frame = Frame(root, padx=15, pady=15)

title_frame.grid(column=0, row=0, sticky="ew")
entries_frame.grid(column=0, row=1, sticky="ew")
buttons_frame.grid(column=0, row=2, sticky="ew")


### Frame Creation End


### Title Start

Label(title_frame, text="Julie_Birthday_Hire", font=title_font)

### Title Start


### Entries Boxes Start







### Entries Boxes End



### Tkinter Window Configuration Start
screen_x, screen_y = root.winfo_screenwidth(), root.winfo_screenheight() #Grabs device resolution


# Window Geometry Calculations
win_x = int(screen_x / 3) # Deciding window width based on screen size, so no matter what display, window will always take up 33.333%
win_y = int(screen_y / 3) # Deciding window height based on screen size, so no matter what display, window will always take up 33.333%


margin_x = int(screen_x / 2 - win_x / 2) # Adding padding so window will always appear in the middle
margin_y = int(screen_y / 2 - win_y / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

root.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}")
### Tkinter Window Configuration End

mainloop()