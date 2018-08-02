from __future__ import division

import numpy as np
class Game(object):

    def __init__(self):
        self.color='black'
        self.position=(100,100)
        self.digest= None
        self.frame = np.zeros((480, 640, 3))

    def get_frame_from_game_state(self):
        self.frame = np.zeros((480, 640, 3))
        self.add_dot_to_frame()

        return self.frame

    def add_dot_to_frame(self):
        for i in range(480):
            for j in range(640):
                if (i-240 + self.position[0])**2 + (j-320 +self.position[1])**2 < 100 :
                    self.frame[i,j]= np.array((1,1,1))

    def get_updated(self, digest):

        if digest == 'up':
            print('match up')
            self.position = (self.position[0] + 50, self.position[1] )
        if digest == 'down':
            print('match down')
            self.position = (self.position[0] - 50, self.position[1])
        if digest == 'right':
            print('match right')
            self.position = (self.position[0], self.position[1] - 50)
        if digest == 'left':
            print('match left')
            self.position = (self.position[0], self.position[1] + 50)

