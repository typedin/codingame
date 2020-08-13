import unittest
from src.solution import solution, caesar, mapRotor


encode3 = '''ENCODE
4
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
AAA'''

encode23 = '''ENCODE
7
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
WEATHERREPORTWINDYTODAY'''

encode21 = '''ENCODE
9
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
EVERYONEISWELCOMEHERE'''

encode42 = '''ENCODE
9
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
EVERYONEISWELCOMEHEREEVERYONEISWELCOMEHERE
'''

decode21 = '''DECODE
9
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
PQSACVVTOISXFXCIAMQEM
'''

decode49 = '''DECODE
5
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
XPCXAUPHYQALKJMGKRWPGYHFTKRFFFNOUTZCABUAEHQLGXREZ
'''


class SolutionTest(unittest.TestCase):

    def test_caesar_shift(self):
        self.assertEqual(
            caesar("AAA", 4),
            "EFG"
        )
        self.assertEqual(
            caesar("ZZZ", 1),
            "ABC"
        )
        self.assertEqual(
            caesar("ABCD", 4),
            "EGIK"
        )
        self.assertEqual(
            caesar("EGIK", 4, True),
            "ABCD",
        )
        self.assertEqual(
            caesar("EFG", 4, True),
            "AAA"
        )

    def test_mapRotor(self):
        rotor = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        inText = "KFDI"
        self.assertEqual(mapRotor(rotor, inText), "BDGV")

        rotor = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        inText = "BDGV"
        self.assertEqual(mapRotor(rotor, inText), "JCRX")

        rotor = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        inText = "JCRX"
        self.assertEqual(mapRotor(rotor, inText), "EGIK")


    def test_encode(self):
        self.assertEqual(
            solution(encode3.splitlines()),
            "KQF"
        )
        self.assertEqual(
            solution(encode23.splitlines()),
            "ALWAURKQEQQWLRAWZHUYKVN"
        )
        self.assertEqual(
            solution(encode21.splitlines()),
            "PQSACVVTOISXFXCIAMQEM"
        )
        self.assertEqual(
            solution(encode42.splitlines()),
            "PQSACVVTOISXFXCIAMQEMDZIXFJJSTQIENEFQXVZYV"
        )

    def test_decode(self):
        self.assertEqual(
            solution(decode21.splitlines()),
            "EVERYONEISWELCOMEHERE"
        )

        self.assertEqual(
            solution(decode49.splitlines()),
            "THEQUICKBROWNFOXJUMPSOVERALAZYSPHINXOFBLACKQUARTZ"
        )
