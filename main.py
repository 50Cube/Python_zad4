from tkinter import *
from sheep import *
from wolf import *

init_pos_limit = 200
sheeps = []
sheep_circles = []


def draw(wolf):
    canvas.pack()
    wolf.circle = create_circle(wolf.position[0], wolf.position[1], 10, canvas, "red")

    canvas.bind("<Key>", key)
    canvas.bind("<Button-1>", callback_left)
    canvas.bind("<Button-3>", lambda event, wolff=wolf: callback_right(event, wolff))

    # TODO: dostosowanie pozycji przyciskow do rozmiaru okna

    step_button = Button(window, text="Step", width=20, height=1).place(x=init_pos_limit/4, y=3 * init_pos_limit + 10)
    reset_button = Button(window, text="Reset", width=20, height=1, command=lambda wolff=wolf: click_reset(wolff)).place(x=init_pos_limit + 10, y=3 * init_pos_limit + 10)

    window.mainloop()


def create_circle(x, y, r, canvas, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color, outline="")


def key(event):
    print("pressed", repr(event.char))


def callback_left(event):
    print("Clicked at", event.x, event.y)
    add_sheep(event.x, event.y, 10)


def callback_right(event, wolff):
    print("Clicked at", event.x, event.y)
    move_wolf(wolff, event.x, event.y)


def add_sheep(x, y, sheep_distance):
    sheeps.append(Sheep(sheep_distance, x, y))
    tmp = create_circle(x, y, 10, canvas, "blue")
    sheep_circles.append(tmp)


def move_wolf(wolf, x, y):
    canvas.delete(wolf.circle)
    wolf.position[0] = x
    wolf.position[1] = y
    wolf.circle = create_circle(wolf.position[0], wolf.position[1], 10, canvas, "red")


def click_reset(wolf):
    move_wolf(wolf, 1.5*init_pos_limit, 1.5*init_pos_limit)
    sheeps.clear()
    for i in range(len(sheep_circles)):
        canvas.delete(sheep_circles[i])
    sheep_circles.clear()


def simulate(rounds, sheep_amount, sheep_limit, wolf_distance, sheep_distance):
    wolf = Wolf(wolf_distance)

    draw(wolf)

    for i in range(rounds):
        print('Numer tury: ' + str(i + 1))
        print('Liczba owiec: ' + str(len(sheeps)))
        wolf.print_wolf()
        if len(sheeps) == 0:
            print('Wilk zjadł wszystkie owce')
            break
        for j in range(len(sheeps)):
            sheeps[j].move_sheep()
            # sheeps[j].print_sheep()
        print()
        tmp_sheep, tmp_dist = wolf.check_distance(sheeps)
        wolf.move(tmp_sheep, tmp_dist, sheeps)


if __name__ == '__main__':
    window = Tk()
    window.title('HeRb')
    window.geometry(str(3 * init_pos_limit) + 'x' + str(3 * init_pos_limit + 40) + '+500-100')
    window.resizable(False, False)

    canvas = Canvas(window, width=3 * init_pos_limit, height=3 * init_pos_limit, bg="#42F058")

    simulate(50, 15, 10.0, 1.0, 0.5)
