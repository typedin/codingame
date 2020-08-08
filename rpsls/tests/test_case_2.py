import unittest
from src.solution import solution
from tests.__fixtures__.feed2 import feed2


class TestSolution(unittest.TestCase):

    def test_tournament_2(self):
        sut = solution(feed2)

        sut.tournament()

        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(1, sut.getWinner().id)
        self.assertEqual([2], sut.getWinner().opponents)
