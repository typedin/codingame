import unittest
from src.solution import solution
from tests.__fixtures__.feed1 import feed1


class TestSolution(unittest.TestCase):

    def test_tournament_1(self):
        sut = solution(feed1)

        sut.tournament()

        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(2, sut.getWinner().id)
        self.assertEqual([6, 5, 1], sut.getWinner().opponents)
