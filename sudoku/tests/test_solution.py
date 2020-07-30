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

    def test_correct_row(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            self.sut.get_row(0)
        )

    def test_correct_column(self):
        self.assertEqual(
            [1, 4, 7, 9, 3, 6, 8, 2, 5],
            self.sut.get_column(0)
        )

    def test_correct_cell(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            self.sut.get_cell(0)
        )
        self.assertEqual(
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            self.sut.get_cell(1)
        )
        self.assertEqual(
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
            self.sut.get_cell(3)
        )

    def test_a_row_can_be_valid(self):
        self.assertTrue(self.sut.is_valid([
            1, 4, 7, 9, 3, 6, 8, 2, 5
        ]))

    def test_first_case(self):
        self.assertTrue(solution(correct).is_correct())


if __name__ == '__main__':
    unittest.main()
