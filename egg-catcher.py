from itertools import cycle
from random import randrange
from tkinter import *
from tkinter import messagebox

eggs = []


def createEgg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    if egg_interval!=-1:
        win.after(egg_interval, createEgg)


def eggDropped(egg):
    global lives_remaining, egg_speed, egg_interval
    eggs.remove(egg)
    c.delete(egg)
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Lives : ' + str(lives_remaining))
    if lives_remaining == 0:
        for egg in eggs:
            c.delete(egg)
        eggs.clear()
        egg_speed = -1
        egg_interval = -1
        messagebox.showinfo('Game Over!!', 'Final Score : ' + str(score))
        win.destroy()


def moveEggs():
    for egg in eggs:
        (eggX1, eggY1, eggX2, eggY2) = c.coords(egg)
        c.move(egg, 0, 10)

        if eggY2 > canvas_height:
            eggDropped(egg)

    if egg_speed!=-1:
        win.after(egg_speed, moveEggs)


def checkCatch():
    global score, egg_interval, egg_speed
    (catcherX1, catcherY1, catcherX2, catcherY2) = c.coords(catcher)

    for egg in eggs:
        (eggX1, eggY1, eggX2, eggY2) = c.coords(egg)
        if catcherX1 <= eggX1 and eggX2 <= catcherX2 and catcherY2 - eggY2 < 30:
            eggs.remove(egg)
            c.delete(egg)
            score += egg_score
            egg_speed = int(egg_speed * 0.95)
            egg_interval = int(egg_interval * 0.95)
            c.itemconfigure(score_text, text='Score : ' + str(score))

    win.after(100, checkCatch)


def moveLeft(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)


def moveRight(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)


canvas_width = 800
canvas_height = 400

win = Tk()

c = Canvas(win, width=canvas_width, height=canvas_height, background='deep sky blue')

c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='dark green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

color_cycle = cycle(['light blue', 'light pink', 'light green', 'dark red', 'blue', 'pink', 'green', 'red'])
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

score = 0
score_text = c.create_text(15, 18, anchor='nw', font=('Arial', 14, 'bold'), fill='white', text='Score :' + str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width - 15, 18, anchor='ne', font=('Arial', 13, 'bold'), fill='white',
                           text='Lives : ' + str(lives_remaining))

c.bind('<Left>', moveLeft)
c.bind('<Right>', moveRight)
c.focus_set()

win.after(500, createEgg)
win.after(500, moveEggs)
win.after(1000, checkCatch)

win.title("Egg Catcher")
win.mainloop()
