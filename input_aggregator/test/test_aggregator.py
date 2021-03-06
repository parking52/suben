from input_aggregator import aggregator
from unittest import TestCase
import numpy as np


class TestAggregator(TestCase):
    def setUp(self):
        self.agg = aggregator.Aggregator()

    def test_process_single_message(self):
        single_message = {'message': 'qqq', 'username': 'uuu'}
        actual_output = self.agg.process_single_message(single_message['message'])
        expected_output = None
        assert actual_output == expected_output

        single_message = {'message': 'Dyr war 18', 'username': 'u1'}
        actual_output = self.agg.process_single_message(single_message['message'])
        expected_output = None
        assert actual_output == expected_output

        single_message = {'message': 'Raed 25 25 25 25 ', 'username': 'u2'}
        actual_output = self.agg.process_single_message(single_message['message'])
        expected_output = None
        assert actual_output == expected_output

        single_message = {'message': 'Raed 25 25 25 25', 'username': 'u2'}
        actual_output = self.agg.process_single_message(single_message['message'])
        expected_output = {'Raed': np.array([25, 25, 25, 25])}
        assert actual_output.keys() == expected_output.keys()
        np.testing.assert_almost_equal(actual_output.values(), expected_output.values())


    def test_process_received_messages(self):

        sample_to_be_processed = [
            {'message': 'Raed 50 50 0 0', 'username': 'ccc'},
        ]
        actual_output = self.agg.process_received_messages(sample_to_be_processed)
        expected_output = {
            'Raed': np.array([50,50,0,0]),
        }
        assert actual_output.keys() == expected_output.keys()
        np.testing.assert_almost_equal(actual_output.values(), expected_output.values())



        sample_to_be_processed = [
            {'message': 'Dyr 50 50 50 0', 'username': 'ccc'}, # incorrect
            {'message': 'Dyr 50 50 0 0', 'username': 'ccc'},
            {'message': 'Dyr 70 30 0 0', 'username': 'ccc'},
            {'message': 'Dyr 0 40 60 0', 'username': 'ccc'},
        ]
        actual_output = self.agg.process_received_messages(sample_to_be_processed)
        expected_output = {
            'Dyr': np.array([40,40,20,0]),
        }
        assert actual_output.keys() == expected_output.keys()
        np.testing.assert_almost_equal(actual_output.values(), expected_output.values())



        sample_to_be_processed = [
            {'message': 'Dyr 40 40 20 0', 'username': 'ccc'},
            {'message': 'Dyr 20 20 60 0', 'username': 'ccc'},
            {'message': 'Raed 40 40 20 0', 'username': 'ccc'},
            {'message': 'Raed 20 20 60 0', 'username': 'ccc'},
            {'message': 'Riki 40 40 20 0', 'username': 'ccc'},
            {'message': 'Riki 20 20 60 0', 'username': 'ccc'},
        ]
        actual_output = self.agg.process_received_messages(sample_to_be_processed)
        expected_output = {
            'Riki': np.array([30, 30, 40, 0]),
            'Dyr': np.array([30, 30, 40, 0]),
            'Raed': np.array([30, 30, 40, 0]),
        }
        assert actual_output.keys() == expected_output.keys()
        np.testing.assert_almost_equal(actual_output.values(), expected_output.values())