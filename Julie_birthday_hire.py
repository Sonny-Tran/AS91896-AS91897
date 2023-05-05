from tkinter import *
from Julie_birthday_hire_modules import modules


root = Tk()



win_x, win_y, margin_x, margin_y = modules.window_geometery()
root.geometry(f"{win_x}x{win_y}+{margin_x}+{margin_y}")

mainloop()