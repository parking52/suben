import numpy as np

class Game(object):

    def __init__(self):
        self.color='black'

    def get_frame_from_game_state(self):
        frame = np.zeros((480, 640, 3))
        if self.color == "red":
            frame[:, :, :] = np.array(
                [1, 0, 0])[None, None, :]
        elif self.color == "green":
            frame[:, :, :] = np.array(
                [0, 1, 0])[None, None, :]
        elif self.color == "blue":
            frame[:, :, :] = np.array(
                [0, 0, 1])[None, None, :]
        return frame

    def get_updated(self, digest):
        if digest:
            if self.color != digest:
                print ('changing my color to ' + digest)

            self.color = digest