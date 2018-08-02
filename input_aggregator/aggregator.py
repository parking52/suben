import numpy as np
from lexical import KINGDOMS_NAME
from collections import OrderedDict

class Aggregator(object):

    def process_received_messages(self, received):
        # process all the messages

        digest = {}
        # for name in KINGDOMS_NAME:
            # digest[name] = np.array([33,33,34,0])

        if received:
            for chat_message in received:
                print("Got a message '%s' from %s" % (
                    chat_message['message'],
                    chat_message['username']
                ))
                collected = self.process_single_message(chat_message['message'])

            #     if collected:
            #
            #         try:
            #             digest[collected.keys()[0]] = np.vstack((digest[collected.keys()[0]], collected.values()[0]))
            #         except KeyError:
            #             digest[collected.keys()[0]] = collected.values()[0]
            #
            # for key in digest.keys():
            #     if digest[key].shape.__len__() > 1:
            #         digest[key] = digest[key].mean(axis=0)
            return collected

        return None

    def process_single_message(self, message):

        print(message)

        direction = message

        if direction in ['up','down','right','left']:
            # print(direction)
            return direction

        return None