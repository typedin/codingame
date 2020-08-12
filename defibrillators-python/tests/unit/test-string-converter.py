import unittest
from src.solution import StringConverter, StringToDecimal


class WrongImplementationOfStringConverter(StringConverter):
    pass


class TestStringConverter(unittest.TestCase):

    def test_parse_method_must_be_implemented(self):
        with self.assertRaises(Exception):
            WrongImplementationOfStringConverter().parse()

    def test_a_string_must_be_passed(self):
        with self.assertRaises(ValueError):
            WrongImplementationOfStringConverter(None)


class TestToDecimal(unittest.TestCase):

    def test_it_converts_strings_with_comas_to_decimal(self):
        assert StringToDecimal("3,1415").parse() == 3.1415
