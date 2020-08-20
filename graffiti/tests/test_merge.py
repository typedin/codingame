import unittest
from src.solution import merge


class TestMerge(unittest.TestCase):

    def test_one_portion(self):
        mergeables = [[1, 4]]
        self.assertEqual(
            merge(mergeables),
            [(1, 4)]
        )

    def test_non_overlappings_are_returned_as_is(self):
        non_overlappings = [
            [1, 2],
            [3, 5]
        ]
        self.assertEqual(
            merge(non_overlappings),
            [(1, 2), (3, 5)]
        )

    def test_merges_two_overlapping_with_one_starting_inside_the_other(self):
        mergeables = [
            [1, 4],
            [2, 5]
        ]
        self.assertEqual(
            merge(mergeables),
            [(1, 5)]
        )
        inverted_mergeables = [
            [1, 4],
            [2, 5]
        ]
        self.assertEqual(
            merge(inverted_mergeables),
            [(1, 5)]
        )

    def test_one_inside(self):
        mergeable_with_one_inside = [
            [1, 4],
            [2, 3]
        ]
        self.assertEqual(
            merge(mergeable_with_one_inside),
            [(1, 4)]
        )

    def test_over_boundaries(self):
        over_boundaries = [
            [1, 4],
            [2, 3],
            [2, 43],
        ]
        self.assertEqual(
            merge(over_boundaries),
            [(1, 43)]
        )

    def test_overlapping(self):
        overlappings = [
            [1, 4],
            [1, 3]
        ]
        self.assertEqual(
            merge(overlappings),
            [(1, 4)]
        )
        overlappings = [
            [1, 2],
            [1, 4]
        ]
        self.assertEqual(
            merge(overlappings),
            [(1, 4)]
        )

    def test_continuous(self):
        many_continuous = [
            [2, 3],
            [3, 20],
            [20, 30],
            [30, 40],
            [41, 60],
            [60, 70],
            [70, 88],
            [88, 99],
            [99, 100],
            [40, 41],
        ]
        self.assertEqual(
            merge(many_continuous),
            [(2, 100)]
        )
