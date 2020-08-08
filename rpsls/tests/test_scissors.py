import src
import unittest
from src.player import Player
from src.signs import Scissors
from tests.commonAssertion import CommonAssertion


class TestScissors(unittest.TestCase, CommonAssertion):

    @classmethod
    def setUpClass(cls):
        cls.sut = getattr(src.signs, "Scissors")
        cls.playerA = Player(1, "C")

    def test_first_player_must_be_scissors(self):
        playerA = Player(1, "NOT SCISSORS")
        playerB = Player(2, "P")
        self.assertRaises(ValueError, Scissors, playerA, playerB)

    def test_scissor_wins_over_paper(self):
        self.playerB = Player(2, "P")
        self.assertTrue(self.assert_playerA_wins())

    def test_scissor_wins_over_paper_lizard(self):
        self.playerB = Player(2, "L")
        self.assertTrue(self.assert_playerA_wins())

    def test_scissor_loses_against_rock(self):
        self.playerB = Player(2, "R")
        self.assertTrue(self.assert_playerB_wins())

    def test_scissor_loses_against_spock(self):
        self.playerB = Player(2, "S")
        self.assertTrue(self.assert_playerB_wins())
