import src
import unittest
from src.paper import Paper
from src.player import Player
from tests.commonAssertion import CommonAssertion


class TestPaper(unittest.TestCase, CommonAssertion):

    @classmethod
    def setUpClass(cls):
        cls.sut = getattr(src.paper, "Paper")
        cls.playerA = Player(1, "P")

    def test_first_player_must_be_paper(self):
        playerA = Player(1, "NOT PAPER")
        playerB = Player(2, "S")
        self.assertRaises(ValueError, Paper, playerA, playerB)

    def test_paper_wins_over_rock(self):
        self.playerB = Player(2, "R")
        self.assertTrue(self.assert_playerA_wins())

    def test_paper_wins_over_spock(self):
        self.playerB = Player(2, "S")
        self.assertTrue(self.assert_playerA_wins())

    def test_paper_loses_against_lizard(self):
        self.playerB = Player(2, "L")
        self.assertTrue(self.assert_playerB_wins())

    def test_paper_loses_against_scissors(self):
        self.playerB = Player(2, "C")
        self.assertTrue(self.assert_playerB_wins())
