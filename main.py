from tkinter import *
from sheep import *
from wolf import *

init_pos_limit = 200


def simulate(rounds,
             sheep_amount,
             sheep_limit,
             wolf_distance,
             sheep_distance):
    sheeps = []
    wolf = Wolf(wolf_distance)

    for i in range(sheep_amount):
        sheeps.append(Sheep(i, sheep_limit, sheep_distance))

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
    window = Tk()
    window.title('HeRb')
    window.geometry(str(3*init_pos_limit) + 'x' + str(3*init_pos_limit))
    window.resizable(False, False)
    window.configure(background='#42F058')
    window.mainloop()
    simulate(50, 15, 10.0, 1.0, 0.5)
