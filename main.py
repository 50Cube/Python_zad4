from tkinter import *
import wolf
from sheep import *
from wolf import *

init_pos_limit = 200


def draw(wolf):
    window = Tk()
    window.title('HeRb')
    window.geometry(str(3 * init_pos_limit) + 'x' + str(3 * init_pos_limit))
    window.resizable(False, False)

    canvas = Canvas(window, width=3 * init_pos_limit, height=3 * init_pos_limit, bg="#42F058")
    canvas.pack()
    create_circle(wolf.position[0], wolf.position[1], 10, canvas, "red")

    window.mainloop()


def create_circle(x, y, r, canvas, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color, outline="")


def simulate(rounds, sheep_amount, sheep_limit, wolf_distance, sheep_distance):
    sheeps = []
    wolf = Wolf(wolf_distance)

    # for i in range(sheep_amount):
    #     sheeps.append(Sheep(i, sheep_limit, sheep_distance, 0, 0))

    draw(wolf)

    for i in range(rounds):
        print('Numer tury: ' + str(i+1))
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
    simulate(50, 15, 10.0, 1.0, 0.5)
