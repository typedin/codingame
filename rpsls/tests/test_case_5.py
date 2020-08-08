import unittest
from src.solution import solution
from tests.__fixtures__.feed5 import feed5


class TestSolution(unittest.TestCase):

    def test_tournament_5(self):
        sut = solution(feed5)

        sut.tournament()

        self.assertEqual(1, len(sut.opponents))
        self.assertEqual(34, sut.getWinner().id)
        self.assertEqual(
            [45, 262, 229, 823, 283, 152, 24, 228, 230, 188],
            sut.getWinner().opponents
        )
