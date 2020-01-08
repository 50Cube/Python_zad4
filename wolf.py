import math
from sheep import *


class Wolf:
    def __init__(self, distance):
        self.position = [1.5*init_pos_limit, 1.5*init_pos_limit]
        self.wolf_move_dist = distance
        self.circle = create_circle(self.position[0], self.position[1], 10, 'red')

    def print_wolf(self):
        print('Wilk znajduje sie na pozycji '
              '[' + '%0.3f' % self.position[0] + ', ' + '%0.3f' % self.position[1] + ']')

    def check_distance(self, sheeps):
        closest_sheep = sheeps[0]
        closest_sheep_distance = math.sqrt((sheeps[0].position[0] - self.position[0]) ** 2
                                           + (sheeps[0].position[1] - self.position[1]) ** 2)
        for i in range(1, len(sheeps)):
            if math.sqrt((sheeps[i].position[0] - self.position[0]) ** 2
                         + (sheeps[i].position[1] - self.position[1]) ** 2) < closest_sheep_distance:
                closest_sheep = sheeps[i]
                closest_sheep_distance = math.sqrt((sheeps[i].position[0] - self.position[0]) ** 2
                                                   + (sheeps[i].position[1] - self.position[1]) ** 2)
        return closest_sheep, closest_sheep_distance

    def move(self, sheep, distance, sheeps):
        if distance < self.wolf_move_dist:
            canvas.move(self.circle, sheep.position[0] - self.position[0], sheep.position[1] - self.position[1])
            self.position[0] = sheep.position[0]
            self.position[1] = sheep.position[1]
            sheeps.remove(sheep)
            update_sheep_label()
            if len(sheeps) == 0:
                last_sheep_eaten()
        else:
            vector = [0.0, 0.0]
            vector[0] = sheep.position[0] - self.position[0]
            vector[1] = sheep.position[1] - self.position[1]
            vector_length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
            canvas.move(self.circle, (vector[0] / vector_length) * self.wolf_move_dist, (vector[1] / vector_length) * self.wolf_move_dist)
            self.position[0] += (vector[0] / vector_length) * self.wolf_move_dist
            self.position[1] += (vector[1] / vector_length) * self.wolf_move_dist

    def relocate(self, x, y):
        canvas.move(self.circle, x - self.position[0], y - self.position[1])
        self.position[0] = x
        self.position[1] = y

    def __str__(self):
        return 'Wolf(position: ({0}; {1}))'.format('%0.3f' % self.position[0],
                                                   '%0.3f' % self.position[1])
