import random


class Sheep:
    def __init__(self, id, limit, distance, positionX, positionY):
        self.id = id
        self.init_pos_limit = limit
        self.position = [positionX, positionY]
        self.sheep_move_dist = distance

    def print_sheep(self):
        print('Owca nr {0} znajduje sie na pozycji {1}'.format(str(self.id + 1), str(self.position)))

    def move_sheep(self):
        old_pos = [self.position[0], self.position[1]]
        direction = random.randint(0, 3)
        if direction == 0:
            self.position[1] += self.sheep_move_dist
        elif direction == 1:
            self.position[0] += self.sheep_move_dist
        elif self.position == 2:
            self.position[1] += -self.sheep_move_dist
        else:
            self.position[0] += self.sheep_move_dist

    def __str__(self):
        return 'Sheep(id: {0}, position: ({1}; {2}))'.format(str(self.id),
                                                             '%0.3f' % self.position[0],
                                                             '%0.3f' % self.position[1])

    def __repr__(self):
        return self.__str__()
