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

color_cycle = cycle(['light blue', 'light pink', 'light green', 'light red', 'blue', 'pink', 'green', 'red'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

catcher_color = 'dark blue'
catcher_width = 100
catcher_height = 100
catcher_start_x1 = canvas_width / 2 - catcher_width / 2
catcher_start_y1 = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x1 + catcher_width
catcher_start_y2 = catcher_start_y1 + catcher_height

catcher = c.create_arc(catcher_start_x1, catcher_start_y1, catcher_start_x2, catcher_start_y2, start=200, extent=140,
                       style='arc', outline=catcher_color, width=3)

win.mainloop()
