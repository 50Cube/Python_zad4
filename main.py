from tkinter import Button
from wolf import *
from globals import *

wolf = Wolf(10)


def callback_left(event):
    add_sheep(event.x, event.y, 5)


def callback_right(event):
    wolf.relocate(event.x, event.y)


def add_sheep(x, y, sheep_distance):
    sheeps.append(Sheep(sheep_distance, x, y))
    update_sheep_label()


def click_step():
    if len(sheeps) == 0:
        no_sheep_window = Toplevel(window)
        no_sheep_window.geometry('275x50+400-100')
        no_sheep_window.title('Error')
        display = Label(no_sheep_window, text="There are no sheep on map.")
        display.config(font=("Courier", 12))
        display.pack()
        no_sheep_window.focus_set()
        no_sheep_window.grab_set()
    else:
        simulate()


def click_reset():
    wolf.relocate(1.5*init_pos_limit, 1.5*init_pos_limit)
    sheeps.clear()
    update_sheep_label()


def simulate():
    for j in range(len(sheeps)):
        sheeps[j].move_sheep()
    tmp_sheep, tmp_dist = wolf.check_distance(sheeps)
    wolf.move(tmp_sheep, tmp_dist, sheeps)


canvas.bind("<Button-1>", callback_left)
canvas.bind("<Button-2>", callback_right)
canvas.bind("<Button-3>", callback_right)

step_button = Button(window, text="Step", width=init_pos_limit//10, height=1, command=click_step)\
    .place(x=init_pos_limit/4, y=3 * init_pos_limit + init_pos_limit//20)
reset_button = Button(window, text="Reset", width=init_pos_limit//10, height=1, command=click_reset)\
    .place(x=init_pos_limit + 10, y=3 * init_pos_limit + init_pos_limit//20)

if __name__ == '__main__':
    if init_pos_limit < 180 or init_pos_limit > 230:
        print('Incorrect window size')
        exit(0)
    window.mainloop()
