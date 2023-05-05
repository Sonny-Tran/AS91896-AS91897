from tkinter import *

root = Tk()
root.withdraw()

class modules:
    def window_geometery():
        screen_x, screen_y = root.winfo_screenwidth(), root.winfo_screenheight() #Grabs device resolution

        # Window Geometry Calculations
        window_x = int(screen_x / 3) # Deciding window width based on screen size, so no matter what display, window will always take up 33.333%
        window_y = int(screen_y / 3) # Deciding window height based on screen size, so no matter what display, window will always take up 33.333%


        margin_x = int(screen_x / 2 - window_x / 2) # Adding padding so window will always appear in the middle
        margin_y = int(screen_y / 2 - window_y / 2) # Screen_height - Window_Height = Empty space on the side / 2 since we want the window to be in the middle

        return(window_x, window_y, margin_x, margin_y)