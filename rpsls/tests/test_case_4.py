import unittest
from src.solution import solution
from tests.__fixtures__.feed4 import feed4


class TestSolution(unittest.TestCase):

    def test_tournament_4(self):
        sut = solution(feed4)

        sut.tournament()

        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(128, sut.getWinner().id)
        self.assertEqual([75, 2, 10, 29, 6, 1, 3], sut.getWinner().opponents)
