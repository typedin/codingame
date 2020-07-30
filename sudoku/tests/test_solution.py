import unittest
from src.solution import solution

correct = '''1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
9 1 2 3 4 5 6 7 8
3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
8 9 1 2 3 4 5 6 7
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
'''


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sut = solution(correct, 9)

    def test_validate_a_set(self):
        self.assertTrue(self.sut.is_valid([
            1, 4, 7, 9, 3, 6, 8, 2, 5
        ]))
        self.assertFalse(self.sut.is_valid([
            1, 1, 1, 1, 1, 1, 1, 1, 1
        ]))

    def test_first_case(self):
        self.assertTrue(solution(correct).is_correct())


if __name__ == '__main__':
    unittest.main()
