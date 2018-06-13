from gamer import kingdom
from unittest import TestCase
import numpy as np


class TestKingdom(TestCase):
    def setUp(self):
        pass

    def test_init_kingdom(self):
        k = kingdom.Kingdom('Riki')
        assert k.money == 10


    def test_next_stage(self):
        k = kingdom.Kingdom('Riki')
        k.next_stage()
        k.next_stage()
