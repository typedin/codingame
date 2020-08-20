import unittest
from src.solution import solution


class TestSolution(unittest.TestCase):

    def test_example(self):
        readings = '''10
        2
        1 4
        5 6'''
        self.assertEqual(
            solution(readings),
            [
                [0, 1],
                [4, 5],
                [6, 10]
            ]
        )

    def test_overlapping_1(self):
        readings = '''10
        2
        1 4
        3 5'''
        self.assertEqual(
            solution(readings),
            [
                [0, 1],
                [5, 10]
            ]
        )

    def test_overlapping_2(self):
        readings = '''10
        2
        1 4
        2 3'''

        self.assertEqual(
            solution(readings),
            [
                [0, 1],
                [4, 10]
            ]
        )

    def test_continuous(self):
        readings = '''100
        10
        2 3
        3 20
        20 30
        30 40
        41 60
        60 70
        70 88
        88 99
        99 100
        40 41'''
        self.assertEqual(
            solution(readings),
            [
                [0, 2],
            ]
        )

    def test_all_painted(self):
        readings = '''12
        5
        6 10
        0 4
        7 8
        3 7
        8 12'''
        self.assertEqual(
            solution(readings),
            []
        )

    def test_long_fence(self):
        readings = '''2000000000
        5
        2 4
        6 10
        7 8
        3 7
        8 12'''
        self.assertEqual(
            solution(readings),
            [
                [0, 2],
                [12, 2000000000]
            ]
        )
