import random
from globals import *


class Sheep:
    def __init__(self, distance, position_x, position_y):
        self.position = [position_x, position_y]
        self.sheep_move_dist = distance
        self.circle = create_circle(self.position[0], self.position[1], 10, 'blue')

    def print_sheep(self):
        print('Owca znajduje sie na pozycji {0}'.format(str(self.position)))

    def move_sheep(self):
        direction = random.randint(0, 3)
        if direction == 0:
            self.position[1] += self.sheep_move_dist
            canvas.move(self.circle, 0, self.sheep_move_dist)
        elif direction == 1:
            self.position[0] += self.sheep_move_dist
            canvas.move(self.circle, self.sheep_move_dist, 0)
        elif self.position == 2:
            self.position[1] += -self.sheep_move_dist
            canvas.move(self.circle, 0, -self.sheep_move_dist)
        else:
            self.position[0] += -self.sheep_move_dist
            canvas.move(self.circle, -self.sheep_move_dist, 0)

    def __del__(self):
        try:
            canvas.delete(self.circle)
        except TclError:
            pass
