from __future__ import division

import numpy as np
class Game(object):

    def __init__(self):
        self.color='black'
        self.digest= {
            'Riki': np.array([0, 0, 0]),
            'Dyr': np.array([0, 0, 0]),
            'Raed': np.array([0, 0, 0]),
        }
        self.frame = np.zeros((480, 640, 3))

    def get_frame_from_game_state(self):
        self.frame = np.zeros((480, 640, 3))
        # self.frame[:, :, 0] = np.array(self.digest['Riki']/100)[None, None, :]
        # self.frame[:, :, 1] = np.array(self.digest['Dyr']/100)[None, None, :]
        self.frame[:, :, 2] = np.array(self.digest['Raed'] / 100)[None, None, :]
        return self.frame

    def get_updated(self, digest):
        if digest:
            self.digest = digest
