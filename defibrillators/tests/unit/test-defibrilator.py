import unittest
from src.solution import Defibrilator, StringToDecimal

class Dummy():
    pass

class DefibrilatorTest(unittest.TestCase):

    def test_cannot_be_instanciate_without_an_entry(self):
        with self.assertRaises(ValueError):
            Defibrilator(None, None)

    def test_entry_must_be_the_right_size(self):
        with self.assertRaises(ValueError):
            Defibrilator([{}, {}], None)

    def test_a_formator_must_be_passed(self):
        with self.assertRaises(ValueError):
            Defibrilator([{}]*6, Dummy)

    def test_it_has_getters_for_name_address_longitude_and_latitude(self):
        lines = [
            "3",
            "Zoo de Lunaret",
            "50 avenue Agropolis 34090 Mtp",
            "",
            "3,87388031141133",
            "43,6395872778854"
        ]
        defibrilator = Defibrilator(lines, StringToDecimal)

        assert defibrilator.name() == "Zoo de Lunaret"
        assert defibrilator.address() == "50 avenue Agropolis 34090 Mtp"
        assert defibrilator.lon() == 3.87388031141133
        assert defibrilator.lat() == 43.6395872778854
