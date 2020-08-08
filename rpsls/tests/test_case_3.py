import unittest
from src.solution import solution
from tests.__fixtures__.feed3 import feed3


class TestSolution(unittest.TestCase):

    def test_tournament_3(self):
        sut = solution(feed3)

        sut.tournament()

        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(10, sut.getWinner().id)
        self.assertEqual([30, 31, 20, 11, 15], sut.getWinner().opponents)
