import src
import unittest
from src.signs import Draw
from src.player import Player
from tests.commonAssertion import CommonAssertion


class TestDraw(unittest.TestCase, CommonAssertion):

    @classmethod
    def setUpClass(cls):
        cls.sut = getattr(src.signs, "Draw")

    def test_both_player_must_have_the_same_sign(self):
        playerA = Player(1, "S")
        playerB = Player(2, "L")
        self.assertRaises(ValueError, Draw, playerA, playerB)

    def test_playerA_is_the_lowest(self):
        self.playerA = Player(1, "P")
        self.playerB = Player(2, "P")
        self.assertTrue(self.assert_playerA_wins())

    def test_playerB_is_the_lowest(self):
        self.playerA = Player(2, "P")
        self.playerB = Player(1, "P")
        self.assertTrue(self.assert_playerB_wins())
