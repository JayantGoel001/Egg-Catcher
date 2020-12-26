from itertools import cycle
from random import randrange
from tkinter import *

canvas_width = 800
canvas_height = 400

win = Tk()
c = Canvas(win, width=canvas_width, height=canvas_height, background='deep sky blue')
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='dark green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

win.mainloop()
