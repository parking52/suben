from gamer import gamestate
from unittest import TestCase
import numpy as np


class TestGamestate(TestCase):
    def setUp(self):
        pass

    def test_init_gamestate(self):
        g = gamestate.Gamestate()

        self.assertIsNotNone(g.id)
        self.assertEqual(g.n_kingdoms, 3)
        self.assertEqual(g.get_kingdom('Riki').money, 10)