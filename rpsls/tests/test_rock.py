import src
import unittest
from src.rock import Rock
from src.player import Player
from tests.commonAssertion import CommonAssertion


class TestRock(unittest.TestCase, CommonAssertion):

    @classmethod
    def setUpClass(cls):
        cls.sut = getattr(src.rock, "Rock")
        cls.playerA = Player(1, "R")

    def test_first_player_must_be_rock(self):
        playerA = Player(1, "NOT ROCK")
        playerB = Player(2, "P")
        self.assertRaises(ValueError, Rock, playerA, playerB)

    def test_rock_wins_over_lizard(self):
        self.playerB = Player(2, "L")
        self.assertTrue(self.assert_playerA_wins())

    def test_rock_wins_over_scissors(self):
        self.playerB = Player(2, "C")
        self.assertTrue(self.assert_playerA_wins())

    def test_rock_loses_against_paper(self):
        self.playerB = Player(2, "P")
        self.assertTrue(self.assert_playerB_wins())

    def test_rock_loses_against_spock(self):
        self.playerB = Player(2, "S")
        self.assertTrue(self.assert_playerB_wins())
