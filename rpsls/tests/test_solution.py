import unittest
from src.solution import solution
from tests.__fixtures__.feed1 import feed1
from tests.__fixtures__.feed2 import feed2
from tests.__fixtures__.feed3 import feed3
from tests.__fixtures__.feed4 import feed4
from tests.__fixtures__.feed5 import feed5


class TestSolution(unittest.TestCase):

    def test_tournament_1(self):
        sut = solution(feed1)
        sut.tournament()
        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(2, sut.getWinner().id)
        self.assertEqual([6, 5, 1], sut.getWinner().opponents)

    def test_tournament_2(self):
        sut = solution(feed2)
        sut.tournament()
        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(1, sut.getWinner().id)
        self.assertEqual([2], sut.getWinner().opponents)

    def test_tournament_3(self):
        sut = solution(feed3)
        sut.tournament()
        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(10, sut.getWinner().id)
        self.assertEqual([30, 31, 20, 11, 15], sut.getWinner().opponents)

    def test_tournament_4(self):
        sut = solution(feed4)
        sut.tournament()
        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(128, sut.getWinner().id)
        self.assertEqual([75, 2, 10, 29, 6, 1, 3], sut.getWinner().opponents)

    def test_tournament_5(self):
        sut = solution(feed5)
        sut.tournament()
        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(34, sut.getWinner().id)
        self.assertEqual(
            [45, 262, 229, 823, 283, 152, 24, 228, 230, 188],
            sut.getWinner().opponents
        )
