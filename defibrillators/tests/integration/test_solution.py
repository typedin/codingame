import unittest
from src.solution import Solution, StringToDecimal, User, Defibrilator, Algorithm

lines = [
    "3,879483",
    "43,608177",
    "1",
    "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217",
    "2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849",
    "3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854"
]


class SolutionTest(unittest.TestCase):
    def test_cannot_be_instanciate_without_lines(self):
        with self.assertRaises(ValueError):
            Solution(None, StringToDecimal)

    def test_cannot_be_instanciate_without_a_StringFormator(self):
        with self.assertRaises(ValueError):
            Solution(lines, None)

    def test_it_instanciates_a_user(self):
        expectedLon = 3.879483
        expectedLat = 43.608177

        user = Solution(lines, StringToDecimal).user()

        assert isinstance(user, User)
        assert user.lat == expectedLat
        assert user.lon == expectedLon

    def test_it_creates_an_array_of_defibrilators(self):
        defibrilators = Solution(lines, StringToDecimal).defibrilators()

        assert len(defibrilators) == 3
        for defibrilator in defibrilators:
            assert isinstance(defibrilator, Defibrilator)

    def test_it_returns_the_closest_defibrilator(self):
        assert Solution(lines, StringToDecimal).getClosest(Algorithm).name() == "Maison de la Prevention Sante"
