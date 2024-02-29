#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
from tkinter import *
from tkinter.font import *
from tkinter.ttk import *

# main window
root = Tk()
root.wm_geometry("300x300")
root.title("Authorization")

f = Frame(root)
f.grid(column=0, row=0, sticky="NESW")
s = Style()
s.configure("Blue.TFrame", background='blue')
s.configure("Green.TFrame", background='green')
s.configure("Red.TFrame", background='red')
s.configure("Yellow.TFrame", background='yellow')
Frame(f, style="Blue.TFrame", width=200, height=150).grid(column=0, row=0)
Frame(f, style="Green.TFrame", width=100, height=150).grid(column=1, row=0)
Frame(f, style="Red.TFrame", width=200, height=150).grid(column=0, row=1)
Frame(f, style="Yellow.TFrame", width=100, height=150).grid(column=1, row=1)

root.mainloop()