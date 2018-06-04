import numpy as np
from lexical import KINGDOMS_NAME
from collections import OrderedDict

class Aggregator(object):

    def process_received_messages(self, received):
        # process all the messages

        digest = {}
        # for name in KINGDOMS_NAME:
            # digest[name] = np.array([33,33,34])

        if received:
            for chat_message in received:
                print("Got a message '%s' from %s" % (
                    chat_message['message'],
                    chat_message['username']
                ))
                collected = self.process_single_message(chat_message['message'])

                if collected:

                    try:
                        digest[collected.keys()[0]] = np.vstack((digest[collected.keys()[0]], collected.values()[0]))
                    except KeyError:
                        digest[collected.keys()[0]] = collected.values()[0]

            for key in digest.keys():
                if digest[key].shape.__len__() > 1:
                    digest[key] = digest[key].mean(axis=0)
            return digest

        return None

    def process_single_message(self, message):

        split_message = message.split(' ')
        if not split_message.__len__() == 4:
            return None
        if not split_message[0] in KINGDOMS_NAME:
            return None
        try:
            dict = {}
            dict[split_message[0]] = np.array([int(split_message[i]) for i in [1,2,3]])
        except ValueError:
            return None

        if dict.values()[0].sum() == 100:
            return dict
        else:
            return None