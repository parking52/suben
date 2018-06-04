import numpy as np

class Aggregator(object):

    def process_received_messages(self, received):
        # process all the messages

        color = None
        if received:
            for chat_message in received:
                print("Got a message '%s' from %s" % (
                    chat_message['message'],
                    chat_message['username']
                ))
                color = chat_message['message'] if chat_message['message'] in ['red', 'blue', 'green'] else ''

        return color