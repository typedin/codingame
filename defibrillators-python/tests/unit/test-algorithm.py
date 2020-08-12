import unittest
from src.solution import Algorithm, User, StringToDecimal, Defibrilator

linesForDefibrilators = [
    [
        "1",
        "Maison de la Prevention Sante",
        "6 rue Maguelone 340000 Montpellier",
        "",
        "3,87952263361082",
        "43,6071285339217",
    ],
    [
        "2",
        "Hotel de Ville",
        "1 place Georges Freche 34267 Montpellier",
        "",
        "3,89652239197876",
        "43,5987299452849",
    ],
    [
        "3",
        "Zoo de Lunaret",
        "50 avenue Agropolis 34090 Mtp",
        "",
        "3,87388031141133",
        "43,6395872778854"
    ]
]


class AlgorithmTest(unittest.TestCase):

    def createValidUser(self):
        return User(["3,879483", "43,608177"], StringToDecimal)

    def test_valid_user_must_be_provided(self):
        with self.assertRaises(ValueError):
            Algorithm(None, [])

    def test_an_array_of_defibrilators_is_required(self):
        with self.assertRaises(ValueError):
            Algorithm(self.createValidUser(), [])

    def test_raises_error_when_invalid_defibrilator_is_passed(self):
        with self.assertRaises(ValueError):
            Algorithm(self.createValidUser(), [{}, {}])
