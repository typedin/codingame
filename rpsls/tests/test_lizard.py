import src
import unittest
from src.signs import Lizard
from src.player import Player
from tests.commonAssertion import CommonAssertion


class TestLizard(unittest.TestCase, CommonAssertion):

    @classmethod
    def setUpClass(cls):
        cls.sut = getattr(src.signs, "Lizard")
        cls.playerA = Player(1, "L")

    def test_first_player_must_be_lizard(self):
        playerA = Player(1, "NOT LIZARD")
        playerB = Player(2, "P")
        self.assertRaises(ValueError, Lizard, playerA, playerB)

    def test_lizard_wins_over_paper(self):
        self.playerB = Player(2, "P")
        self.assertTrue(self.assert_playerA_wins())

    def test_lizard_wins_over_spock(self):
        self.playerB = Player(2, "S")
        self.assertTrue(self.assert_playerA_wins())

    def test_lizard_loses_against_rock(self):
        self.playerB = Player(2, "R")
        self.assertTrue(self.assert_playerB_wins())

    def test_lizard_loses_against_scissors(self):
        self.playerB = Player(2, "C")
        self.assertTrue(self.assert_playerB_wins())
