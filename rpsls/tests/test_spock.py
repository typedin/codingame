import src
import unittest
from src.signs import Spock
from src.player import Player
from tests.commonAssertion import CommonAssertion


class TestSpock(unittest.TestCase, CommonAssertion):

    @classmethod
    def setUpClass(cls):
        cls.sut = getattr(src.signs, "Spock")
        cls.playerA = Player(1, "S")

    def test_first_player_must_be_spock(self):
        playerA = Player(1, "NOT SPOCK")
        playerB = Player(2, "P")
        self.assertRaises(ValueError, Spock, playerA, playerB)

    def test_spock_wins_over_scissors(self):
        self.playerB = Player(2, "C")
        self.assertTrue(self.assert_playerA_wins())

    def test_spock_wins_over_rock(self):
        self.playerB = Player(2, "R")
        self.assertTrue(self.assert_playerA_wins())

    def test_spock_loses_against_paper(self):
        self.playerB = Player(2, "P")
        self.assertTrue(self.assert_playerB_wins())

    def test_spock_loses_against_lizard(self):
        self.playerB = Player(2, "L")
        self.assertTrue(self.assert_playerB_wins())
