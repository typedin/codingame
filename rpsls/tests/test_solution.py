import unittest
from src.player import Player
from src.solution import solution

feed = '''8
4 R
1 P
8 P
3 R
7 C
5 S
6 L
2 L
'''


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution(feed)

    def test_case_scissors_vs_paper(self):
        playerA = Player(1, "C")
        playerB = Player(2, "P")

        winner = self.sut.fight(playerA, playerB)

        self.assertEqual(playerA.id, winner.id)
        self.assertEqual([2], playerA.get_opponents())

    def test_case_spock_vs_paper(self):
        playerA = Player(1, "S")
        playerB = Player(2, "P")
        winner = self.sut.fight(playerA, playerB)
        self.assertEqual(playerB.id, winner.id)
        self.assertEqual([1], playerB.get_opponents())
        pass
