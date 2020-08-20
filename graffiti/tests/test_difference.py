import unittest
from src.solution import difference


class TestDifference(unittest.TestCase):

    def test_makes_difference_between_fence_and_one_set(self):
        sut = difference(10, [[1, 4]])
        self.assertEqual(
            next(sut),
            [0, 1]
        )
        self.assertEqual(
            next(sut),
            [4, 10]
        )

    def test_makes_difference_between_fence_and_many_sets(self):
        sets = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        sut = difference(10, sets)
        self.assertEqual(
            next(sut),
            [0, 1]
        )
        self.assertEqual(
            next(sut),
            [2, 3]
        )
        self.assertEqual(
            next(sut),
            [4, 5]
        )

    def test_no_duplication(self):
        sets = [
            [1, 2],
            [1, 2],
            [1, 2]
        ]
        self.assertEqual(
            next(difference(10, sets)),
            [0, 1]
        )

    def test_continuous(self):
        continuous = [[2, 100]]

        self.assertEqual(
            next(difference(100, continuous)),
            [0, 2]
        )
