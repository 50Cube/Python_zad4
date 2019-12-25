import random
from globals import *

class Sheep:
    def __init__(self, distance, positionX, positionY):
        self.position = [positionX, positionY]
        self.sheep_move_dist = distance
        self.circle = create_circle(self.position[0], self.position[1], 10, 'blue')

    def print_sheep(self):
        print('Owca znajduje sie na pozycji {0}'.format(str(self.position)))

    def move_sheep(self):
        old_pos = [self.position[0], self.position[1]]
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

    # def __str__(self):
    #     return 'Sheep(id: {0}, position: ({1}; {2}))'.format(str(self.id),
    #                                                          '%0.3f' % self.position[0],
    #                                                          '%0.3f' % self.position[1])

    def __repr__(self):
        return self.__str__()
