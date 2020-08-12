import unittest
from src.solution import solution, caesarShift


class SolutionTest(unittest.TestCase):

    def test_example_input(self):
        readings = '''ENCODE
            4
            BDFHJLCPRTXVZNYEIWGAKMUSQO
            AJDKSIRUXBLHWTMCQGZNPYFVOE
            EKMFLGDQVZNTOWYHXUSPAIBRCJ
            AAA'''
        self.assertEqual(solution("AAA"), "KQF")

    def test_caesar_shift(self):
        self.assertEqual(caesarShift("AAA", 4), "EFG")
        self.assertEqual(caesarShift("ZZZ", 1), "ABC")
