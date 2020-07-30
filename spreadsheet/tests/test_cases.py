import unittest
from src.solution import solution
from tests.__fixtures__.cases import cases


class TestParser(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(
            solution(cases[0]["input"].splitlines()),
            cases[0]["expectation"]
        )

    def test_case_1(self):
        self.assertEqual(
            solution(cases[1]["input"].splitlines()),
            cases[1]["expectation"]
        )

    def test_case_2(self):
        self.assertEqual(
            solution(cases[2]["input"].splitlines()),
            cases[2]["expectation"]
        )

    def test_case_3(self):
        self.assertEqual(
            solution(cases[3]["input"].splitlines()),
            cases[3]["expectation"]
        )

    def test_case_4(self):
        self.assertEqual(
            solution(cases[4]["input"].splitlines()),
            cases[4]["expectation"]
        )

    def test_case_5(self):
        self.assertEqual(
            solution(cases[5]["input"].splitlines()),
            cases[5]["expectation"]
        )

    def test_case_6(self):
        self.assertEqual(
            solution(cases[6]["input"].splitlines()),
            cases[6]["expectation"]
        )

    def test_case_7(self):
        self.assertEqual(
            solution(cases[7]["input"].splitlines()),
            cases[7]["expectation"]
        )

    def test_case_8(self):
        self.assertEqual(
            solution(cases[8]["input"].splitlines()),
            cases[8]["expectation"]
        )

    def test_case_9(self):
        self.assertEqual(
            solution(cases[9]["input"].splitlines()),
            cases[9]["expectation"]
        )

    def test_case_10(self):
        self.assertEqual(
            solution(cases[10]["input"].splitlines()),
            cases[10]["expectation"]
        )

    def test_case_11(self):
        self.assertEqual(
            solution(cases[11]["input"].splitlines()),
            cases[11]["expectation"]
        )

    def test_case_12(self):
        self.assertEqual(
            solution(cases[12]["input"].splitlines()),
            cases[12]["expectation"]
        )

    def test_case_13(self):
        self.assertEqual(
            solution(cases[13]["input"].splitlines()),
            cases[13]["expectation"]
        )


if __name__ == '__main__':
    unittest.main()
