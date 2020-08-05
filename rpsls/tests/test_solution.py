import unittest
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

    def test_first_case(self):
        self.assertEqual(self.sut.result(), [2, [6, 5, 1]])

    def test_rules(self):
        pass
