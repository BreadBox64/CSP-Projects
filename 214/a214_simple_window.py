#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
from tkinter import *
from tkinter.font import *

# main window
root = Tk()
root.wm_geometry("200x100")
root.title("Authorization")

frame = Frame(root).grid()

usernameLabel = Label(frame, text='Username:').grid(column=0, row=0)
passwordLabel = Label(frame, text='Password:', font=Font(root, "Courier", "Courier")).grid(column=1, row=0)

root.mainloop()