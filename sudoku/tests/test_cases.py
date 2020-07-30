import unittest
from src.solution import solution
from tests.__fixtures__.cases import cases


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        case = cases[0]
        self.assertEqual(
            case["expectation"],
            solution(case["input"]).is_correct()
        )

    def test_case_2(self):
        case = cases[1]
        self.assertEqual(
            case["expectation"],
            solution(case["input"]).is_correct()
        )

    def test_case_3(self):
        case = cases[2]
        self.assertEqual(
            case["expectation"],
            solution(case["input"]).is_correct()
        )

    def test_case_4(self):
        case = cases[3]
        self.assertEqual(
            case["expectation"],
            solution(case["input"]).is_correct()
        )

    def test_case_5(self):
        case = cases[4]
        self.assertEqual(
            case["expectation"],
            solution(case["input"]).is_correct()
        )


if __name__ == '__main__':
    unittest.main()
