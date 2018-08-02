from __future__ import division
import numpy as np
import uuid
from kingdom import Kingdom

class Gamestate(object):

    def __init__(self):
        self.id = uuid.uuid4()
        self.kingdoms = {
            'Riki' : Kingdom('Riki'),
            'Dyr' : Kingdom('Dyr'),
            'Raed' : Kingdom('Raed')
        }
        self.n_kingdoms = 3
        ## structure du digest
        # For each kingdom the following:
        # Military power
        # Money
        # Economic power
        #
        self.digest= {
            'Riki': np.array([0, 0, 0]),
            'Dyr': np.array([0, 0, 0]),
            'Raed': np.array([0, 0, 0]),
        }

    def get_kingdom(self, name):
        return self.kingdoms[name]

    def get_frame_from_game_state(self):
        self.frame = np.zeros((480, 640, 3))
        # self.frame[:, :, 0] = np.array(self.digest['Riki']/100)[None, None, :]
        # self.frame[:, :, 1] = np.array(self.digest['Dyr']/100)[None, None, :]
        self.frame[:, :, 2] = np.array(self.digest['Raed'] / 100)[None, None, :]
        return self.frame

    def get_updated(self, digest):
        if digest:
            self.digest = digest

        self.kingdoms['Riki'].next_stage()
        self.kingdoms['Dyr'].next_stage()
        self.kingdoms['Raed'].next_stage()


